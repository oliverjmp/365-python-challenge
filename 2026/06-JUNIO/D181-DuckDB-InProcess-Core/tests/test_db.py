import pytest
from src.db_engine import DuckDBEngine

def test_duckdb_connection_and_query():
    """Valida la conexión básica y la ejecución de una consulta SQL simple."""
    engine = DuckDBEngine(":memory:")
    result = engine.execute_query("SELECT 42 AS val;")
    assert result == [(42,)]
    engine.close()

def test_duckdb_query_with_parameters():
    """Valida la ejecución de consultas SQL con paso de parámetros para cubrir la rama faltante."""
    engine = DuckDBEngine(":memory:")
    result = engine.execute_query("SELECT ? + ? AS sum_val;", (10, 32))
    assert result == [(42,)]
    engine.close()

def test_duckdb_sample_table_operations():
    """Valida la creación de tablas, inserción y consultas analíticas agrupadas."""
    engine = DuckDBEngine(":memory:")
    engine.create_sample_table()
    
    # Consultar datos filtrados o agregados
    result = engine.execute_query("SELECT category, SUM(value) FROM analytics_data GROUP BY category ORDER BY category;")
    assert len(result) == 2
    assert result[0] == ('A', 25.7)
    assert result[1] == ('B', 20.0)
    engine.close()