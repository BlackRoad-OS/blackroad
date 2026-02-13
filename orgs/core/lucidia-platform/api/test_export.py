"""Tests for the user data export endpoint on Lucidia platform."""

from fastapi.testclient import TestClient
from main import app, user_contexts, UserContext


client = TestClient(app)


def _clear():
    user_contexts.clear()


def test_export_new_user():
    """Exporting for a user with no context returns null learning_context."""
    _clear()
    resp = client.get("/api/v1/users/unknown-user/export")
    assert resp.status_code == 200
    data = resp.json()

    assert data["export_version"] == "1.0"
    assert data["platform"] == "lucidia"
    assert data["user_id"] == "unknown-user"
    assert data["learning_context"] is None


def test_export_existing_user():
    """Exporting for a user with context returns their learning data."""
    _clear()
    user_contexts["user-123"] = UserContext(
        user_id="user-123",
        learning_style="visual",
        strengths=["algebra"],
        areas_for_growth=["geometry"],
        recent_topics=["equations"],
        session_count=5,
        total_problems_solved=42,
    )

    resp = client.get("/api/v1/users/user-123/export")
    assert resp.status_code == 200
    data = resp.json()

    ctx = data["learning_context"]
    assert ctx["user_id"] == "user-123"
    assert ctx["learning_style"] == "visual"
    assert ctx["strengths"] == ["algebra"]
    assert ctx["total_problems_solved"] == 42
