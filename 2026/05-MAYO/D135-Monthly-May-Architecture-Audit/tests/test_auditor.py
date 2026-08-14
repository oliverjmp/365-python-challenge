import pytest
import os
import json
from src.auditor import ArchitectureAuditor

def test_auditor_verify_artifacts(tmp_path):
    """Valida la detección correcta de archivos existentes y faltantes."""
    valid_file = tmp_path / "model.pkl"
    valid_file.write_text("dummy model content")
    
    relative_valid = "model.pkl"
    relative_missing = "missing_artifact.json"
    
    auditor = ArchitectureAuditor(base_path=str(tmp_path))
    result = auditor.verify_required_artifacts([relative_valid, relative_missing])
    
    assert result["total_checked"] == 2
    assert result["missing_count"] == 1
    assert relative_missing in result["missing_artifacts"]
    assert result["details"][relative_valid] is True
    assert result["details"][relative_missing] is False

def test_generate_audit_report_success(tmp_path):
    """Valida la correcta exportación del reporte de auditoría en formato JSON."""
    auditor = ArchitectureAuditor(base_path=str(tmp_path))
    dummy_data = {"status": "SUCCESS", "score": 100}
    
    report_path = auditor.generate_audit_report(dummy_data, output_filename="report.json")
    
    assert os.path.exists(report_path)
    
    with open(report_path, "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
        
    assert loaded_data["status"] == "SUCCESS"
    assert loaded_data["score"] == 100

def test_generate_audit_report_invalid_data_raises_error(tmp_path):
    """Valida que se lance un ValueError si se intenta auditar datos no estructurados."""
    auditor = ArchitectureAuditor(base_path=str(tmp_path))
    with pytest.raises(ValueError, match="deben ser un diccionario válido"):
        auditor.generate_audit_report("invalid_data_type")