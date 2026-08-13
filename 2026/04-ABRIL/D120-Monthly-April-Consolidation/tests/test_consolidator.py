import pytest
from src.consolidator import AprilBlockConsolidator

def test_audit_milestones_success(tmp_path):
    """Prueba la auditoría exitosa de hitos existentes."""
    # Creamos carpetas simuladas de hitos en tmp_path
    milestone_name = "D110-Openpyxl-Financial-Modeler"
    d = tmp_path / milestone_name
    d.mkdir()

    consolidator = AprilBlockConsolidator(april_path=str(tmp_path))
    results = consolidator.audit_milestones([milestone_name])
    
    assert results[milestone_name] is True

def test_audit_milestones_missing(tmp_path):
    """Prueba la detección de hitos faltantes o no creados."""
    consolidator = AprilBlockConsolidator(april_path=str(tmp_path))
    results = consolidator.audit_milestones(["D999-Missing-Milestone"])
    
    assert results["D999-Missing-Milestone"] is False

def test_generate_consolidation_report(tmp_path):
    """Prueba la correcta generación del reporte de cierre de bloque."""
    m1 = tmp_path / "D110-Openpyxl-Financial-Modeler"
    m1.mkdir()
    
    consolidator = AprilBlockConsolidator(april_path=str(tmp_path))
    report = consolidator.generate_consolidation_report(["D110-Openpyxl-Financial-Modeler"])
    
    assert "REPORTE DE CONSOLIDACIÓN" in report
    assert "100% COMPLETADO" in report