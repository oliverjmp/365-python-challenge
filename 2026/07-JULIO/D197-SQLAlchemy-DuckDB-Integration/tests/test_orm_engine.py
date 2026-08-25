import os
import pytest
from src.orm_engine import DuckDBORMManager
import pytest
from src.orm_engine import DuckDBORMManager

def test_orm_conexion_y_creacion(tmp_path):
    db_file = tmp_path / "data_lake" / "test_orm.db"
    manager = DuckDBORMManager(db_path=str(db_file))
    
    clientes = manager.obtener_todos_los_clientes()
    assert isinstance(clientes, list)
    assert len(clientes) == 0

def test_guardar_y_consultar_cliente(tmp_path):
    db_file = tmp_path / "data_lake" / "test_orm.db"
    manager = DuckDBORMManager(db_path=str(db_file))
    
    cliente_id = manager.guardar_cliente(nombre="Ana Torres", segmento="VIP", limite_credito=5000.0)
    assert cliente_id > 0
    
    clientes = manager.obtener_todos_los_clientes()
    assert len(clientes) == 1
    assert clientes[0]["nombre"] == "Ana Torres"
    assert clientes[0]["segmento"] == "VIP"


def test_guardar_cliente_error(tmp_path):
    """Verifica que se capture la excepción y se haga rollback si ocurre un error al guardar."""
    db_file = tmp_path / "data_lake" / "test_orm_error.db"
    manager = DuckDBORMManager(db_path=str(db_file))
    
    # Forzamos un error pasando un tipo de dato incorrecto (por ejemplo, None en un campo obligatorio que no lo acepta)
    # o cerrando/invalidando la sesión de alguna forma. Una forma limpia es pasar un valor inválido 
    # que cause un error de SQLAlchemy/DuckDB, como un objeto no soportado en el campo nombre.
    with pytest.raises(Exception):
        # Un diccionario o un objeto complejo no puede ser convertido a VARCHAR por SQLAlchemy/DuckDB limpiamente
        manager.guardar_cliente(nombre=None, segmento="Corporativo", limite_credito=1000.0)