import pytest
import pandas as pd
from src.aggregation_manager import AdvancedAggregationManager

@pytest.fixture
def agg_manager():
    manager = AdvancedAggregationManager(":memory:")
    df_test = pd.DataFrame({
        "region": ["Norte", "Norte", "Sur", "Sur"],
        "categoria": ["Hardware", "Software", "Hardware", "Software"],
        "ventas": [100.0, 200.0, 150.0, 250.0]
    })
    manager.load_dataset("ventas_globales", df_test)
    yield manager
    manager.close()

def test_load_dataset(agg_manager):
    df_res = agg_manager.execute_rollup("ventas_globales", "region", "categoria", "ventas")
    assert len(df_res) > 0

def test_execute_rollup(agg_manager):
    df_res = agg_manager.execute_rollup("ventas_globales", "region", "categoria", "ventas")
    # ROLLUP genera agregaciones jerárquicas incluyendo subtotales y total general
    assert "total_metric" in df_res.columns
    assert len(df_res) >= 4

def test_execute_cube(agg_manager):
    df_res = agg_manager.execute_cube("ventas_globales", "region", "categoria", "ventas")
    # CUBE genera todas las combinaciones cruzadas posibles
    assert "total_metric" in df_res.columns
    assert len(df_res) >= 4