import pytest
import pandas as pd
from src.query_runner import DuckDBQueryRunner
from src.exceptions import SQLSyntaxError, QueryExecutionError

def test_ejecucion_query_exitosa(tmp_path):
    """Verifica que una consulta válida devuelva resultados correctos."""
    db_file = str(tmp_path / "test.db")
    runner = DuckDBQueryRunner(db_path=db_file)
    
    # Creamos una tabla auxiliar y consultamos
    runner.ejecutar_query("CREATE TABLE clientes (id INT, nombre VARCHAR);")
    runner.ejecutar_query("INSERT INTO clientes VALUES (1, 'Alpha');")
    
    df = runner.ejecutar_query("SELECT * FROM clientes;")
    assert not df.empty
    assert df.iloc[0]["nombre"] == "Alpha"

def test_captura_sql_syntax_error():
    """Verifica que un error de sintaxis lance SQLSyntaxError."""
    runner = DuckDBQueryRunner()
    query_invalida = "SELEC * FROM tabla_falsa" # Error de tipeo en SELECT
    
    with pytest.raises(SQLSyntaxError) as exc_info:
        runner.ejecutar_query(query_invalida)
    
    assert "SINTAXIS INVÁLIDA" in str(exc_info.value)

def test_captura_query_execution_error():
    """Verifica que un fallo de ejecución lógica lance QueryExecutionError."""
    runner = DuckDBQueryRunner()
    query_fallida = "SELECT * FROM tabla_que_no_existe;"
    
    with pytest.raises(QueryExecutionError) as exc_info:
        runner.ejecutar_query(query_fallida)
    
    assert "ERROR DE EJECUCIÓN" in str(exc_info.value)

def test_repropagacion_excepcion_personalizada():
    """Verifica que si la excepción ya es una instancia personalizada, se re-lanza directamente (Línea 23)."""
    runner = DuckDBQueryRunner()
    
    # Simulamos o forzamos un escenario donde el error evaluado sea una SQLSyntaxError propia
    from src.exceptions import SQLSyntaxError
    
    class MockConnectionFalla:
        def execute(self, query):
            raise SQLSyntaxError("Error forzado", query=query)
        def close(self):
            pass

    # Parcheamos temporalmente la conexión interna para forzar la excepción personalizada
    import duckdb
    original_connect = duckdb.connect
    
    try:
        duckdb.connect = lambda path: MockConnectionFalla()
        with pytest.raises(SQLSyntaxError):
            runner.ejecutar_query("SELECT mal")
    finally:
        duckdb.connect = original_connect