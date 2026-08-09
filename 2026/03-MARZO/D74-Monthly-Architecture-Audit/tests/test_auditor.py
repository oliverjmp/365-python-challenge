import os
import json
import pytest
from src.auditor import ArchitectureAuditor

def test_auditor_missing_json(tmp_path):
    """Verifica el comportamiento cuando el archivo JSON no existe."""
    fake_path = tmp_path / "non_existent.json"
    auditor = ArchitectureAuditor(str(fake_path))
    result = auditor.audit_modules()
    
    assert result["total"] == 0
    assert result["passed"] == 0

def test_auditor_validates_files(tmp_path):
    """Verifica la correcta auditoría de módulos existentes y faltantes."""
    # Creamos un archivo real temporal y un path falso
    valid_file = tmp_path / "dummy.py"
    valid_file.write_text("# test")
    
    manifest_data = {
        "modules": [
            {"name": "ValidModule", "path": str(valid_file)},
            {"name": "InvalidModule", "path": "ruta/falsa/inexistente.py"}
        ]
    }
    
    json_file = tmp_path / "manifest.json"
    json_file.write_text(json.dumps(manifest_data))
    
    auditor = ArchitectureAuditor(str(json_file))
    result = auditor.audit_modules()
    
    assert result["total"] == 2
    assert result["passed"] == 1
    assert result["failed"] == 1
    assert result["details"][0]["status"] == "OK"
    assert result["details"][1]["status"] == "MISSING"