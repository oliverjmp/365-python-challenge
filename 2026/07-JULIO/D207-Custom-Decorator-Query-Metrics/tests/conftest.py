import pytest
import duckdb

@pytest.fixture(scope="function")
def duckdb_metrics_conn():
    """Fixture que inicializa una conexión DuckDB efímera para pruebas de telemetría."""
    conn = duckdb.connect(database=":memory:")
    
    conn.execute("""
        CREATE TABLE metrics_data (
            id INTEGER,
            operacion VARCHAR,
            tabla VARCHAR,
            filas_afectadas INTEGER,
            estado VARCHAR
        );
    """)
    
    conn.execute("""
        INSERT INTO metrics_data VALUES
        (1, 'SELECT', 'transacciones', 150, 'Exitoso'),
        (2, 'INSERT', 'transacciones', 45, 'Exitoso'),
        (3, 'UPDATE', 'logs', 12, 'Exitoso'),
        (4, 'SELECT', 'logs', 500, 'Exitoso');
    """)
    
    yield conn
    conn.close()