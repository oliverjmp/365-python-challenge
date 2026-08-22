import pytest
from pydantic import ValidationError
from src.validators import InferencePayload

def test_valid_payload():
    """Valida un payload correcto que cumple con todas las restricciones."""
    data = {
        "model_version": "v1.0.0",
        "features": [1.5, 2.0, 3.1],
        "threshold": 0.7
    }
    payload = InferencePayload(**data)
    assert payload.model_version == "v1.0.0"
    assert len(payload.features) == 3
    assert payload.threshold == 0.7

def test_invalid_empty_features():
    """Valida que se rechace un vector de características vacío."""
    with pytest.raises(ValidationError, match="no puede estar vacío"):
        InferencePayload(model_version="v1.0.0", features=[])

def test_invalid_too_many_features():
    """Valida que se rechace un vector con más de 10 características."""
    with pytest.raises(ValidationError, match="excede el límite máximo"):
        InferencePayload(model_version="v1.0.0", features=[1.0] * 11)

def test_invalid_model_version_format():
    """Valida que la versión del modelo deba comenzar con 'v'."""
    with pytest.raises(ValidationError, match="debe comenzar con el prefijo 'v'"):
        InferencePayload(model_version="1.0.0", features=[1.0, 2.0])

def test_invalid_business_logic_v2():
    """Valida la regla de negocio de modelos v2 que exigen al menos 3 features."""
    with pytest.raises(ValidationError, match="requieren un mínimo de 3 características"):
        InferencePayload(model_version="v2.1.0", features=[1.0, 2.0])

def test_valid_business_logic_v2():
    """Valida que un modelo v2 con 3 o más features pase correctamente."""
    payload = InferencePayload(model_version="v2.0.0", features=[1.0, 2.0, 3.0])
    assert payload.model_version == "v2.0.0"