import pytest
from src.audit_engine import AuditEngine

def test_audit_engine_success():
    engine = AuditEngine(max_workers=2)
    report = engine.run_full_audit(total_probes=3)
    
    assert report["total_probes"] == 3
    assert report["passed"] == 3
    assert report["health_score"] == 100.0
    assert len(report["details"]) == 3

def test_audit_engine_invalid_probes():
    engine = AuditEngine()
    with pytest.raises(ValueError, match="El número de pruebas debe ser mayor a cero."):
        engine.run_full_audit(total_probes=0)

def test_export_audit_json():
    engine = AuditEngine()
    sample_data = {"total_probes": 1, "passed": 1, "health_score": 100.0, "details": []}
    json_output = engine.export_audit_json(sample_data)
    
    assert "total_probes" in json_output
    assert "100.0" in json_output