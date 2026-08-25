import pytest
import pandas as pd
from src.analytics_engine import DuckDBAnalyticsEngine

def test_engine_inicializacion_y_metricas(tmp_path):
    db_file = tmp_path / "data_lake" / "test_analytics.db"
    engine = DuckDBAnalyticsEngine(db_path=str(db_file))
    
    metricas = engine.obtener_metricas_globales()
    assert metricas["total_transacciones"] == 6
    assert metricas["monto_total"] > 0
    assert metricas["ticket_promedio"] > 0

def test_consulta_resumen(tmp_path):
    db_file = tmp_path / "data_lake" / "test_analytics.db"
    engine = DuckDBAnalyticsEngine(db_path=str(db_file))
    
    df = engine.ejecutar_consulta_resumen()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "categoria" in df.columns
    assert "ventas_totales" in df.columns