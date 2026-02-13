"""Tests for the user data export endpoint."""

from fastapi.testclient import TestClient
from main import app, users_db, conversations_db, agents_db, blockchain_db


client = TestClient(app)


def _register_user(email="test@blackroad.io", password="testpass123", name="Test User"):
    """Register a user and return the access token and user id."""
    users_db.clear()
    conversations_db.clear()
    agents_db.clear()
    blockchain_db["transactions"].clear()
    blockchain_db["blocks"].clear()

    resp = client.post("/api/auth/register", json={
        "email": email,
        "password": password,
        "name": name,
    })
    data = resp.json()
    return data["access_token"], data["user"]["id"]


def test_export_requires_auth():
    resp = client.get("/api/user/export")
    assert resp.status_code == 401


def test_export_returns_user_profile():
    token, user_id = _register_user()
    resp = client.get("/api/user/export", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    data = resp.json()

    assert data["export_version"] == "1.0"
    assert data["exported_at"] is not None
    assert data["user"]["id"] == user_id
    assert data["user"]["email"] == "test@blackroad.io"
    assert data["user"]["name"] == "Test User"
    assert "password" not in data["user"]
    assert "password_hash" not in data["user"]


def test_export_includes_conversations():
    token, _ = _register_user()

    # Create a conversation
    client.post(
        "/api/ai-chat/chat",
        json={"message": "Hello from export test"},
        headers={"Authorization": f"Bearer {token}"},
    )

    resp = client.get("/api/user/export", headers={"Authorization": f"Bearer {token}"})
    data = resp.json()

    assert len(data["conversations"]) == 1
    assert data["conversations"][0]["messages"][0]["content"] == "Hello from export test"


def test_export_includes_agents():
    token, _ = _register_user()

    # Spawn an agent
    client.post(
        "/api/agents/spawn",
        json={"role": "tester", "capabilities": ["testing"]},
        headers={"Authorization": f"Bearer {token}"},
    )

    resp = client.get("/api/user/export", headers={"Authorization": f"Bearer {token}"})
    data = resp.json()

    assert len(data["agents"]) == 1
    assert data["agents"][0]["role"] == "tester"


def test_export_includes_transactions():
    token, _ = _register_user()

    # Create a transaction
    client.post(
        "/api/blockchain/transaction",
        json={"from_address": "addr1", "to_address": "addr2", "amount": 10.0},
        headers={"Authorization": f"Bearer {token}"},
    )

    resp = client.get("/api/user/export", headers={"Authorization": f"Bearer {token}"})
    data = resp.json()

    assert len(data["transactions"]) == 1
    assert data["transactions"][0]["amount"] == 10.0


def test_export_content_disposition_header():
    token, user_id = _register_user()
    resp = client.get("/api/user/export", headers={"Authorization": f"Bearer {token}"})
    assert f"blackroad-export-{user_id}.json" in resp.headers.get("content-disposition", "")
