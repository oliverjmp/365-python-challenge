import pytest
from src.pipeline_runner import DockerDuckDBPipeline

def test_pipeline_inicializacion():
    """Verifica que el pipeline inicialice la conexión correctamente."""
    pipeline = DockerDuckDBPipeline()
    assert pipeline.conn is not None

def test_ejecucion_proceso():
    """Valida que el pipeline procese los datos y devuelva el DataFrame esperado."""
    pipeline = DockerDuckDBPipeline()
    df = pipeline.ejecutar_proceso()
    
    assert not df.empty
    assert "categoria" in df.columns
    assert "monto_total" in df.columns
    assert len(df) == 3