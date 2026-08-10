import pytest
from src.data_contract import DataContractValidator

def test_valid_data_batch():
    """Valida que un lote de datos conforme al contrato pase sin errores."""
    schema = {
        "id": {"type": int, "nullable": False},
        "name": {"type": str, "nullable": False},
        "score": {"type": float, "nullable": True}
    }
    validator = DataContractValidator(schema)
    
    batch = [
        {"id": 1, "name": "Alice", "score": 95.5},
        {"id": 2, "name": "Bob", "score": None}
    ]
    
    errors = validator.validate_batch(batch)
    assert errors == {}

def test_invalid_data_batch():
    """Valida que se detecten violaciones de tipo y campos obligatorios ausentes."""
    schema = {
        "id": {"type": int, "nullable": False},
        "age": {"type": int, "nullable": False}
    }
    validator = DataContractValidator(schema)
    
    batch = [
        {"id": "not_an_int", "age": 25}, # id con tipo incorrecto
        {"age": None}                    # falta id y age es nulo
    ]
    
    errors = validator.validate_batch(batch)
    
    assert 0 in errors
    assert 1 in errors
    assert len(errors[0]) == 1
    assert len(errors[1]) == 2