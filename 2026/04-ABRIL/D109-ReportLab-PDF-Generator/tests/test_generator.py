import pytest
from pathlib import Path
from src.generator import ExecutiveReportGenerator
from reportlab.graphics.shapes import Drawing

def test_vector_chart_creation():
    """Valida que la función devuelva un objeto Drawing válido con elementos gráficos."""
    generator = ExecutiveReportGenerator()
    chart = generator.create_vector_chart()
    assert isinstance(chart, Drawing)
    assert len(chart.contents) > 0

def test_generate_pdf_success(tmp_path):
    """Valida la generación exitosa del fichero PDF físico en el disco."""
    pdf_path = tmp_path / "test_report.pdf"
    generator = ExecutiveReportGenerator(output_filename=str(pdf_path))
    
    sample_data = {
        "title": "Reporte de Prueba Unitaria",
        "date": "2026-04-12",
        "author": "Test Suite Bot"
    }

    result_file = generator.generate_pdf(sample_data)
    
    assert result_file == str(pdf_path)
    assert pdf_path.exists()
    # Comprueba que el archivo PDF tiene contenido binario generado
    assert pdf_path.stat().st_size > 0