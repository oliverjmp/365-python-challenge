import pytest
from src.model_service import ModelInferenceService

def test_service_prediction_success():
    """Valida que el servicio devuelva una predicción válida con datos correctos."""
    service = ModelInferenceService()
    # Nuestro modelo dummy de prueba usa 4 características
    result = service.predict([0.1, 0.2, 0.3, 0.4])
    
    assert "prediction" in result
    assert "probability" in result
    assert isinstance(result["prediction"], int)

def test_service_prediction_empty_features():
    """Valida que se lance un error si se envían características vacías."""
    service = ModelInferenceService()
    with pytest.raises(ValueError, match="no puede estar vacío"):
        service.predict([])

def test_service_model_not_found():
    """Valida que se lance FileNotFoundError si la ruta del modelo es incorrecta."""
    with pytest.raises(FileNotFoundError):
        ModelInferenceService(model_path="ruta/falsa/modelo.joblib")