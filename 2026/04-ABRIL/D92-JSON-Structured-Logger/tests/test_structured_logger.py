import json
import logging
import pytest
from src.structured_logger import get_structured_logger, set_correlation_id

def test_structured_logger_json_output(capsys):
    """Valida que el logger emita mensajes correctamente estructurados en formato JSON."""
    logger = get_structured_logger("test_json_logger")
    set_correlation_id("corr-xyz-123")
    
    # Creamos un LogRecord simulado o usamos el logger directamente capturando la salida
    # Como usamos StreamHandler hacia sys.stderr por defecto en logging, podemos probar el formateador directamente
    from src.structured_logger import JsonFormatter
    
    record = logging.LogRecord(
        name="test", level=logging.INFO, pathname="", lineno=0,
        msg="Operación ETL completada", args=(), exc_info=None
    )
    record.extra_data = {"rows_processed": 500}
    
    formatter = JsonFormatter()
    formatted_output = formatter.format(record)
    
    parsed_json = json.loads(formatted_output)
    
    assert parsed_json["level"] == "INFO"
    assert parsed_json["message"] == "Operación ETL completada"
    assert parsed_json["correlation_id"] == "corr-xyz-123"
    assert parsed_json["rows_processed"] == 500

def test_logger_without_correlation_id():
    """Valida que el logger funcione correctamente incluso si no se establece un Correlation ID."""
    set_correlation_id(None)
    from src.structured_logger import JsonFormatter
    
    record = logging.LogRecord(
        name="test", level=logging.WARNING, pathname="", lineno=0,
        msg="Advertencia sin contexto", args=(), exc_info=None
    )
    
    formatter = JsonFormatter()
    parsed_json = json.loads(formatter.format(record))
    
    assert "correlation_id" not in parsed_json
    assert parsed_json["message"] == "Advertencia sin contexto"