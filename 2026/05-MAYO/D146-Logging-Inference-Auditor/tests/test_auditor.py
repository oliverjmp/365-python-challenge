import json
import pytest
from src.auditor import InferenceAuditor, JSONFormatter

def test_json_formatter():
    """Valida que el formateador JSON serialice correctamente un LogRecord."""
    import logging
    formatter = JSONFormatter()
    record = logging.LogRecord(
        name="TestLogger", level=logging.INFO, pathname="", lineno=0,
        msg="Mensaje de prueba", args=(), exc_info=None
    )
    record.audit_data = {"request_id": "123", "success": True}
    
    formatted = formatter.format(record)
    data = json.loads(formatted)
    
    assert data["message"] == "Mensaje de prueba"
    assert data["request_id"] == "123"
    assert data["success"] is True

def test_invalid_arguments_raise_error():
    """Valida que un request_id o model_version vacíos lancen un ValueError."""
    auditor = InferenceAuditor()
    with pytest.raises(ValueError, match="son obligatorios"):
        auditor.audit_inference("", "v1.0", [1.0], lambda: 1)

def test_successful_inference_audit(capsys):
    """Valida el registro exitoso de una inferencia auditada."""
    auditor = InferenceAuditor(logger_name="TestAuditorSuccess")
    
    def mock_infer():
        return [0.95]

    res = auditor.audit_inference(
        request_id="req-001",
        model_version="v1.0.0",
        features=[1.5, 2.0],
        inference_func=mock_infer
    )

    assert res == [0.95]
    
    captured = capsys.readouterr()
    log_data = json.loads(captured.out.strip())
    
    assert log_data["request_id"] == "req-001"
    assert log_data["model_version"] == "v1.0.0"
    assert log_data["success"] is True
    assert log_data["prediction"] == [0.95]
    assert log_data["latency_ms"] >= 0.0

def test_failed_inference_audit(capsys):
    """Valida que el auditor registre correctamente los fallos de inferencia."""
    auditor = InferenceAuditor(logger_name="TestAuditorError")
    
    def mock_failing_infer():
        raise RuntimeError("Modelo no disponible")

    with pytest.raises(RuntimeError, match="Modelo no disponible"):
        auditor.audit_inference(
            request_id="req-002",
            model_version="v1.0.0",
            features=[1.0],
            inference_func=mock_failing_infer
        )

    captured = capsys.readouterr()
    log_data = json.loads(captured.out.strip())
    
    assert log_data["request_id"] == "req-002"
    assert log_data["success"] is False
    assert log_data["error"] == "Modelo no disponible"
    assert log_data["level"] == "ERROR"