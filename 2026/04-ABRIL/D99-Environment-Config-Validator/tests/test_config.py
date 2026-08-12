import os
import pytest
from pydantic import ValidationError
from src.config import Settings

def test_settings_success_with_env(monkeypatch):
    """Valida la carga correcta de configuraciones mediante variables de entorno."""
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/db")
    monkeypatch.setenv("API_SECRET_KEY", "super-secret-key-123")
    monkeypatch.setenv("MAX_CONNECTIONS", "50")

    settings = Settings()
    assert settings.app_env == "production"
    assert settings.database_url == "postgresql://user:pass@localhost:5432/db"
    assert settings.api_secret_key == "super-secret-key-123"
    assert settings.max_connections == 50

def test_settings_missing_mandatory_fields(monkeypatch):
    """Valida que Pydantic lance un error si faltan campos obligatorios."""
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.delenv("API_SECRET_KEY", raising=False)

    with pytest.raises(ValidationError):
        Settings(_env_file=None)