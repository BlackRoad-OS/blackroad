"""Lucidia Platform API - AI-powered learning that actually works."""

from fastapi import FastAPI, HTTPException, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import base64
import random
import uuid
from datetime import datetime

# Import routers
from routers import billing
from routers import code
from routers import memory

app = FastAPI(
    title="Lucidia API",
    description="AI-powered learning platform - the end of technical barriers",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://lucidia.ai", "https://app.lucidia.ai"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(billing.router, prefix="/api/v1")
app.include_router(code.router)  # Code analysis router (50+ languages)
app.include_router(memory.router)  # 2048-style memory system


# ============================================================================
# Models
# ============================================================================

class ProblemInput(BaseModel):
    """Input for problem analysis."""
    text: Optional[str] = None
    image_base64: Optional[str] = None
    voice_transcript: Optional[str] = None
    subject: Optional[str] = None  # math, physics, chemistry, etc.
    grade_level: Optional[str] = None  # elementary, middle, high, college


class Explanation(BaseModel):
    """AI-generated explanation."""
    id: str
    problem_text: str
    subject: str
    difficulty: str
    steps: List[Dict[str, Any]]
    visualization_url: Optional[str] = None
    video_url: Optional[str] = None
    confidence: float
    created_at: datetime


class UserContext(BaseModel):
    """Persistent user learning context."""
    user_id: str
    learning_style: str  # visual, auditory, kinesthetic, reading
    strengths: List[str]
    areas_for_growth: List[str]
    recent_topics: List[str]
    session_count: int
    total_problems_solved: int


class VisualizationRequest(BaseModel):
    """Request for visual content generation."""
    concept: str
    type: str  # "2d_graph", "3d_model", "animation", "diagram"
    context: Optional[str] = None


class HealthResponse(BaseModel):
    """Health check response."""
    status: str
    version: str
    services: Dict[str, str]


# ============================================================================
# In-memory storage (replace with database in production)
# ============================================================================

user_contexts: Dict[str, UserContext] = {}
explanations_cache: Dict[str, Explanation] = {}
practice_problems: Dict[str, Dict[str, Any]] = {}

# Practice problem bank organized by subject and difficulty
PROBLEM_BANK: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "math": {
        "easy": [
            {
                "scenario": "You have 12 cookies to share equally among 4 friends. How many cookies does each friend get?",
                "problem": "12 ÷ 4 = ?",
                "answer": "3",
                "topic": "division",
                "hints": ["Think about grouping the cookies", "Each friend should get the same amount"],
                "visualization_prompt": "12 cookies being distributed to 4 people",
                "feedback_correct": "Great job! 12 ÷ 4 = 3. Each friend gets 3 cookies.",
                "feedback_incorrect": "Not quite. Try thinking about how to split 12 items into 4 equal groups.",
            },
            {
                "scenario": "A farmer has 7 apple trees. Each tree has 6 apples. How many apples does the farmer have in total?",
                "problem": "7 × 6 = ?",
                "answer": "42",
                "topic": "multiplication",
                "hints": ["Multiply the number of trees by the apples per tree", "You can add 6 seven times"],
                "visualization_prompt": "7 apple trees each with 6 apples",
                "feedback_correct": "Correct! 7 × 6 = 42. The farmer has 42 apples in total.",
                "feedback_incorrect": "Not quite. Try multiplying the number of trees (7) by the apples on each tree (6).",
            },
            {
                "scenario": "You saved $15 from your allowance and your grandma gives you $23 for your birthday. How much money do you have now?",
                "problem": "15 + 23 = ?",
                "answer": "38",
                "topic": "addition",
                "hints": ["Add the two amounts together", "Try adding the tens first, then the ones"],
                "visualization_prompt": "Two groups of dollar bills being combined",
                "feedback_correct": "That's right! $15 + $23 = $38. You now have $38!",
                "feedback_incorrect": "Not quite. Try adding 15 and 23 together. Add the ones first (5+3), then the tens (10+20).",
            },
            {
                "scenario": "A pizza has 8 slices. You eat 3 slices. How many slices are left?",
                "problem": "8 - 3 = ?",
                "answer": "5",
                "topic": "subtraction",
                "hints": ["Start with the total number of slices", "Take away the slices you ate"],
                "visualization_prompt": "A pizza with 8 slices, 3 removed",
                "feedback_correct": "Correct! 8 - 3 = 5. There are 5 slices left.",
                "feedback_incorrect": "Not quite. Start with 8 slices and take away 3. How many remain?",
            },
        ],
        "medium": [
            {
                "scenario": "A rectangular garden is 12 meters long and 8 meters wide. What is its area?",
                "problem": "12 × 8 = ?",
                "answer": "96",
                "topic": "area",
                "hints": ["Area of a rectangle = length × width", "Multiply the two dimensions"],
                "visualization_prompt": "A rectangular garden with dimensions labeled",
                "feedback_correct": "Correct! 12 × 8 = 96 square meters.",
                "feedback_incorrect": "Not quite. To find the area of a rectangle, multiply length (12) by width (8).",
            },
            {
                "scenario": "A store sells notebooks for $4 each. If you buy 3 notebooks and pay with a $20 bill, how much change do you get?",
                "problem": "20 - (4 × 3) = ?",
                "answer": "8",
                "topic": "multi-step",
                "hints": ["First find the total cost of 3 notebooks", "Then subtract that from $20"],
                "visualization_prompt": "3 notebooks priced at $4 each, paying with a $20 bill",
                "feedback_correct": "Correct! 3 notebooks cost $12, and $20 - $12 = $8 change.",
                "feedback_incorrect": "Not quite. First calculate the total cost: 4 × 3 = $12. Then find the change: $20 - $12.",
            },
            {
                "scenario": "You need to share 3 pizzas equally among 4 people. What fraction of a pizza does each person get?",
                "problem": "3 ÷ 4 = ?",
                "answer": "3/4",
                "topic": "fractions",
                "hints": ["Think about dividing each pizza into 4 parts", "Each person gets some slices from each pizza"],
                "visualization_prompt": "3 pizzas being divided among 4 people",
                "feedback_correct": "Correct! Each person gets 3/4 of a pizza.",
                "feedback_incorrect": "Not quite. If you divide 3 pizzas among 4 people, each gets 3/4 of a pizza.",
            },
        ],
        "hard": [
            {
                "scenario": "A train travels at 60 km/h for 2.5 hours, then at 80 km/h for 1.5 hours. What is the total distance traveled?",
                "problem": "(60 × 2.5) + (80 × 1.5) = ?",
                "answer": "270",
                "topic": "distance",
                "hints": ["Calculate each leg separately: distance = speed × time", "Then add the two distances together"],
                "visualization_prompt": "A train journey with two legs at different speeds",
                "feedback_correct": "Correct! (60 × 2.5) + (80 × 1.5) = 150 + 120 = 270 km.",
                "feedback_incorrect": "Not quite. First leg: 60 × 2.5 = 150 km. Second leg: 80 × 1.5 = 120 km. Total: 150 + 120.",
            },
            {
                "scenario": "A circle has a radius of 7 cm. What is its area? (Use π ≈ 3.14)",
                "problem": "π × 7² = ?",
                "answer": "153.86",
                "topic": "geometry",
                "hints": ["Area of a circle = π × r²", "First square the radius, then multiply by π"],
                "visualization_prompt": "A circle with radius 7 cm labeled",
                "feedback_correct": "Correct! π × 7² = 3.14 × 49 = 153.86 cm².",
                "feedback_incorrect": "Not quite. First square the radius: 7² = 49. Then multiply by π: 3.14 × 49.",
            },
        ],
    },
    "physics": {
        "easy": [
            {
                "scenario": "A car travels 100 kilometers in 2 hours. What is its average speed?",
                "problem": "100 ÷ 2 = ?",
                "answer": "50",
                "topic": "speed",
                "hints": ["Speed = distance ÷ time", "Divide the total distance by the total time"],
                "visualization_prompt": "A car traveling 100 km in 2 hours",
                "feedback_correct": "Correct! 100 km ÷ 2 hours = 50 km/h.",
                "feedback_incorrect": "Not quite. Speed = distance ÷ time. Divide 100 km by 2 hours.",
            },
        ],
        "medium": [
            {
                "scenario": "An object has a mass of 10 kg and accelerates at 3 m/s². What is the force applied?",
                "problem": "F = 10 × 3 = ?",
                "answer": "30",
                "topic": "force",
                "hints": ["Use Newton's second law: F = m × a", "Multiply mass by acceleration"],
                "visualization_prompt": "A 10 kg object being pushed with acceleration of 3 m/s²",
                "feedback_correct": "Correct! F = m × a = 10 × 3 = 30 Newtons.",
                "feedback_incorrect": "Not quite. Use F = m × a. Multiply the mass (10 kg) by the acceleration (3 m/s²).",
            },
        ],
        "hard": [
            {
                "scenario": "A ball is dropped from a height of 45 meters. How long does it take to hit the ground? (g = 10 m/s²)",
                "problem": "t = √(2h/g) = √(2×45/10) = ?",
                "answer": "3",
                "topic": "free-fall",
                "hints": ["Use the formula: h = ½gt²", "Rearrange to t = √(2h/g)"],
                "visualization_prompt": "A ball falling from 45 meters height",
                "feedback_correct": "Correct! t = √(2×45/10) = √9 = 3 seconds.",
                "feedback_incorrect": "Not quite. Using h = ½gt², we get t = √(2h/g) = √(90/10) = √9.",
            },
        ],
    },
}


# ============================================================================
# Core Endpoints
# ============================================================================

@app.get("/health", response_model=HealthResponse)
async def health():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        version="0.1.0",
        services={
            "api": "operational",
            "ai_tutor": "operational",
            "visualizer": "operational",
            "memory": "operational",
        }
    )


@app.post("/api/v1/problems/analyze", response_model=Explanation)
async def analyze_problem(problem: ProblemInput):
    """
    Analyze a problem and generate personalized explanation.

    Accepts:
    - Text description
    - Image (base64 encoded)
    - Voice transcript

    Returns step-by-step explanation with optional visualization.
    """
    # Determine problem text from input
    problem_text = problem.text or problem.voice_transcript or "Image problem"

    # Auto-detect subject if not provided
    subject = problem.subject or _detect_subject(problem_text)

    # Generate explanation ID
    explanation_id = str(uuid.uuid4())

    # TODO: Connect to lucidia-core mathematician/physicist for actual analysis
    # For now, return structured response

    explanation = Explanation(
        id=explanation_id,
        problem_text=problem_text,
        subject=subject,
        difficulty=_assess_difficulty(problem_text),
        steps=[
            {
                "number": 1,
                "title": "Understand the Problem",
                "content": f"Let's break down what we're solving: {problem_text}",
                "visualization": None,
            },
            {
                "number": 2,
                "title": "Identify Key Concepts",
                "content": "The key mathematical concepts involved are...",
                "visualization": "concept_map",
            },
            {
                "number": 3,
                "title": "Apply the Method",
                "content": "Here's how we solve it step by step...",
                "visualization": "step_animation",
            },
            {
                "number": 4,
                "title": "Verify the Answer",
                "content": "Let's check our work to make sure it's correct...",
                "visualization": None,
            },
        ],
        visualization_url=f"/api/v1/visualizations/{explanation_id}",
        confidence=0.95,
        created_at=datetime.utcnow(),
    )

    explanations_cache[explanation_id] = explanation
    return explanation


@app.post("/api/v1/problems/upload")
async def upload_problem_image(file: UploadFile = File(...)):
    """
    Upload an image of a problem for analysis.

    Supports: PNG, JPG, PDF
    Max size: 10MB
    """
    if file.content_type not in ["image/png", "image/jpeg", "application/pdf"]:
        raise HTTPException(400, "Unsupported file type. Use PNG, JPG, or PDF.")

    contents = await file.read()
    if len(contents) > 10 * 1024 * 1024:
        raise HTTPException(400, "File too large. Max 10MB.")

    # Encode and analyze
    image_base64 = base64.b64encode(contents).decode()

    # Create problem input and analyze
    problem = ProblemInput(image_base64=image_base64)
    return await analyze_problem(problem)


@app.get("/api/v1/explanations/{explanation_id}", response_model=Explanation)
async def get_explanation(explanation_id: str):
    """Retrieve a previously generated explanation."""
    if explanation_id not in explanations_cache:
        raise HTTPException(404, "Explanation not found")
    return explanations_cache[explanation_id]


# ============================================================================
# Visualization Endpoints
# ============================================================================

@app.post("/api/v1/visualizations/generate")
async def generate_visualization(request: VisualizationRequest):
    """
    Generate visual content for a concept.

    Types:
    - 2d_graph: Interactive 2D graphs (Desmos-like)
    - 3d_model: 3D models (chemistry molecules, geometry)
    - animation: Animated explanations
    - diagram: Static diagrams with annotations
    """
    viz_id = str(uuid.uuid4())

    # TODO: Connect to lucidia-core visualizers
    return {
        "id": viz_id,
        "type": request.type,
        "concept": request.concept,
        "url": f"/api/v1/visualizations/render/{viz_id}",
        "embed_code": f'<iframe src="https://lucidia.ai/embed/{viz_id}" />',
        "status": "generating",
    }


@app.get("/api/v1/visualizations/render/{viz_id}")
async def render_visualization(viz_id: str):
    """Render a generated visualization."""
    # TODO: Return actual visualization data
    return {
        "id": viz_id,
        "type": "2d_graph",
        "data": {
            "equation": "y = x^2",
            "domain": [-10, 10],
            "range": [-10, 100],
        },
        "interactive": True,
    }


# ============================================================================
# User Context / Memory Endpoints
# ============================================================================

@app.get("/api/v1/users/{user_id}/context", response_model=UserContext)
async def get_user_context(user_id: str):
    """
    Get persistent learning context for a user.

    Lucidia remembers:
    - Learning style preferences
    - Strengths and areas for growth
    - Recent topics studied
    - Progress over time
    """
    if user_id not in user_contexts:
        # Create new context
        user_contexts[user_id] = UserContext(
            user_id=user_id,
            learning_style="visual",
            strengths=[],
            areas_for_growth=[],
            recent_topics=[],
            session_count=1,
            total_problems_solved=0,
        )

    return user_contexts[user_id]


@app.put("/api/v1/users/{user_id}/context")
async def update_user_context(user_id: str, context: UserContext):
    """Update user learning context."""
    user_contexts[user_id] = context
    return {"status": "updated", "user_id": user_id}


@app.post("/api/v1/users/{user_id}/problem-solved")
async def record_problem_solved(user_id: str, subject: str, topic: str, success: bool):
    """Record that a user solved (or attempted) a problem."""
    if user_id not in user_contexts:
        await get_user_context(user_id)

    ctx = user_contexts[user_id]
    ctx.total_problems_solved += 1

    if topic not in ctx.recent_topics:
        ctx.recent_topics.append(topic)
        if len(ctx.recent_topics) > 10:
            ctx.recent_topics.pop(0)

    if success and topic not in ctx.strengths:
        ctx.strengths.append(topic)

    return {"status": "recorded", "total_solved": ctx.total_problems_solved}


# ============================================================================
# Practice / Game Endpoints
# ============================================================================

@app.get("/api/v1/practice/generate")
async def generate_practice_problem(
    subject: str = "math",
    topic: Optional[str] = None,
    difficulty: str = "medium",
    user_id: Optional[str] = None,
):
    """
    Generate a contextual practice problem.

    Problems are presented in real-world scenarios:
    - "4 houses, 4 dogs" for division
    - "Pizza slices" for fractions
    - "Building a treehouse" for geometry
    """
    # Get user context for personalization
    context = None
    if user_id and user_id in user_contexts:
        context = user_contexts[user_id]

    # Select a problem from the bank based on subject and difficulty
    subject_problems = PROBLEM_BANK.get(subject, PROBLEM_BANK["math"])
    difficulty_problems = subject_problems.get(difficulty, subject_problems.get("easy", []))

    # Filter by topic if specified
    if topic:
        topic_filtered = [p for p in difficulty_problems if p["topic"] == topic]
        if topic_filtered:
            difficulty_problems = topic_filtered

    # Pick a random problem from the matching set
    problem_data = random.choice(difficulty_problems)

    problem_id = str(uuid.uuid4())

    # Store the problem with its answer for later checking
    practice_problems[problem_id] = {
        "answer": problem_data["answer"],
        "subject": subject,
        "topic": problem_data["topic"],
        "problem": problem_data["problem"],
        "feedback_correct": problem_data["feedback_correct"],
        "feedback_incorrect": problem_data["feedback_incorrect"],
    }

    return {
        "id": problem_id,
        "subject": subject,
        "topic": problem_data["topic"],
        "difficulty": difficulty,
        "scenario": problem_data["scenario"],
        "problem": problem_data["problem"],
        "hints": problem_data["hints"],
        "visualization_prompt": problem_data["visualization_prompt"],
    }


@app.post("/api/v1/practice/check")
async def check_practice_answer(
    problem_id: str,
    answer: str,
    user_id: Optional[str] = None,
):
    """Check a practice problem answer and provide feedback."""
    if problem_id not in practice_problems:
        raise HTTPException(404, "Problem not found. It may have expired or the ID is invalid.")

    problem = practice_problems[problem_id]
    correct = answer.strip() == problem["answer"]

    # Build the next problem URL using the same subject/topic
    next_url = f"/api/v1/practice/generate?subject={problem['subject']}&topic={problem['topic']}"

    # Record progress if user_id is provided
    if user_id:
        if user_id not in user_contexts:
            await get_user_context(user_id)
        ctx = user_contexts[user_id]
        if correct:
            ctx.total_problems_solved += 1
            if problem["topic"] not in ctx.recent_topics:
                ctx.recent_topics.append(problem["topic"])
                if len(ctx.recent_topics) > 10:
                    ctx.recent_topics.pop(0)

    return {
        "correct": correct,
        "expected_answer": problem["answer"] if not correct else None,
        "feedback": problem["feedback_correct"] if correct else problem["feedback_incorrect"],
        "next_problem": next_url,
    }


# ============================================================================
# Helper Functions
# ============================================================================

def _detect_subject(text: str) -> str:
    """Auto-detect subject from problem text."""
    text_lower = text.lower()

    if any(word in text_lower for word in ["equation", "solve", "x =", "algebra", "factor"]):
        return "algebra"
    if any(word in text_lower for word in ["triangle", "circle", "angle", "area", "perimeter"]):
        return "geometry"
    if any(word in text_lower for word in ["velocity", "force", "mass", "energy", "acceleration"]):
        return "physics"
    if any(word in text_lower for word in ["molecule", "reaction", "element", "compound"]):
        return "chemistry"
    if any(word in text_lower for word in ["cell", "organism", "dna", "evolution"]):
        return "biology"
    if any(word in text_lower for word in ["+", "-", "×", "÷", "divide", "multiply", "add", "subtract"]):
        return "arithmetic"

    return "general"


def _assess_difficulty(text: str) -> str:
    """Assess problem difficulty."""
    # Simple heuristic based on length and keywords
    if len(text) < 50:
        return "easy"
    if any(word in text.lower() for word in ["integral", "derivative", "matrix", "quantum"]):
        return "hard"
    return "medium"


# ============================================================================
# Run
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
