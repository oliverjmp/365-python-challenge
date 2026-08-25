import pytest
import asyncio
from src.async_engine import AsyncDuckDBRunner

@pytest.mark.asyncio
async def test_ejecucion_concurrente_exitosa(tmp_path):
    """Valida la ejecución concurrente leyendo desde un archivo DuckDB temporal en disco."""
    db_file = tmp_path / "data_lake" / "test_analytics.db"
    runner = AsyncDuckDBRunner(db_path=str(db_file))
    
    queries = [
        {"id": "TEST_1", "query": "SELECT COUNT(*) FROM ventas_analiticas;", "delay": 0.02},
        {"id": "TEST_2", "query": "SELECT categoria FROM ventas_analiticas;", "delay": 0.02}
    ]
    
    resultados = await runner.ejecutar_lote_concurrente(queries)
    
    assert len(resultados) == 2
    assert resultados[0]["query_id"] == "TEST_1"
    assert resultados[0]["filas_obtenidas"] > 0
    assert resultados[1]["query_id"] == "TEST_2"