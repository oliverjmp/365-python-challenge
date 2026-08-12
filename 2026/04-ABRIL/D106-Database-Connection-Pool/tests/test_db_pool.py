from src.db_pool import DatabaseConnectionPool

def test_db_pool_initialization():
    """Valida la correcta inicialización del pool y sus parámetros."""
    pool_manager = DatabaseConnectionPool(db_url="sqlite:///:memory:", pool_size=3, max_overflow=5)
    status = pool_manager.get_connection_status()
    
    # El tamaño configurado del pool debe ser 3
    assert status["size"] == 3
    # Inicialmente no hay conexiones checked out ni checked in físicas creadas hasta usarlas
    assert "checkedin" in status
    assert "checkedout" in status
    assert "overflow" in status

def test_execute_query():
    """Valida la ejecución exitosa de consultas usando el pool."""
    pool_manager = DatabaseConnectionPool(db_url="sqlite:///:memory:")
    result = pool_manager.execute_query("SELECT 1")
    assert result == 1