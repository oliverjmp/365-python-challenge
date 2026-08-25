import pytest
from src.spatial_runner import SpatialQueryRunner

def test_spatial_runner_inicializacion():
    """Verifica que el runner inicialice y cargue la extensión espacial correctamente."""
    runner = SpatialQueryRunner()
    assert runner.conn is not None

def test_ejecucion_consulta_espacial():
    """Valida la correcta transformación y retorno de geometrías espaciales."""
    runner = SpatialQueryRunner()
    datos = runner.ejecutar_consulta_espacial()
    
    assert len(datos) == 3
    assert datos[0][1] == "Madrid Centro"
    assert "POINT" in datos[0][4]

def test_spatial_extension_failure(monkeypatch):
    """Verifica que se lance un RuntimeError si falla la instalación o carga de la extensión spatial."""
    from src.spatial_runner import SpatialQueryRunner
    
    # Mockeamos el método execute para que falle al intentar instalar/cargar 'spatial'
    class MockConnection:
        def execute(self, query):
            if "spatial" in query.lower():
                raise Exception("Error simulado de extensión")
            return self

    monkeypatch.setattr("duckdb.connect", lambda database=":memory:": MockConnection())
    
    with pytest.raises(RuntimeError, match="No se pudo cargar la extensión spatial"):
        SpatialQueryRunner()