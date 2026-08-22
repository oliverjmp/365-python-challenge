import pytest
import pandas as pd
from src.filter_engine import DataFilterEngine

@pytest.fixture
def sample_data():
    data = {
        "id": [1, 2, 3, 4],
        "categoria": ["Tech", "Finance", "Tech", "HR"],
        "valor": [100.5, 200.0, 150.0, 50.0]
    }
    return pd.DataFrame(data)

def test_filter_by_categories(sample_data):
    engine = DataFilterEngine(sample_data)
    result = engine.filter_by_categories("categoria", ["Tech"])
    assert len(result) == 2
    assert all(result["categoria"] == "Tech")

def test_filter_by_categories_empty(sample_data):
    engine = DataFilterEngine(sample_data)
    result = engine.filter_by_categories("categoria", [])
    assert len(result) == 4

def test_filter_by_numeric_range(sample_data):
    engine = DataFilterEngine(sample_data)
    result = engine.filter_by_numeric_range("valor", 100.0, 160.0)
    assert len(result) == 2
    assert set(result["id"]) == {1, 3}

def test_get_summary_metrics(sample_data):
    engine = DataFilterEngine(sample_data)
    metrics = engine.get_summary_metrics(sample_data, "valor")
    assert metrics["count"] == 4
    assert metrics["total"] == 500.5  # Corregido de 505.5 a 500.5
    assert metrics["average"] == 500.5 / 4

def test_get_summary_metrics_empty():
    engine = DataFilterEngine(pd.DataFrame(columns=["id", "categoria", "valor"]))
    metrics = engine.get_summary_metrics(pd.DataFrame(), "valor")
    assert metrics["count"] == 0
    assert metrics["total"] == 0.0
    assert metrics["average"] == 0.0