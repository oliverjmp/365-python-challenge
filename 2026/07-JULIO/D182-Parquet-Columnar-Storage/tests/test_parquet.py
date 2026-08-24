import os
import pytest
import pandas as pd
from src.parquet_pipeline import ParquetPipeline
from src import parquet_pipeline

def test_parquet_conversion_success(tmp_path):
    """Valida el flujo exitoso de conversión de un CSV temporal a Parquet."""
    d = tmp_path / "sub"
    d.mkdir()
    csv_file = d / "data.csv"
    parquet_file = d / "data.parquet"

    # Crear un CSV de prueba
    df_original = pd.DataFrame({"id": [1, 2], "val": [10.5, 20.1]})
    df_original.to_csv(csv_file, index=False)

    pipeline = ParquetPipeline(compression="SNAPPY")
    success = pipeline.convert_csv_to_parquet(str(csv_file), str(parquet_file))

    assert success is True
    assert os.path.exists(parquet_file)

    # Validar que el archivo Parquet se lea correctamente
    df_read = pd.read_parquet(parquet_file)
    assert len(df_read) == 2
    assert "id" in df_read.columns

def test_csv_not_found_raises_error():
    """Valida que un archivo CSV inexistente lance FileNotFoundError."""
    pipeline = ParquetPipeline()
    with pytest.raises(FileNotFoundError):
        pipeline.convert_csv_to_parquet("archivo_falso_inexistente.csv", "salida.parquet")

def test_empty_csv_raises_error(tmp_path):
    """Valida que un CSV vacío lance un ValueError."""
    d = tmp_path / "sub"
    d.mkdir()
    csv_file = d / "empty.csv"
    parquet_file = d / "empty.parquet"

    # Crear CSV vacío sin registros
    pd.DataFrame(columns=["id", "name"]).to_csv(csv_file, index=False)

    pipeline = ParquetPipeline()
    with pytest.raises(ValueError, match="está vacío"):
        pipeline.convert_csv_to_parquet(str(csv_file), str(parquet_file))

def test_pyarrow_not_available_raises_error(monkeypatch):
    """Valida que se lance ImportError si PyArrow no está disponible en el entorno."""
    monkeypatch.setattr(parquet_pipeline, "PYARROW_AVAILABLE", False)
    with pytest.raises(ImportError, match="PyArrow no está instalado"):
        ParquetPipeline()