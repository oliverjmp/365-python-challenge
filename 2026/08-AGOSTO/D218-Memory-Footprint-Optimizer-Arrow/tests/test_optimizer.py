import pandas as pd
import pytest
from src.memory_optimizer import ArrowMemoryOptimizer

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({
        "id": range(1, 5001),
        "valor": [i * 2.5 for i in range(1, 5001)],
        "etiqueta": ["test_category"] * 5000
    })

def test_memory_pools_availability():
    pools = ArrowMemoryOptimizer.get_available_memory_pools()
    assert isinstance(pools, list)
    assert len(pools) > 0

def test_memory_pool_stats():
    stats = ArrowMemoryOptimizer.get_memory_pool_stats()
    assert "backend_name" in stats
    assert "bytes_allocated" in stats
    assert "max_memory" in stats
    assert stats["bytes_allocated"] >= 0

def test_process_dataset_with_pool(sample_dataframe):
    df_res, metrics = ArrowMemoryOptimizer.process_large_dataset_with_pool(sample_dataframe)
    assert len(df_res) == 5000
    assert metrics["rows_processed"] == 5000
    assert metrics["allocated_during"] >= 0