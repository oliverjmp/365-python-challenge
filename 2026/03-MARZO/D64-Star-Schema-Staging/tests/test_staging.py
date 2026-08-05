import os
import pandas as pd
import pytest
from src.database import DatabaseManager
from src.pipeline import StarSchemaETL

@pytest.fixture
def setup_test_environment(tmp_path):
    db_file = tmp_path / "test_warehouse.db"
    csv_file = tmp_path / "source_transactions.csv"

    # Crear CSV de prueba simulado
    df = pd.DataFrame({
        "customer_id": [1, 2],
        "customer_name": ["Alice", "Bob"],
        "country": ["Spain", "France"],
        "product_id": [101, 102],
        "product_name": ["Laptop", "Mouse"],
        "category": ["Electronics", "Accessories"],
        "date": ["2026-03-01", "2026-03-02"],
        "quantity": [1, 2],
        "total_amount": [1200.0, 50.0]
    })
    df.to_csv(csv_file, index=False)

    db_manager = DatabaseManager(db_path=str(db_file))
    etl = StarSchemaETL(db_manager=db_manager, csv_path=str(csv_file))
    etl.run_pipeline()

    return db_manager

def test_star_schema_integrity(setup_test_environment):
    conn = setup_test_environment.get_connection()

    # Validar registros huérfanos en la tabla de hechos frente a dimensiones
    orphaned_customers = conn.execute("""
        SELECT COUNT(*) FROM fact_transaction f 
        LEFT JOIN dim_customer c ON f.customer_id = c.customer_id 
        WHERE c.customer_id IS NULL
    ️""").fetchone()[0] # type: ignore

    assert orphaned_customers == 0, "Se encontraron registros huérfanos en clientes."

    # Validar conteo correcto en dimensiones
    customer_count = conn.execute("SELECT COUNT(*) FROM dim_customer").fetchone()[0] # type: ignore
    assert customer_count == 2

    fact_count = conn.execute("SELECT COUNT(*) FROM fact_transaction").fetchone()[0] # type: ignore
    assert fact_count == 2

    conn.close()