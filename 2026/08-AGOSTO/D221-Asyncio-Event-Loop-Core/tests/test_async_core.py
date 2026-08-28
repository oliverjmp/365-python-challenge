import pytest
import asyncio
from src.async_core import AsyncEventLoopCore

@pytest.mark.asyncio
async def test_simulate_io_task():
    core = AsyncEventLoopCore()
    result = await core.simulate_io_task(1, 0.01)
    assert result["task_id"] == 1
    assert result["status"] == "COMPLETED"
    assert result["duration"] >= 0.01

@pytest.mark.asyncio
async def test_execute_concurrent_workload_success():
    core = AsyncEventLoopCore()
    workload = await core.execute_concurrent_workload(5, 0.01)
    assert workload["total_tasks"] == 5
    assert len(workload["results"]) == 5
    assert workload["total_duration"] < 0.2  # Comprobación de concurrencia real

@pytest.mark.asyncio
async def test_execute_concurrent_workload_invalid_count():
    core = AsyncEventLoopCore()
    with pytest.raises(ValueError, match="El número de tareas concurrentes debe ser mayor a cero."):
        await core.execute_concurrent_workload(0)