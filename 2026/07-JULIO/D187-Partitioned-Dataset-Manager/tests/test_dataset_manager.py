import os
import pytest
from src.dataset_manager_engine import PartitionedDatasetManagerEngine

def test_pipeline_partitioned_manager(tmp_path):
    store_dir = str(tmp_path / "partitioned_store")
    manager = PartitionedDatasetManagerEngine(base_path=store_dir)

    escritura = manager.escribir_dataset_particionado(15000)
    assert escritura["filas_escritas"] == 15000

    lectura = manager.leer_dataset_filtrado("EUROPE", "2026-07-02")
    df_res = lectura["dataframe_resultados"]

    assert not df_res.empty
    assert all(df_res["region"] == "EUROPE")
    assert all(df_res["fecha"] == "2026-07-02")

def test_error_directorio_ausente():
    manager = PartitionedDatasetManagerEngine(base_path="ruta/ficticia/inexistente")
    with pytest.raises(FileNotFoundError):
        manager.leer_dataset_filtrado("ASIA", "2026-07-01")