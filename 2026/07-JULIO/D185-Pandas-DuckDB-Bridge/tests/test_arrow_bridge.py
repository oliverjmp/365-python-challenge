import pytest
import pyarrow as pa
from src.arrow_bridge_engine import PandasDuckDBBridgeEngine

def test_pipeline_arrow_bridge():
    engine = PandasDuckDBBridgeEngine()
    
    table_arrow = engine.generar_dataset_vectorial(10000)
    assert isinstance(table_arrow, pa.Table)
    assert table_arrow.num_rows == 10000

    analisis = engine.ejecutar_analitica_bridge(table_arrow)
    df_res = analisis["dataframe_resultados"]

    assert not df_res.empty
    assert "departamento" in df_res.columns
    assert "monto_total" in df_res.columns

    engine.cerrar_conexion()