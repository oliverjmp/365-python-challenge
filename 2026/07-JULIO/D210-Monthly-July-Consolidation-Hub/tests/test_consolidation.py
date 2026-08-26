import pytest
import duckdb
import pandas as pd
from src.consolidation_hub import JulyConsolidationHub

@pytest.fixture
def duckdb_memory_conn():
    conn = duckdb.connect(database=":memory:")
    yield conn
    conn.close()

def test_generar_reporte_consolidado_julio(duckdb_memory_conn):
    hub = JulyConsolidationHub(duckdb_memory_conn)
    df = hub.generar_reporte_consolidado_julio()
    
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 6
    assert "D210" in df["hito"].values

def test_calcular_kpis_globales(duckdb_memory_conn):
    hub = JulyConsolidationHub(duckdb_memory_conn)
    kpis = hub.calcular_kpis_globales()
    
    assert kpis["total_hitos_completados"] == 6
    assert kpis["cobertura_promedio_global"] == 100.0
    assert kpis["hitos_en_estado_optimo"] == 6
    assert kpis["deuda_tecnica_pendiente"] == 0.0