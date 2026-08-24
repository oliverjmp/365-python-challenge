import os
import pytest
from src.parquet_query_engine import EnterpriseParquetEngine

def test_pipeline_analitico_corporativo(tmp_path):
    """Valida el ciclo completo de ingesta empresarial y consulta analítica directa."""
    dir_trabajo = tmp_path / "lakehouse"
    dir_trabajo.mkdir()
    archivo_parquet = str(dir_trabajo / "transacciones_enterprise.parquet")

    engine = EnterpriseParquetEngine()
    
    # 1. Validar la ingesta
    meta = engine.simular_ingesta_corporativa(archivo_parquet)
    assert meta["registros"] == 250000
    assert os.path.exists(archivo_parquet)

    # 2. Validar la analítica directa sin RAM
    analisis = engine.ejecutar_analitica_directa(archivo_parquet)
    assert analisis["latencia_consulta_ms"] > 0
    df_res = analisis["dataframe_resultados"]
    
    assert not df_res.empty
    assert "ingresos_totales" in df_res.columns
    assert "ticket_promedio" in df_res.columns

    engine.cerrar_conexion()

def test_excepcion_archivo_inexistente():
    """Valida el manejo de errores corporativo ante ficheros corruptos o ausentes."""
    engine = EnterpriseParquetEngine()
    with pytest.raises(FileNotFoundError):
        engine.ejecutar_analitica_directa("ruta/almacen_inexistente.parquet")
    engine.cerrar_conexion()