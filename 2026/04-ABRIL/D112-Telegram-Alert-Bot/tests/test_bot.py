import pytest
from src.bot import TelegramAlertBot

@pytest.fixture
def alert_bot():
    return TelegramAlertBot("TEST_TOKEN_123", "123456789")

def test_bot_initialization(alert_bot):
    assert alert_bot.token == "TEST_TOKEN_123"
    assert alert_bot.chat_id == "123456789"
    assert "TEST_TOKEN_123" in alert_bot.base_url

def test_send_alert_success(alert_bot, monkeypatch):
    class MockResponse:
        status_code = 200
        def json(self):
            return {"ok": True}

    monkeypatch.setattr("requests.post", lambda url, json, timeout: MockResponse())
    
    result = alert_bot.send_alert("🚨 *Alerta Crítica:* Fallo en pipeline ETL de ventas.")
    assert result is True

def test_send_alert_api_error(alert_bot, monkeypatch):
    class MockResponse:
        status_code = 400
        def json(self):
            return {"ok": False}

    monkeypatch.setattr("requests.post", lambda url, json, timeout: MockResponse())
    
    result = alert_bot.send_alert("Mensaje de prueba")
    assert result is False

def test_send_alert_request_exception(alert_bot, monkeypatch):
    import requests
    def mock_post(*args, **kwargs):
        raise requests.RequestException("Error de red simulado")

    monkeypatch.setattr("requests.post", mock_post)
    
    result = alert_bot.send_alert("Mensaje con fallo de red")
    assert result is False