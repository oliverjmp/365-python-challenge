import pytest
import os
from src.pdf_generator import ExecutivePDFGenerator

def test_invalid_filename_raises_error():
    """Valida que una ruta de archivo sin extensión .pdf lance un ValueError."""
    with pytest.raises(ValueError, match="extensión .pdf"):
        ExecutivePDFGenerator("reporte_invalido.txt")

def test_empty_filename_raises_error():
    """Valida que un nombre de archivo vacío lance un ValueError."""
    with pytest.raises(ValueError, match="extensión .pdf"):
        ExecutivePDFGenerator("")

def test_empty_title_raises_error(tmp_path):
    """Valida que un título vacío lance un ValueError al generar el reporte."""
    pdf_path = tmp_path / "test.pdf"
    generator = ExecutivePDFGenerator(str(pdf_path))
    
    with pytest.raises(ValueError, match="El título del informe no puede estar vacío"):
        generator.generate_report("", "Subtítulo", [["A", "B", "C"]])

def test_empty_rows_raises_error(tmp_path):
    """Valida que un conjunto de filas vacío lance un ValueError."""
    pdf_path = tmp_path / "test.pdf"
    generator = ExecutivePDFGenerator(str(pdf_path))
    
    with pytest.raises(ValueError, match="no pueden estar vacías"):
        generator.generate_report("Título Válido", "Subtítulo", [])

def test_pdf_generation_success(tmp_path):
    """Valida la generación exitosa del PDF corporativo estructurado."""
    pdf_path = tmp_path / "informe_ejecutivo.pdf"
    generator = ExecutivePDFGenerator(str(pdf_path))

    rows = [
        ["Métrica", "Categoría", "Valor"],
        ["Ingresos", "Retail", "$45,000 USD"],
        ["Conversión", "Digital", "3.8%"],
        ["Retención", "SaaS", "94.2%"]
    ]

    result = generator.generate_report(
        title="Informe Financiero Q2",
        subtitle="Auditoría de Rendimiento Global",
        data_rows=rows
    )

    assert result == str(pdf_path)
    assert os.path.exists(str(pdf_path))
    assert os.path.getsize(str(pdf_path)) > 0

def test_generate_report_runtime_error(tmp_path):
    """Valida que un error crítico durante la compilación del PDF lance un RuntimeError."""
    # Intentar guardar el PDF en una ruta que sea un directorio inválido o un archivo bloqueado forzará la excepción
    invalid_dir_path = tmp_path / "directorio_inexistente" / "archivo.pdf"
    generator = ExecutivePDFGenerator(str(invalid_dir_path))

    with pytest.raises(RuntimeError, match="Error crítico al compilar el documento PDF"):
        generator.generate_report(
            title="Título de Prueba",
            subtitle="Subtítulo",
            data_rows=[["A", "B", "C"]]
        )