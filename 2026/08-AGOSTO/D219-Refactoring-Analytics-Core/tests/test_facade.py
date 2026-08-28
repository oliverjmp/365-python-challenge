import pandas as pd
import pytest
from src.facade import AnalyticsCoreFacade

@pytest.fixture
def sample_df():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "valor": [10.5, 20.0, 35.2]
    })

def test_analytics_core_facade_success(sample_df):
    facade = AnalyticsCoreFacade()
    result = facade.execute_pipeline(sample_df)

    assert "initial_memory" in result
    assert "analytical_metrics" in result
    assert result["analytical_metrics"]["total_rows"] == 3
    assert "valor" in result["analytical_metrics"]["columns"]

def test_analytics_core_facade_empty_dataframe():
    facade = AnalyticsCoreFacade()
    with pytest.raises(ValueError, match="El DataFrame de entrada está vacío."):
        facade.execute_pipeline(pd.DataFrame())