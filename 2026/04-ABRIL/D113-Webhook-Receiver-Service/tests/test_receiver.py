import hmac
import hashlib
from fastapi.testclient import TestClient
from src.receiver import app, WEBHOOK_SECRET

client = TestClient(app)

def generate_signature(body: bytes) -> str:
    mac = hmac.new(WEBHOOK_SECRET, msg=body, digestmod=hashlib.sha256)
    return f"sha256={mac.hexdigest()}"

def test_webhook_success():
    payload = {
        "event": "payment.completed",
        "timestamp": "2026-04-14T12:00:00Z",
        "data": {"transaction_id": "tx_999888", "amount": 150.00}
    }
    
    import json
    body_bytes = json.dumps(payload).encode("utf-8")
    signature = generate_signature(body_bytes)
    
    response = client.post(
        "/webhook",
        content=body_bytes,
        headers={"X-Hub-Signature-256": signature, "Content-Type": "application/json"}
    )
    
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["processed"] is True

def test_webhook_invalid_signature():
    payload = {"event": "hack.attempt", "timestamp": "now", "data": {}}
    import json
    body_bytes = json.dumps(payload).encode("utf-8")
    
    response = client.post(
        "/webhook",
        content=body_bytes,
        headers={"X-Hub-Signature-256": "sha256=firmafalsa123456", "Content-Type": "application/json"}
    )
    
    assert response.status_code == 401
    assert "Firma HMAC inválida" in response.json()["detail"]

def test_webhook_missing_signature():
    response = client.post(
        "/webhook",
        json={"event": "test"}
    )
    
    assert response.status_code == 401
    assert "Firma HMAC inválida" in response.json()["detail"]