import pytest
import responses
from src.webhook_client import trigger_webhook

@responses.activate
def test_trigger_webhook_success():
    url = "https://api.test.com/webhook"
    responses.add(
        responses.POST,
        url,
        json={"status": "received"},
        status=200
    )

    result = trigger_webhook(url, {"test": True})
    assert result["success"] is True
    assert result["status_code"] == 200
    assert result["response"] == {"status": "received"}

@responses.activate
def test_trigger_webhook_http_error():
    url = "https://api.test.com/webhook"
    responses.add(
        responses.POST,
        url,
        body="Internal Server Error",
        status=500
    )

    result = trigger_webhook(url, {"test": True})
    assert result["success"] is False
    assert result["status_code"] == 500

def test_trigger_webhook_invalid_url():
    result = trigger_webhook("", {"test": True})
    assert result["success"] is False
    assert result["status_code"] == 0

import requests

@responses.activate
def test_trigger_webhook_connection_error():
    url = "https://api.test.com/webhook"
    # Simular un error de conexión de red utilizando responses
    responses.add(
        responses.POST,
        url,
        body=requests.exceptions.ConnectionError("Error de red simulado")
    )

    result = trigger_webhook(url, {"test": True})
    assert result["success"] is False
    assert result["status_code"] == 500
    assert "Error de red simulado" in result["response"]