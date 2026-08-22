import pytest
from src.batch_processor import AsyncBatchPredictionProcessor, cpu_heavy_predict

def test_cpu_heavy_predict_direct():
    """Valida la función de cálculo pesado aislada."""
    data = [[1.0, 2.0], [3.0, 4.0]]
    res = cpu_heavy_predict(data)
    assert res == [4.5, 10.5]

def test_invalid_batch_size_raises_error():
    """Valida que un batch_size menor o igual a cero lance ValueError."""
    with pytest.raises(ValueError, match="debe ser mayor a cero"):
        AsyncBatchPredictionProcessor(batch_size=0)

@pytest.mark.asyncio
async def test_process_batch_empty_raises_error():
    """Valida que procesar una lista vacía lance un ValueError."""
    processor = AsyncBatchPredictionProcessor(batch_size=2)
    with pytest.raises(ValueError, match="no puede estar vacía"):
        await processor.process_batch_async([])

@pytest.mark.asyncio
async def test_process_batch_success():
    """Valida el procesamiento asíncrono exitoso con múltiples lotes."""
    processor = AsyncBatchPredictionProcessor(batch_size=2)
    input_data = [
        [1.0, 1.0],
        [2.0, 2.0],
        [3.0, 3.0],
        [4.0, 4.0],
        [5.0, 5.0]
    ]
    
    predictions = await processor.process_batch_async(input_data)
    
    assert isinstance(predictions, list)
    assert len(predictions) == 5
    # [1+1]*1.5 = 3.0, [2+2]*1.5 = 6.0, etc.
    assert predictions == [3.0, 6.0, 9.0, 12.0, 15.0]