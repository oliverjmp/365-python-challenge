import os
import pytest
from src.secret_manager import SecretManager

def test_secret_manager_default_values():
    # Limpiar variables para probar valores por defecto seguros
    if "DUCKDB_USER" in os.environ:
        del os.environ["DUCKDB_USER"]
    if "DUCKDB_STORAGE_BUCKET" in os.environ:
        del os.environ["DUCKDB_STORAGE_BUCKET"]

    manager = SecretManager()
    config = manager.validar_credenciales()
    
    assert config["user"] == "admin_analitica"
    assert config["bucket"] == "s3://enterprise-data-lake-raw"
    assert len(config["token_generado"]) == 32  # 16 hex bytes = 32 chars
    assert config["status"] == "SECURE_CONFIGURED"

def test_secret_manager_custom_env(monkeypatch):
    monkeypatch.setenv("DUCKDB_USER", "custom_user")
    monkeypatch.setenv("DUCKDB_STORAGE_BUCKET", "azure://my-secure-container")

    manager = SecretManager()
    config = manager.validar_credenciales()
    
    assert config["user"] == "custom_user"
    assert config["bucket"] == "azure://my-secure-container"

def test_secret_manager_invalid_bucket(monkeypatch):
    monkeypatch.setenv("DUCKDB_STORAGE_BUCKET", "ruta_insegura_local")
    manager = SecretManager()
    
    with pytest.raises(ValueError, match="La ruta del Data Lake debe ser un almacenamiento remoto seguro"):
        manager.validar_credenciales()