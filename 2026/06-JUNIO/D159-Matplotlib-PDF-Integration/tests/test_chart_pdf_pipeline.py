import pytest
import os
from src.chart_pdf_pipeline import ChartPDFPipeline

def test_invalid_filename_raises_error():
    """Valida que una ruta de salida sin extensión .pdf lance un ValueError."""
    with pytest.raises(ValueError, match="extensión .pdf"):
        ChartPDFPipeline("reporte.docx")

def test_empty_filename_raises_error():
    """Valida que un nombre de archivo vacío lance un ValueError."""
    with pytest.raises(ValueError, match="extensión .pdf"):
        ChartPDFPipeline("")

def test_generate_chart_empty_data_raises_error(tmp_path):
    """Valida que pasar listas vacías o desiguales al generador de gráficos lance ValueError."""
    pipeline = ChartPDFPipeline(str(tmp_path / "test.pdf"))
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        pipeline.generate_chart_image([], [])
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        pipeline.generate_chart_image(["A", "B"], [10])

def test_build_report_empty_title_raises_error(tmp_path):
    """Valida que un título vacío lance un ValueError."""
    pipeline = ChartPDFPipeline(str(tmp_path / "test.pdf"))
    with pytest.raises(ValueError, match="El título del informe no puede estar vacío"):
        pipeline.build_report_with_chart("", ["Norte", "Sur"], [100, 200], [["Col1", "Col2", "Col3"]])

def test_build_report_empty_table_raises_error(tmp_path):
    """Valida que datos de tabla vacíos lancen un ValueError."""
    pipeline = ChartPDFPipeline(str(tmp_path / "test.pdf"))
    with pytest.raises(ValueError, match="no pueden estar vacíos"):
        pipeline.build_report_with_chart("Título", ["Norte", "Sur"], [100, 200], [])

def test_pipeline_full_generation_success(tmp_path):
    """Valida el flujo completo de rasterización de gráfico e incrustación en PDF corporativo."""
    pdf_path = tmp_path / "reporte_estadistico_final.pdf"
    pipeline = ChartPDFPipeline(str(pdf_path))

    categories = ["Enero", "Febrero", "Marzo", "Abril"]
    values = [12500, 18200, 15400, 22100]
    
    table_data = [
        ["Mes", "Segmento", "Total Facturado"],
        ["Enero", "Enterprise", "$12,500"],
        ["Febrero", "Enterprise", "$18,200"],
        ["Marzo", "Enterprise", "$15,400"],
        ["Abril", "Enterprise", "$22,100"]
    ]

    result = pipeline.build_report_with_chart(
        title="Auditoría de Crecimiento Trimestral",
        categories=categories,
        values=values,
        summary_table_data=table_data
    )

    assert result == str(pdf_path)
    assert os.path.exists(str(pdf_path))
    assert os.path.getsize(str(pdf_path)) > 0

def test_generate_chart_runtime_error(tmp_path):
    """Valida que un fallo al generar el gráfico lance un RuntimeError."""
    pipeline = ChartPDFPipeline(str(tmp_path / "test.pdf"))
    # Forzar un fallo pasando tipos de datos incompatibles que rompan Matplotlib
    with pytest.raises(RuntimeError, match="Error crítico al renderizar el gráfico estadístico"):
        pipeline.generate_chart_image(["A"], [None]) # type: ignore

def test_build_report_runtime_error(tmp_path):
    """Valida que un fallo crítico durante la compilación del PDF con gráficos lance un RuntimeError."""
    # Usar una ruta inválida que sea un directorio bloqueará la compilación del SimpleDocTemplate
    invalid_path = tmp_path / "dir_inexistente" / "reporte.pdf"
    pipeline = ChartPDFPipeline(str(invalid_path))
    
    with pytest.raises(RuntimeError, match="Error crítico al compilar el PDF con gráficos"):
        pipeline.build_report_with_chart(
            title="Título Válido",
            categories=["A", "B"],
            values=[10, 20],
            summary_table_data=[["Col1", "Col2", "Col3"]]
        )