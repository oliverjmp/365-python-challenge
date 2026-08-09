import os
import pytest
from src.processor import stream_csv_rows, filter_high_values

@pytest.fixture
def temp_csv(tmp_path):
    """Crea un archivo CSV temporal para realizar las pruebas unitarias."""
    file_path = tmp_path / "data.csv"
    content = "id,value\n1,10.5\n2,95.0\n3,45.2\n4,150.0\n"
    file_path.write_text(content, encoding="utf-8")
    return str(file_path)

def test_stream_csv_rows(temp_csv):
    """Valida que el generador lea todas las filas correctamente."""
    rows = list(stream_csv_rows(temp_csv))
    assert len(rows) == 4
    assert rows[0]["id"] == "1"
    assert rows[3]["value"] == "150.0"

def test_filter_high_values(temp_csv):
    """Valida el filtrado eficiente de filas mediante generadores."""
    rows = stream_csv_rows(temp_csv)
    filtered = list(filter_high_values(rows, threshold=50.0))
    
    assert len(filtered) == 2
    assert filtered[0]["id"] == "2"
    assert filtered[1]["id"] == "4"