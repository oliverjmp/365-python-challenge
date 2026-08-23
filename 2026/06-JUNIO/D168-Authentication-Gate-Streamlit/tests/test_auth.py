import os
import pytest
from src.auth_manager import load_config, init_authenticator

def test_auth_pipeline():
    config_path = "config.yaml"
    assert os.path.exists(config_path)
    
    config = load_config(config_path)
    assert "credentials" in config
    assert "cookie" in config
    
    authenticator = init_authenticator(config)
    assert authenticator is not None

def test_load_config_exception():
    # Forzamos una excepción al intentar cargar un archivo inexistente
    with pytest.raises(FileNotFoundError):
        load_config("archivo_config_falso.yaml")