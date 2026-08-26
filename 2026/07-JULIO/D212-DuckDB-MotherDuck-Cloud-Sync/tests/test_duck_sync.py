import pytest
import pandas as pd
from src.duck_sync import DuckDBMotherDuckManager

@pytest.fixture
def db_manager():
    manager = DuckDBMotherDuckManager(":memory:")
    df_test = pd.DataFrame({
        "id": [1, 2, 3],
        "producto": ["Laptop", "Mouse", "Teclado"],
        "precio": [1200.0, 25.5, 45.0]
    })
    manager.create_local_table("productos_locales", df_test)
    yield manager
    manager.close()

def test_create_and_query_local_table(db_manager):
    df_res = db_manager.query_hybrid_data("SELECT * FROM productos_locales")
    assert len(df_res) == 3
    assert list(df_res["producto"]) == ["Laptop", "Mouse", "Teclado"]

def test_simulate_cloud_sync(db_manager):
    rows_synced = db_manager.simulate_cloud_sync("productos_locales", "md.productos_nube")
    assert rows_synced == 3

def test_hybrid_analytical_query(db_manager):
    query = "SELECT SUM(precio) as total FROM productos_locales"
    df_res = db_manager.query_hybrid_data(query)
    assert df_res["total"].iloc[0] == 1270.5