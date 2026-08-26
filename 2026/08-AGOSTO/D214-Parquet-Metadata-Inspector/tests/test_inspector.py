import pytest
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from src.parquet_inspector import ParquetMetadataInspector

@pytest.fixture
def sample_parquet_file(tmp_path):
    file_path = tmp_path / "test_data.parquet"
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "nombre": ["Ana", "Bruno", "Carla"],
        "activo": [True, False, True]
    })
    table = pa.Table.from_pandas(df)
    pq.write_table(table, file_path)
    return str(file_path)

def test_inspector_schema(sample_parquet_file):
    inspector = ParquetMetadataInspector(sample_parquet_file)
    schema_info = inspector.get_schema_info()
    assert len(schema_info) == 3
    assert schema_info[0]["column_name"] == "id"

def test_inspector_file_metadata(sample_parquet_file):
    inspector = ParquetMetadataInspector(sample_parquet_file)
    meta = inspector.get_file_metadata()
    assert meta["num_rows"] == 3
    assert meta["num_row_groups"] >= 1

def test_inspector_row_group_stats(sample_parquet_file):
    inspector = ParquetMetadataInspector(sample_parquet_file)
    stats = inspector.get_row_group_statistics()
    assert len(stats) >= 1
    assert stats[0]["num_rows"] == 3