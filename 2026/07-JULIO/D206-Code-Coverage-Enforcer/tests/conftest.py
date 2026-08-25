import pytest
import duckdb

@pytest.fixture(scope="function")
def duckdb_audit_conn():
    """Fixture que inicializa una base de datos DuckDB efímera para pruebas."""
    conn = duckdb.connect(database=":memory:")
    
    conn.execute("""
        CREATE TABLE audit_data (
            id INTEGER,
            departamento VARCHAR,
            gasto DOUBLE,
            fecha DATE,
            aprobado BOOLEAN
        );
    """)
    
    conn.execute("""
        INSERT INTO audit_data VALUES
        (1, 'Ingeniería', 4500.00, '2026-07-01', TRUE),
        (2, 'Marketing', 1200.50, '2026-07-02', TRUE),
        (3, 'Ventas', 3100.00, '2026-07-03', FALSE),
        (4, 'Ingeniería', 850.25, '2026-07-04', TRUE),
        (5, 'Marketing', 400.00, '2026-07-05', FALSE);
    """)
    
    yield conn
    conn.close()