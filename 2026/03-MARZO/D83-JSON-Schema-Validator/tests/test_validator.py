import pytest
from src.schemas import USER_EVENT_SCHEMA
from src.validator import DataContractValidator

def test_valid_payload():
    """Valida que una carga útil que cumple completamente el esquema pase la validación."""
    validator = DataContractValidator(USER_EVENT_SCHEMA)
    payload = {
        "event_id": "evt-001",
        "username": "Oliver",
        "age": 30,
        "email": "oliver@example.com"
    }
    is_valid, message = validator.validate_payload(payload)
    assert is_valid is True
    assert message == "Validación exitosa"

def test_invalid_type_payload():
    """Valida que se rechace una carga si un campo tiene un tipo de dato incorrecto."""
    validator = DataContractValidator(USER_EVENT_SCHEMA)
    payload = {
        "event_id": "evt-002",
        "username": "Oliver",
        "age": "treinta",  # Debería ser integer
        "email": "oliver@example.com"
    }
    is_valid, message = validator.validate_payload(payload)
    assert is_valid is False
    assert "is not of type 'integer'" in message

def test_missing_required_field():
    """Valida que se rechace la carga si falta un campo obligatorio."""
    validator = DataContractValidator(USER_EVENT_SCHEMA)
    payload = {
        "event_id": "evt-003",
        "username": "Oliver",
        # Falta 'age' y 'email'
    }
    is_valid, message = validator.validate_payload(payload)
    assert is_valid is False
    assert "is a required property" in message

def test_additional_properties_not_allowed():
    """Valida que se rechace la carga si incluye propiedades adicionales no permitidas."""
    validator = DataContractValidator(USER_EVENT_SCHEMA)
    payload = {
        "event_id": "evt-004",
        "username": "Oliver",
        "age": 25,
        "email": "oliver@example.com",
        "role": "admin"  # Propiedad extra no definida en el esquema
    }
    is_valid, message = validator.validate_payload(payload)
    assert is_valid is False
    assert "Additional properties are not allowed" in message