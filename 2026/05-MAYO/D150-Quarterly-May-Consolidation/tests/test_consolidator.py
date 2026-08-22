import pytest
import os
from src.consolidator import MayConsolidator

def test_check_milestones_status(tmp_path):
    """Valida la verificación de existencia de carpetas de hitos."""
    # Crear una estructura temporal simulada
    d147 = tmp_path / "D147-Pytest-ML-Pipeline-Tests"
    d147.mkdir()
    
    consolidator = MayConsolidator(base_path=str(tmp_path))
    milestones = ["D147-Pytest-ML-Pipeline-Tests", "D148-NonExistent"]
    
    status = consolidator.check_milestones_status(milestones)
    assert status["D147-Pytest-ML-Pipeline-Tests"] is True
    assert status["D148-NonExistent"] is False

def test_generate_consolidation_report(tmp_path):
    """Valida la generación correcta del reporte de consolidación mensual."""
    d149 = tmp_path / "D149-Memory-Profiling-Optimization"
    d149.mkdir()
    
    consolidator = MayConsolidator(base_path=str(tmp_path))
    milestones = ["D149-Memory-Profiling-Optimization"]
    
    report = consolidator.generate_consolidation_report(milestones)
    assert report["total_milestones"] == 1
    assert report["completed_milestones"] == 1
    assert report["completion_rate"] == 100.0
    assert "details" in report

def test_empty_milestone_list_report():
    """Valida el comportamiento con una lista de hitos vacía."""
    consolidator = MayConsolidator()
    report = consolidator.generate_consolidation_report([])
    assert report["completion_rate"] == 0.0
    assert report["total_milestones"] == 0