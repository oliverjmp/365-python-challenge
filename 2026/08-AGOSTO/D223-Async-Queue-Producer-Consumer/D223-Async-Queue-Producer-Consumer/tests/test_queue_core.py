import pytest
import asyncio
from src.queue_core import AsyncQueueManager

@pytest.mark.asyncio
async def test_producer_success():
    manager = AsyncQueueManager(maxsize=5)
    count = await manager.producer([1, 2, 3], delay=0.001)
    assert count == 3
    assert manager.queue.qsize() == 3

@pytest.mark.asyncio
async def test_producer_empty_list():
    manager = AsyncQueueManager()
    with pytest.raises(ValueError, match="La lista de elementos a producir no puede estar vacía."):
        await manager.producer([])

@pytest.mark.asyncio
async def test_run_pipeline_success():
    manager = AsyncQueueManager(maxsize=5)
    items = ["task_A", "task_B", "task_C", "task_D"]
    pipeline_result = await manager.run_pipeline(items, num_consumers=2)
    
    assert pipeline_result["total_produced"] == 4
    assert pipeline_result["total_consumed"] == 4
    assert pipeline_result["consumers_count"] == 2
    assert len(pipeline_result["results"]) == 4

@pytest.mark.asyncio
async def test_run_pipeline_invalid_consumers():
    manager = AsyncQueueManager()
    with pytest.raises(ValueError, match="El número de consumidores debe ser mayor a cero."):
        await manager.run_pipeline([1, 2], num_consumers=0)

@pytest.mark.asyncio
async def test_run_pipeline_empty_items():
    manager = AsyncQueueManager()
    with pytest.raises(ValueError, match="La lista de elementos a producir no puede estar vacía."):
        await manager.run_pipeline([], num_consumers=2)

@pytest.mark.asyncio
async def test_consumer_timeout_branch():
    manager = AsyncQueueManager(maxsize=2)
    results = []
    stop_event = asyncio.Event()
    
    # Iniciamos el consumidor con la cola vacía para forzar el TimeoutError (líneas 32-33)
    consumer_task = asyncio.create_task(manager.consumer(1, results, stop_event))
    
    # Damos un breve respiro para que entre al bucle y caiga en el timeout de 0.1s
    await asyncio.sleep(0.15)
    
    # Activamos la señal de parada y un elemento para que pueda salir limpiamente
    stop_event.set()
    await manager.queue.put("item_timeout_test")
    
    await consumer_task
    assert len(results) == 1
    assert results[0]["processed_item"] == "item_timeout_test"