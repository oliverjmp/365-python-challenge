import pytest
from src.schema import schema

@pytest.mark.asyncio
async def test_query_all_logs():
    """Valida la consulta GraphQL para obtener todos los registros de logs."""
    query = """
        query {
            logs {
                id
                level
                message
            }
        }
    """
    result = await schema.execute(query)
    assert result.errors is None
    data = result.data
    assert len(data["logs"]) == 3
    assert data["logs"][0]["level"] == "INFO"

@pytest.mark.asyncio
async def test_query_logs_with_filter():
    """Valida el filtrado de logs por nivel existente mediante argumentos en GraphQL."""
    query = """
        query {
            logs(level: "ERROR") {
                id
                message
            }
        }
    """
    result = await schema.execute(query)
    assert result.errors is None
    data = result.data
    assert len(data["logs"]) == 1
    assert data["logs"][0]["id"] == "2"

@pytest.mark.asyncio
async def test_query_logs_with_empty_filter_result():
    """Valida el filtrado con un nivel que no existe para cubrir ramas vacías."""
    query = """
        query {
            logs(level: "CRITICAL") {
                id
                message
            }
        }
    """
    result = await schema.execute(query)
    assert result.errors is None
    data = result.data
    assert len(data["logs"]) == 0

@pytest.mark.asyncio
async def test_query_single_log_by_id():
    """Valida la consulta de un único registro existente por su ID."""
    query = """
        query {
            log(id: "3") {
                level
                message
            }
        }
    """
    result = await schema.execute(query)
    assert result.errors is None
    data = result.data
    assert data["log"]["level"] == "WARNING"

@pytest.mark.asyncio
async def test_query_single_log_not_found():
    """Valida la consulta de un registro por ID cuando este no existe (retorna null)."""
    query = """
        query {
            log(id: "999") {
                level
                message
            }
        }
    """
    result = await schema.execute(query)
    assert result.errors is None
    data = result.data
    assert data["log"] is None