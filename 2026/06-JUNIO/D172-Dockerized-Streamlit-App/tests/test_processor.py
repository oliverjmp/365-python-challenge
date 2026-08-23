import pandas as pd
from src.data_processor import process_analytics_data

def test_process_analytics_data_valid():
    df = pd.DataFrame({"A": [1, None, 3], "B": [4, 5, 6]})
    result = process_analytics_data(df)
    assert result["A"].tolist() == [1.0, 0.0, 3.0]

def test_process_analytics_data_empty():
    df = pd.DataFrame()
    result = process_analytics_data(df)
    assert result.empty is True