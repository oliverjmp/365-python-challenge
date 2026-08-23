import pandas as pd
from src.data_loader import load_cached_data

def test_load_cached_data():
    df = load_cached_data(500)
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 500
    assert "value" in df.columns