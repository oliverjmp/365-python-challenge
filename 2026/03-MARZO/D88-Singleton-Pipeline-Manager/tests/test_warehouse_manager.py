import pytest
from src.warehouse_manager import WarehouseConnectionManager

def test_singleton_instance_unicity():
    """Valida que múltiples instancias apunten exactamente al mismo objeto en memoria."""
    manager1 = WarehouseConnectionManager("dw_prod_db")
    manager2 = WarehouseConnectionManager("dw_staging_db")
    
    # Comprobamos que sea la misma instancia (el string de conexión se queda con el primero inicializado)
    assert manager1 is manager2
    assert manager2.connection_string == "dw_prod_db"

def test_warehouse_query_execution():
    """Valida la ejecución correcta de operaciones a través del manager singleton."""
    manager = WarehouseConnectionManager()
    result = manager.execute_query("SELECT * FROM sales_summary")
    
    assert "SELECT * FROM sales_summary" in result
    assert manager.is_connected is True

def test_warehouse_query_execution_error():
    """Valida que se lance un error si se intenta ejecutar una consulta sin conexión activa."""
    manager = WarehouseConnectionManager()
    # Forzamos temporalmente el estado de conexión a falso para probar la excepción
    manager.is_connected = False
    
    with pytest.raises(ConnectionError, match="No hay conexión activa con el Data Warehouse."):
        manager.execute_query("SELECT * FROM sales_summary")
        
    # Restauramos la conexión para no afectar otras pruebas
    manager.is_connected = True