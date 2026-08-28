import pandas as pd
import pytest
from src.data_validator import DataQualityEngine

@pytest.fixture
def valid_data():
    return pd.DataFrame({
        "transaction_id": [1, 2, 3],
        "customer_id": [101, 102, 103],
        "amount": [150.00, 1200.50, 45.00],
        "status": ["COMPLETED", "PENDING", "COMPLETED"],
        "event_date": ["2026-08-01", "2026-08-02", "2026-08-03"]
    })

def test_data_quality_success(valid_data):
    engine = DataQualityEngine()
    engine.create_validated_table(valid_data, "test_table")
    
    metrics = engine.run_data_assertions("test_table")
    assert metrics["total_valid_rows"] == 3
    assert metrics["null_customers"] == 0
    assert metrics["null_amounts"] == 0
    assert metrics["high_amount_outliers"] == 0
    engine.close()

def test_data_quality_constraint_violation(valid_data):
    # Modificamos el dataset para que viole la restricción CHECK (amount > 0.0)
    invalid_df = valid_data.copy()
    invalid_df.loc[0, "amount"] = -50.00
    
    engine = DataQualityEngine()
    with pytest.raises(Exception):
        engine.create_validated_table(invalid_df, "invalid_table")
    engine.close()