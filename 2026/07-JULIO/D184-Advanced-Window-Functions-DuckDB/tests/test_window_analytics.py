import os
import pytest
from src.window_analytics_engine import AdvancedWindowAnalyticsEngine

def test_pipeline_window_functions(tmp_path):
    dir_test = tmp_path / "lake"
    dir_test.mkdir()
    parquet_file = str(dir_test / "test_financiero.parquet")

    engine = AdvancedWindowAnalyticsEngine()
    
    meta = engine.generar_dataset_financiero(parquet_file)
    assert meta["total_filas"] > 0
    assert os.path.exists(parquet_file)

    analisis = engine.calcular_metricas_financieras(parquet_file)
    df_res = analisis["dataframe_resultados"]

    assert not df_res.empty
    assert "ingresos_acumulados_anio" in df_res.columns
    assert "variacion_mom_pct" in df_res.columns
    assert len(df_res) == meta["total_filas"]

    engine.cerrar_conexion()

def test_error_archivo_ausente():
    engine = AdvancedWindowAnalyticsEngine()
    with pytest.raises(FileNotFoundError):
        engine.calcular_metricas_financieras("ruta/ficticia/datos.parquet")
    engine.cerrar_conexion()