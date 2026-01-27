# CLAUDE.md - AI Assistant Guidelines for BlackRoad

## Project Overview

**BlackRoad** is a distributed AI reasoning platform featuring specialized agents (Physicist, Mathematician, Chemist, Geologist, etc.) that work together as an integrated ecosystem. It is part of **BlackRoad OS** - "The Road to AI Sovereignty."

- **Organization:** BlackRoad OS, Inc.
- **License:** Proprietary (see LICENSE file)
- **Repository Type:** Monorepo using Turbo with pnpm package manager
- **Core Language:** Python (3.10+) with Node.js tooling for workspace management

## Repository Structure

```
blackroad/
├── packages/
│   └── lucidia-core/           # Main Python package - AI reasoning engines
│       ├── lucidia_core/       # Package module (CLI, API entry points)
│       ├── core/               # Core vector utilities
│       ├── duet/               # Duet coordination system
│       ├── engines/            # Engine implementations
│       ├── intelligence/       # Event system for agent coordination
│       ├── modules/            # Additional modules (random_fields)
│       ├── quantum/            # Quantum computing extensions (QML, kernels)
│       ├── quantum_engine/     # Quantum engine (archetypal geometry, backends)
│       ├── reflex/             # System reflexes (GPIO, wallet, logging)
│       ├── rituals/            # Activation rituals and generation scripts
│       ├── codex*.yaml         # Agent seed configuration files
│       └── [agent].py          # Agent implementations
├── integrations/               # Integration examples (mobile, etc.)
├── .trinity/                   # Light Trinity System (brand, infra, events)
│   ├── redlight/               # Template & brand system
│   ├── greenlight/             # Project coordination & event logging
│   ├── yellowlight/            # Infrastructure automation
│   └── system/                 # Trinity compliance checking
├── .github/workflows/          # CI/CD workflows (12 total)
└── Documentation files
```

## Agent System Architecture

### Agent Files (packages/lucidia-core/)

Each specialized agent follows a consistent pattern:

| Agent | File | Purpose |
|-------|------|---------|
| Physicist | `physicist.py` | Energy modeling, feedback systems, physical laws |
| Mathematician | `mathematician.py` | Symbolic computation, proofs, mathematical analysis |
| Chemist | `chemist.py` | Molecular analysis, reactions, chemical processes |
| Geologist | `geologist.py` | Terrain modeling, resource mapping, stratigraphy |
| Engineer | `engineer.py` | Structural analysis, optimization |
| Analyst | `analyst.py` | Data analysis, pattern recognition |
| Painter | `painter.py` | Visual generation, graphics |
| Architect | `architect.py` | System design, blueprints |
| Poet | `poet.py` | Creative text, lyrical composition |
| Speaker | `speaker.py` | NLP, communication |
| Navigator | `navigator.py` | Pathfinding, route optimization |
| Researcher | `researcher.py` | Research synthesis, literature review |
| Mediator | `mediator.py` | Coordination, conflict resolution |
| Builder | `builder.py` | Build systems, construction planning |
| Guardian | `guardian.py` | Security, protection protocols |
| Origin | `origin.py` | Core Lucidia origin system |

### Agent Configuration Pattern

Agents are configured via YAML seed files (`codex*.yaml`):

```yaml
id: codex-21
system_charter:
  agent_name: "Codex-21 Physicist"
  generation: 6
  domain: [energy, forces, dynamics, field theory]
  moral_constant: "Power = Responsibility in motion"
  core_principle: "Equations are stories about balance"
purpose: |
  To understand the rules behind motion...
directives:
  - Measure before moving.
  - Never separate beauty from accuracy.
jobs:
  - Model energy flows through hardware and neural networks.
behavioral_loop:
  - observe
  - model
  - test
  - refine
```

### Agent Code Structure

```python
@dataclass
class AgentSeed:
    """Structured representation loaded from YAML."""
    identifier: str
    agent_name: str
    domain: List[str]
    directives: List[str]
    # ... etc

@dataclass
class AgentState:
    """Runtime state persisted between runs."""
    # Agent-specific state fields

    def load(cls, path: Path) -> AgentState: ...
    def save(self, path: Path) -> None: ...

def load_seed(path: Path) -> AgentSeed:
    """Load and validate seed YAML file."""
    ...

def main() -> None:
    """CLI entry point for the agent."""
    ...
```

## Development Setup

### Prerequisites

- Python 3.10+ (3.10, 3.11, 3.12 supported)
- Node.js 20+
- pnpm 9.0.0+

### Installation

```bash
# Clone repository
git clone https://github.com/BlackRoad-OS/blackroad.git
cd blackroad

# Install Node dependencies (workspace management)
pnpm install

# Install Python package in development mode
cd packages/lucidia-core
pip install -e ".[dev]"
```

### Running

```bash
# Turbo commands (from root)
pnpm dev          # Run all packages in dev mode
pnpm build        # Build all packages
pnpm lint         # Lint all packages

# Lucidia CLI
lucidia list      # List available agents
lucidia run physicist --query "energy model"
lucidia api       # Start FastAPI server

# Direct Python execution
python packages/lucidia-core/__main__.py  # Interactive REPL
lucidia-api       # Start API server (entry point)

# Flask app (if using Flask optional dependency)
python -m lucidia_core.app
```

### API Server

```bash
# Start API on default port 8000
lucidia api

# Custom host/port
lucidia api --host 127.0.0.1 --port 3000
```

## Code Conventions

### Python Style

- **Formatter:** Black (line length 100)
- **Linter:** Ruff (E, F, I, N, W rules)
- **Type Checker:** mypy (Python 3.10 target)
- **Line Length:** 100 characters

```bash
# Format code
black packages/lucidia-core

# Lint
ruff check packages/lucidia-core

# Type check
mypy packages/lucidia-core
```

### Code Patterns

1. **Type Hints:** Use throughout, with `from __future__ import annotations`
2. **Dataclasses:** Preferred for structured data
3. **Pathlib:** Use `Path` for all file operations
4. **JSON/YAML:** For configuration and state persistence
5. **Docstrings:** Doctest format with Parameters, Returns, Raises sections

### File Naming

- **Agent files:** Lowercase domain name (`physicist.py`, `mathematician.py`)
- **Config files:** `codex{N}.yaml` for agent seeds
- **State files:** `state.json` for persistent state
- **Log files:** JSONL format (`.jsonl`) for streaming data

### State Persistence

Agents persist state to JSON files and logs to JSONL:

```python
STATE_FILENAME = "state.json"
ENERGY_LOG_NAME = "energy_flow.jsonl"
DEFAULT_STATE_ROOT = Path("/srv/lucidia/physicist")
```

## Testing

### Running Tests

```bash
cd packages/lucidia-core

# Run all tests
pytest

# With coverage
pytest --cov=lucidia_core

# Specific test file
pytest quantum_engine/tests/test_archetypal_geometry.py
```

### Test Locations

- `packages/lucidia-core/quantum_engine/tests/`
- `packages/lucidia-core/quantum/tests/`

### Test Conventions

- Use pytest conventions (`test_*` functions)
- Test mathematical properties and invariants
- Validate coherence and geometric properties

## CI/CD Workflows

Located in `.github/workflows/`:

| Workflow | Purpose |
|----------|---------|
| `ci.yml` | Main CI (lint, test, build) |
| `auto-deploy.yml` | Multi-platform deployment |
| `security-scan.yml` | Security scanning |
| `blackroad-codeql-analysis.yml` | CodeQL security analysis |
| `trinity-compliance.yml` | Light Trinity compliance |
| `auto-label.yml` | Automatic issue labeling |
| `auto-merge.yml` | Automated PR merging |
| `stale-issues.yml` | Stale issue management |

### CI Pipeline

The main CI runs on push/PR to main, master, develop:
1. Setup Node.js 20 and Python 3.11
2. Install dependencies
3. Lint
4. Type check
5. Test
6. Build
7. Upload artifacts

## Brand Standards

### Traffic Light Status System

| Light | Meaning | Production Safe? |
|-------|---------|------------------|
| 🟢 GREEN | Production Ready | Yes |
| 🟡 YELLOW | Proceed with Caution | Maybe |
| 🔴 RED | Do Not Use | No |
| 🔵 BLUE | Archived/Deprecated | No |

### Emoji Usage

Use official BlackRoad emoji dictionary (see `BLACKROAD_EMOJI_DICTIONARY.md`):

- 🖤 BlackRoad Brand
- 💖 Hot Pink (primary color)
- 💙 Electric Blue (info)
- 💜 Violet (creative)
- 🧡 Amber (warning)
- ✅ Success/Complete
- ❌ Failure/Error
- ⚠️ Warning
- 🚀 Deploy/Launch

### Brand Colors

- **Hot Pink:** #FF1D6C (primary)
- **Amber:** Warning color
- **Electric Blue:** Info color
- **Violet:** Creative color

## Key Modules

### Quantum Systems

- `quantum_engine/archetypal_geometry.py` - Platonic solids, quantum fields, Sophia equation
- `quantum/qnn.py` - Quantum neural networks
- `quantum/torch_bridge.py` - PyTorch integration

### Coordination Systems

- `harmony.py` - Multi-node coordination with ledger
- `duet/` - Duet coordination system
- `foundation_system.py` - Distributed memory palace

### Entry Points

- `lucidia_core/cli.py` - CLI (`lucidia` command)
- `lucidia_core/api.py` - FastAPI server (`lucidia-api` command)
- `__main__.py` - Interactive REPL with Harmony coordinator

## Environment Configuration

See `.env.example` for required environment variables:

- Deployment platforms (Railway, Vercel, Cloudflare)
- Container registries (Docker Hub, GHCR)
- AI APIs (OpenAI, Anthropic, Groq)
- Database (Turso)
- Authentication (Clerk)
- Payments (Stripe)

## Working with This Codebase

### When Adding a New Agent

1. Create `codex{N}.yaml` with agent charter and configuration
2. Create `{agent_name}.py` following the dataclass pattern
3. Add to CLI list in `lucidia_core/cli.py`
4. Add tests in appropriate test directory

### When Modifying Agent Behavior

1. Check the corresponding `codex*.yaml` for charter/directives
2. Maintain state persistence patterns
3. Keep behavioral loop intact (observe → model → test → refine)
4. Preserve type hints and docstrings

### When Working on Quantum Modules

1. Tests validate mathematical properties
2. Maintain coherence checks
3. Use NumPy for numerical operations
4. SymPy for symbolic mathematics

## Important Files Reference

| File | Purpose |
|------|---------|
| `packages/lucidia-core/pyproject.toml` | Python package config |
| `package.json` | Root workspace config |
| `.github/workflows/ci.yml` | Main CI pipeline |
| `BLACKROAD_EMOJI_DICTIONARY.md` | Official emoji standards |
| `TRAFFIC_LIGHT_SYSTEM.md` | Status indicator system |
| `.env.example` | Environment variables template |

## Dependencies

### Core Python Dependencies

- `fastapi>=0.100.0` - REST API framework
- `uvicorn>=0.23.0` - ASGI server
- `pydantic>=2.0.0` - Data validation
- `pyyaml>=6.0` - YAML parsing
- `sympy>=1.12` - Symbolic mathematics
- `mpmath>=1.3.0` - Arbitrary precision math
- `numpy>=1.24.0` - Numerical computing

### Development Dependencies

- `pytest>=7.0.0` - Testing
- `pytest-cov>=4.0.0` - Coverage
- `black>=23.0.0` - Formatting
- `ruff>=0.1.0` - Linting
- `mypy>=1.0.0` - Type checking
- `httpx>=0.24.0` - HTTP testing

## Common Tasks

```bash
# Format all Python code
black packages/lucidia-core

# Run linter
ruff check packages/lucidia-core --fix

# Type check
mypy packages/lucidia-core

# Run tests with coverage
pytest packages/lucidia-core --cov

# Start development API server
cd packages/lucidia-core && uvicorn lucidia_core.api:app --reload

# List all agents
lucidia list
```
