import pytest
import pandas as pd
from src.data_contract import DataQualityValidator

def test_validate_procurement_data_success():
    """Valida un lote de datos que cumple perfectamente el contrato."""
    validator = DataQualityValidator()
    valid_df = pd.DataFrame({
        "monto": [1500.50, 200.0, 50.0],
        "estado": ["APROBADO", "PENDIENTE", "RECHAZADO"]
    })
    
    result = validator.validate_procurement_data(valid_df)
    assert result["success"] is True
    assert result["statistics"]["successful_expectations"] == 3

def test_validate_procurement_data_failure():
    """Fuerza la inyección de datos corruptos para probar el rechazo del validador."""
    validator = DataQualityValidator()
    invalid_df = pd.DataFrame({
        "monto": [-100.0, None, 500.0],  # Falla por negativo y nulo
        "estado": ["APROBADO", "FRAUDE", "RECHAZADO"]  # Falla por estado no permitido
    })
    
    result = validator.validate_procurement_data(invalid_df)
    assert result["success"] is False
    assert result["statistics"]["unsuccessful_expectations"] > 0

def test_validate_empty_dataframe():
    """Valida la protección contra estructuras de datos vacías."""
    validator = DataQualityValidator()
    with pytest.raises(ValueError, match="vacío"):
        validator.validate_procurement_data(pd.DataFrame())