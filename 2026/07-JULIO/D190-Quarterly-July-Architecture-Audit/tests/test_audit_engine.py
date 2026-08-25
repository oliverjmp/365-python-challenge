import pytest
import json
from src.audit_engine import QuarterlyArchitectureAuditor

def test_valid_architecture_audit(tmp_path):
    d = tmp_path / "data_lake"
    d.mkdir()
    file_path = d / "architecture_state.json"
    
    valid_data = {
        "quarter": "Q3-2026",
        "phase": "Fase 4",
        "components": [
            {"component_id": "MOD-1", "name": "Modulo 1", "status": "CONFORME", "performance_score": 90.0}
        ]
    }
    file_path.write_text(json.dumps(valid_data), encoding="utf-8")
    
    auditor = QuarterlyArchitectureAuditor(storage_path=str(file_path))
    summary = auditor.audit_architecture()
    
    assert summary["total_components"] == 1
    assert summary["compliance_rate"] == 100.0
    assert summary["status"] == "APROBADO_INTEGRAL"

def test_missing_file_raises_error():
    auditor = QuarterlyArchitectureAuditor(storage_path="ruta/inexistente/file.json")
    with pytest.raises(FileNotFoundError, match="No se encontró el archivo"):
        auditor.load_raw_data()

def test_invalid_schema_validation_raises_error(tmp_path):
    d = tmp_path / "data_lake"
    d.mkdir()
    file_path = d / "architecture_state.json"
    
    invalid_data = {
        "quarter": "Q3-2026",
        "phase": "Fase 4",
        "components": [
            {"component_id": "MOD-1", "name": "Modulo 1", "status": "ESTADO_FALSO", "performance_score": 150.0}
        ]
    }
    file_path.write_text(json.dumps(invalid_data), encoding="utf-8")
    
    auditor = QuarterlyArchitectureAuditor(storage_path=str(file_path))
    with pytest.raises(ValueError, match="Fallo crítico en la validación"):
        auditor.audit_architecture()