import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.receiver import app, SECRET_KEY
from src.dispatcher import WebhookDispatcher
import json

client = TestClient(app)
SECRET_STR = SECRET_KEY.decode('utf-8')

def test_valid_webhook_signature():
    """Valida que un webhook con firma correcta sea procesado con éxito."""
    dispatcher = WebhookDispatcher(SECRET_STR)
    payload = {"event": "user.created", "data": {"id": 101, "name": "Oliver"}}
    
    signature = dispatcher.generate_signature(payload)
    headers = {
        "Content-Type": "application/json",
        "X-Webhook-Signature": signature
    }
    
    body_string = json.dumps(payload, separators=(',', ':'), sort_keys=True)
    # Usamos content en lugar de data para seguir las mejores prácticas de httpx
    response = client.post("/webhook", content=body_string, headers=headers)
    
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_missing_signature():
    """Valida que se rechace la petición si falta el encabezado de firma."""
    payload = {"event": "user.created", "data": {"id": 102}}
    response = client.post("/webhook", json=payload)
    assert response.status_code == 401
    assert response.json()["detail"] == "Firma de webhook faltante"

def test_invalid_signature():
    """Valida que se rechace la petición si la firma es incorrecta o fue manipulada."""
    payload = {"event": "user.created", "data": {"id": 103}}
    headers = {"X-Webhook-Signature": "firma_falsa_invalida_12345"}
    
    response = client.post("/webhook", json=payload, headers=headers)
    assert response.status_code == 403
    assert response.json()["detail"] == "Firma criptográfica inválida"

def test_dispatcher_send_webhook_mocked():
    """Valida que el emisor ejecute la petición HTTP de envío firmando correctamente."""
    dispatcher = WebhookDispatcher(SECRET_STR)
    
    with patch("src.dispatcher.requests.post") as mock_post:
        mock_post.return_value.status_code = 200
        
        response = dispatcher.send_webhook("http://localhost:8000/webhook", "test.event", {"id": 1})
        
        assert response.status_code == 200
        mock_post.assert_called_once()
        called_headers = mock_post.call_args[1]["headers"]
        assert "X-Webhook-Signature" in called_headers