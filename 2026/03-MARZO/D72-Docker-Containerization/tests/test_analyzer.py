import pytest
import pandas as pd
from src.analyzer import AnalyticsMicroservice

def test_process_data():
    """Valida el procesamiento analítico del microservicio."""
    service = AnalyticsMicroservice()
    raw_data = [{"id": 1, "category": "  alpha  "}]
    df = service.process_data(raw_data)
    
    assert isinstance(df, pd.DataFrame)
    assert df.loc[0, "category"] == "ALPHA"

def test_process_data_empty():
    """Valida el comportamiento del microservicio al recibir datos vacíos."""
    service = AnalyticsMicroservice()
    df = service.process_data([])
    
    assert isinstance(df, pd.DataFrame)
    assert df.empty