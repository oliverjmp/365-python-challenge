import pytest
import pandas as pd
from pathlib import Path
from src.cleaner import DataCleaningPipeline

def test_load_data_success(tmp_path):
    """Valida la carga exitosa de un archivo CSV válido."""
    file_path = tmp_path / "test_raw.csv"
    file_path.write_text("id,product,price,stock,category\n1,ItemA,10.0,5,CatA", encoding="utf-8")

    pipeline = DataCleaningPipeline(input_path=str(file_path))
    df = pipeline.load_data()
    assert len(df) == 1
    assert "product" in df.columns

def test_load_data_not_found():
    """Valida que lance FileNotFoundError si el archivo no existe."""
    pipeline = DataCleaningPipeline(input_path="nonexistent.csv")
    with pytest.raises(FileNotFoundError):
        pipeline.load_data()

def test_clean_data_vectorized():
    """Valida la correcta sustitución de valores nulos mediante operaciones vectorizadas."""
    data = {
        "id": [1, 2, 3],
        "product": ["A", None, "C"],
        "price": [100.0, None, 300.0],
        "stock": [10, 5, None],
        "category": [None, "Tech", "Home"]
    }
    df = pd.DataFrame(data)

    pipeline = DataCleaningPipeline()
    cleaned_df = pipeline.clean_data(df)

    # Verificaciones de nulos resueltos
    assert cleaned_df["product"].iloc[1] == "Unnamed Product"
    assert cleaned_df["price"].iloc[1] == 200.0  # Mediana entre 100.0 y 300.0
    assert cleaned_df["stock"].iloc[2] == 0       # Nulo reemplazado por 0
    assert cleaned_df["category"].iloc[0] == "Unknown"

def test_run_pipeline(tmp_path):
    """Valida la ejecución integral del pipeline."""
    file_path = tmp_path / "test_raw.csv"
    file_path.write_text("id,product,price,stock,category\n1,,10.0,,", encoding="utf-8")

    pipeline = DataCleaningPipeline(input_path=str(file_path))
    result_df = pipeline.run_pipeline()

    assert len(result_df) == 1
    assert result_df["product"].iloc[0] == "Unnamed Product"
    assert result_df["stock"].iloc[0] == 0
    assert result_df["category"].iloc[0] == "Unknown"