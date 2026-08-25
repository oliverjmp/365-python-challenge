import pytest
import duckdb

@pytest.fixture(scope="function")
def duckdb_memory_conn():
    """Fixture que provee una conexión DuckDB en memoria aislada por cada test."""
    conn = duckdb.connect(database=":memory:")
    
    # Creación del esquema relacional optimizado
    conn.execute("""
        CREATE TABLE transactions (
            id INTEGER,
            categoria VARCHAR,
            monto DOUBLE,
            fecha DATE,
            estado VARCHAR
        );
    """)
    
    # Ingesta de datos sintéticos controlados para pruebas deterministas
    conn.execute("""
        INSERT INTO transactions VALUES
        (1, 'Hardware', 1200.50, '2026-07-01', 'Completado'),
        (2, 'Software', 450.99, '2026-07-02', 'Completado'),
        (3, 'Servicios', 300.00, '2026-07-03', 'Pendiente'),
        (4, 'Hardware', 150.00, '2026-07-04', 'Completado'),
        (5, 'Software', 89.99, '2026-07-05', 'Completado'),
        (6, 'Logística', 1500.00, '2026-07-06', 'Completado'),
        (7, 'Servicios', 650.25, '2026-07-07', 'Pendiente');
    """)
    
    yield conn
    conn.close()