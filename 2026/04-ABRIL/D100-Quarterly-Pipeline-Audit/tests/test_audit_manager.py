import json
import pytest
from src.audit_manager import QuarterlyPipelineAudit

def test_load_metrics_success(tmp_path):
    """Valida la carga correcta de un archivo JSON válido."""
    sample_data = {
        "quarter": "Q1-Test",
        "pipelines": [{"id": "P1", "status": "SUCCESS"}]
    }
    file_path = tmp_path / "metrics.json"
    file_path.write_text(json.dumps(sample_data), encoding="utf-8")

    auditor = QuarterlyPipelineAudit(metrics_file_path=str(file_path))
    data = auditor.load_metrics()
    
    assert data["quarter"] == "Q1-Test"
    assert len(data["pipelines"]) == 1

def test_load_metrics_file_not_found():
    """Valida el manejo seguro cuando el archivo JSON no existe."""
    auditor = QuarterlyPipelineAudit(metrics_file_path="nonexistent_file.json")
    data = auditor.load_metrics()
    assert data == {}

def test_load_metrics_invalid_json(tmp_path):
    """Valida el manejo de excepciones ante un archivo JSON malformado."""
    file_path = tmp_path / "bad.json"
    file_path.write_text("{ invalid json syntax }", encoding="utf-8")

    auditor = QuarterlyPipelineAudit(metrics_file_path=str(file_path))
    data = auditor.load_metrics()
    assert data == {}

def test_generate_health_report(tmp_path):
    """Valida el cálculo correcto de métricas, tasas de éxito y estado de salud."""
    sample_data = {
        "quarter": "Q1-2026",
        "pipelines": [
            {"id": "1", "status": "SUCCESS"},
            {"id": "2", "status": "SUCCESS"},
            {"id": "3", "status": "FAILED"},
            {"id": "4", "status": "WARNING"}
        ]
    }
    file_path = tmp_path / "metrics.json"
    file_path.write_text(json.dumps(sample_data), encoding="utf-8")

    auditor = QuarterlyPipelineAudit(metrics_file_path=str(file_path))
    report = auditor.generate_health_report()

    assert report["total_pipelines"] == 4
    assert report["success_count"] == 2
    assert report["failed_count"] == 1
    assert report["warning_count"] == 1
    assert report["success_rate_percent"] == 50.0
    assert report["health_status"] == "CRITICAL"

def test_generate_health_report_empty(tmp_path):
    """Valida el comportamiento del reporte con un conjunto de datos vacío."""
    sample_data = {"quarter": "Q1", "pipelines": []}
    file_path = tmp_path / "empty.json"
    file_path.write_text(json.dumps(sample_data), encoding="utf-8")

    auditor = QuarterlyPipelineAudit(metrics_file_path=str(file_path))
    report = auditor.generate_health_report()
    assert report["status"] == "EMPTY"
    assert report["total"] == 0