import os
from src.consolidation_engine import verify_semiannual_modules, generate_consolidation_report

def test_verify_semiannual_modules_success():
    """Valida la detección de artefactos principales en el directorio actual."""
    modules = verify_semiannual_modules(".")
    assert isinstance(modules, list)
    assert len(modules) > 0

def test_verify_semiannual_modules_not_found():
    """Valida que un directorio inexistente retorne una lista vacía."""
    modules = verify_semiannual_modules("ruta_falsa_inexistente_xyz")
    assert modules == []

def test_generate_consolidation_report():
    """Valida la correcta estructuración del reporte de cierre semestral."""
    report = generate_consolidation_report("2026-H1-Python-Challenge")
    assert "2026-H1-Python-Challenge" in report
    assert "=== Cierre Exitoso" in report