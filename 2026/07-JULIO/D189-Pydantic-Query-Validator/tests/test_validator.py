import pytest
from pydantic import ValidationError
from src.query_validator import AnalyticsQuerySchema, SQLSanitizer

def test_valid_analytics_payload():
    """Valida un payload correcto que cumple con todas las restricciones y sanitización."""
    data = {
        "metric": "active_users",
        "start_date": "2026-01-01",
        "end_date": "2026-03-31",
        "filters": ["region_us", "tier_premium"],
        "limit": 50
    }
    query = AnalyticsQuerySchema(**data)
    assert query.metric == "active_users"
    assert query.limit == 50
    assert len(query.filters) == 2

def test_sql_injection_detection_metric():
    """Valida que se bloqueen e identifiquen intentos de inyección SQL en la métrica."""
    malicious_data = {
        "metric": "users; DROP TABLE users; --",
        "start_date": "2026-01-01",
        "end_date": "2026-03-31"
    }
    with pytest.raises(ValidationError, match="Intento de inyección SQL"):
        AnalyticsQuerySchema(**malicious_data)

def test_sql_injection_detection_filters():
    """Valida que se detecten patrones de tautología (OR 1=1) dentro de los filtros."""
    malicious_data = {
        "metric": "sales",
        "start_date": "2026-01-01",
        "end_date": "2026-03-31",
        "filters": ["country = 'ES' OR 1=1"]
    }
    with pytest.raises(ValidationError, match="Intento de inyección SQL"):
        AnalyticsQuerySchema(**malicious_data)

def test_invalid_date_format():
    """Valida que un formato de fecha incorrecto active la restricción de expresión regular."""
    invalid_data = {
        "metric": "revenue",
        "start_date": "01/01/2026",
        "end_date": "2026-03-31"
    }
    with pytest.raises(ValidationError):
        AnalyticsQuerySchema(**invalid_data)

def test_sql_sanitizer_non_string_bypass():
    """Valida que el sanitizador gestione de forma segura tipos de datos que no sean cadenas."""
    assert SQLSanitizer.clean(999) == 999

def test_sanitize_inputs_other_types():
    """Valida que el field_validator maneje de forma segura tipos que no sean string ni list (cobertura del else)."""
    from src.query_validator import AnalyticsQuerySchema
    
    # Pasamos un límite como entero directo y una métrica simulada si permitiera otro tipo, 
    # o probamos directamente la función de clase del validador con un entero o diccionario.
    result = AnalyticsQuerySchema.sanitize_inputs(12345)
    assert result == 12345