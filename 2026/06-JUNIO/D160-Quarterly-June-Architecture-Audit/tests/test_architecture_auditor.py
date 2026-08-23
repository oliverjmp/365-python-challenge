import pytest
import os
import json
from src.architecture_auditor import ArchitectureAuditor

def test_invalid_registry_path_raises_error():
    """Valida que una ruta de registro sin extensión .json lance un ValueError."""
    with pytest.raises(ValueError, match="archivo JSON válido"):
        ArchitectureAuditor("registro.txt")

def test_empty_registry_path_raises_error():
    """Valida que una ruta vacía lance un ValueError."""
    with pytest.raises(ValueError, match="archivo JSON válido"):
        ArchitectureAuditor("")

def test_load_registry_file_not_found(tmp_path):
    """Valida que intentar cargar un archivo JSON inexistente lance FileNotFoundError."""
    auditor = ArchitectureAuditor(str(tmp_path / "no_existe.json"))
    with pytest.raises(FileNotFoundError, match="No se encontró el archivo de registro"):
        auditor.load_registry_data()

def test_load_registry_invalid_json_syntax(tmp_path):
    """Valida que un archivo JSON mal formado lance un ValueError."""
    bad_json_file = tmp_path / "bad.json"
    bad_json_file.write_text("{ formato invalido json", encoding="utf-8")
    
    auditor = ArchitectureAuditor(str(bad_json_file))
    with pytest.raises(ValueError, match="Error de sintaxis en el archivo JSON"):
        auditor.load_registry_data()

def test_load_registry_invalid_root_type(tmp_path):
    """Valida que si el JSON raíz no es un diccionario lance un ValueError."""
    list_json_file = tmp_path / "list.json"
    list_json_file.write_text("[1, 2, 3]", encoding="utf-8")
    
    auditor = ArchitectureAuditor(str(list_json_file))
    with pytest.raises(ValueError, match="debe ser un diccionario raíz"):
        auditor.load_registry_data()

def test_audit_component_performance_empty_list():
    """Valida que pasar una lista vacía de componentes lance un ValueError."""
    auditor = ArchitectureAuditor("dummy.json")
    with pytest.raises(ValueError, match="no puede estar vacía"):
        auditor.audit_component_performance([])

def test_audit_component_invalid_coverage_raises_error():
    """Valida que un porcentaje de cobertura fuera del rango [0, 100] lance un ValueError."""
    auditor = ArchitectureAuditor("dummy.json")
    components = [{"name": "D157", "coverage_percentage": 105.0, "status": "active"}]
    with pytest.raises(ValueError, match="porcentaje de cobertura inválido"):
        auditor.audit_component_performance(components)

def test_generate_report_invalid_path_raises_error(tmp_path):
    """Valida que una ruta de informe de salida inválida lance un ValueError."""
    auditor = ArchitectureAuditor(str(tmp_path / "reg.json"))
    with pytest.raises(ValueError, match="archivo JSON válido"):
        auditor.generate_report([], "reporte.txt")

def test_architecture_auditor_full_success(tmp_path):
    """Valida el ciclo completo de carga de registro, auditoría de rendimiento y generación de informe."""
    registry_file = tmp_path / "registry.json"
    report_file = tmp_path / "audit_report.json"

    registry_data = {
        "milestones": [
            {"name": "D157", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D158", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D159", "coverage_percentage": 98.0, "status": "active"}
        ]
    }
    registry_file.write_text(json.dumps(registry_data), encoding="utf-8")

    auditor = ArchitectureAuditor(str(registry_file))
    loaded = auditor.load_registry_data()
    assert loaded == registry_data

    summary = auditor.audit_component_performance(registry_data["milestones"])
    assert summary["total_components"] == 3
    assert summary["fully_covered_count"] == 2
    assert summary["audit_status"] == "PASSED"

    saved_report = auditor.generate_report(registry_data["milestones"], str(report_file))
    assert saved_report == str(report_file)
    assert os.path.exists(str(report_file))
    assert os.path.getsize(str(report_file)) > 0

def test_load_registry_runtime_error(tmp_path, monkeypatch):
    """Valida que un error inesperado al leer el registro lance un RuntimeError."""
    registry_file = tmp_path / "registry.json"
    registry_file.write_text('{"milestones": []}', encoding="utf-8")
    
    auditor = ArchitectureAuditor(str(registry_file))
    
    # Simular un error genérico (diferente a FileNotFoundError o ValueError) al abrir el archivo
    def mock_open(*args, **kwargs):
        raise PermissionError("Acceso denegado simulado")
    
    monkeypatch.setattr("builtins.open", mock_open)
    
    with pytest.raises(RuntimeError, match="Error crítico al leer el registro de arquitectura"):
        auditor.load_registry_data()

def test_generate_report_runtime_error(tmp_path, monkeypatch):
    """Valida que un error inesperado al generar el informe de auditoría lance un RuntimeError."""
    registry_file = tmp_path / "registry.json"
    registry_file.write_text('{"milestones": []}', encoding="utf-8")
    
    auditor = ArchitectureAuditor(str(registry_file))
    components = [{"name": "D157", "coverage_percentage": 100.0, "status": "active"}]
    
    # Simular un error genérico al abrir el archivo para escritura
    def mock_open(*args, **kwargs):
        raise PermissionError("Error de escritura simulado")
        
    monkeypatch.setattr("builtins.open", mock_open)
    
    with pytest.raises(RuntimeError, match="Error crítico al generar el informe de auditoría"):
        auditor.generate_report(components, str(tmp_path / "report.json"))