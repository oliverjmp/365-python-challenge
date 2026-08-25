import os
import pytest
from src.batch_converter import CSVParquetBatchConverter

def test_conversor_por_lotes(tmp_path):
    raw = tmp_path / "raw"
    processed = tmp_path / "processed"
    
    converter = CSVParquetBatchConverter(raw_dir=str(raw), processed_dir=str(processed))
    
    # Crear un CSV pequeño para test
    import pandas as pd
    df = pd.DataFrame({"id": [1, 2, 3], "texto": ["a", "b", "c"]})
    csv_test = raw / "test.csv"
    df.to_csv(csv_test, index=False)
    
    total = converter.convertir_a_parquet("test.csv", "test_out.parquet", chunksize=1)
    assert total == 3
    assert os.path.exists(processed / "test_out.parquet")

def test_csv_no_encontrado_lanza_error(tmp_path):
    converter = CSVParquetBatchConverter(raw_dir=str(tmp_path / "raw"), processed_dir=str(tmp_path / "processed"))
    with pytest.raises(FileNotFoundError):
        list(converter.leer_csv_por_lotes("no_existe.csv"))