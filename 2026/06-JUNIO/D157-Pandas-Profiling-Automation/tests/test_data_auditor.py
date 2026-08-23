import pytest
import pandas as pd
from src.data_auditor import DataAuditorEngine

def test_auditor_empty_dataframe_raises_error():
    """Valida que inicializar el motor con un DataFrame vacío lance un ValueError."""
    with pytest.raises(ValueError, match="no puede ser nulo ni estar vacío"):
        DataAuditorEngine(pd.DataFrame())

def test_auditor_none_dataframe_raises_error():
    """Valida que inicializar con None lance un ValueError."""
    with pytest.raises(ValueError, match="no puede ser nulo ni estar vacío"):
        DataAuditorEngine(None) # type: ignore

def test_generate_profile_report_success():
    """Valida la creación exitosa del objeto ProfileReport."""
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, 5],
        "B": ["foo", "bar", "foo", "bar", "baz"]
    })
    auditor = DataAuditorEngine(df)
    profile = auditor.generate_profile_report(title="Test Report")
    
    assert profile is not None

def test_export_report_invalid_extension_raises_error(tmp_path):
    """Valida que exportar a una ruta sin extensión .html lance un ValueError."""
    df = pd.DataFrame({"A": [1, 2, 3]})
    auditor = DataAuditorEngine(df)
    
    invalid_path = tmp_path / "report.txt"
    with pytest.raises(ValueError, match="extensión .html"):
        auditor.export_report_to_html(str(invalid_path))

def test_export_report_to_html_success(tmp_path):
    """Valida la exportación correcta del reporte interactivo a un archivo HTML físico."""
    df = pd.DataFrame({
        "id": [101, 102, 103],
        "valor": [15.5, 20.1, 19.8]
    })
    auditor = DataAuditorEngine(df)
    
    output_file = tmp_path / "auditoria_resultado.html"
    result_path = auditor.export_report_to_html(str(output_file), title="Auditoría Comercial")
    
    assert result_path == str(output_file)
    assert output_file.exists()
    assert output_file.stat().st_size > 0