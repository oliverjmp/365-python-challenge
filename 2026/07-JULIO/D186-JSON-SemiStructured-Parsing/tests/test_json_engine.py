import os
import pytest
from src.json_parsing_engine import JSONSemiStructuredEngine

def test_pipeline_json_parsing(tmp_path):
    dir_test = tmp_path / "lake"
    dir_test.mkdir()
    parquet_file = str(dir_test / "test_json.parquet")

    engine = JSONSemiStructuredEngine()
    
    meta = engine.generar_dataset_json(parquet_file)
    assert meta["total_filas"] > 0
    assert os.path.exists(parquet_file)

    analisis = engine.consultar_datos_json(parquet_file)
    df_res = analisis["dataframe_resultados"]

    assert not df_res.empty
    assert "tipo_evento" in df_res.columns
    assert "latencia_promedio_ms" in df_res.columns

    engine.cerrar_conexion()

def test_error_archivo_ausente():
    engine = JSONSemiStructuredEngine()
    with pytest.raises(FileNotFoundError):
        engine.consultar_datos_json("ruta/ficticia/datos.parquet")
    engine.cerrar_conexion()