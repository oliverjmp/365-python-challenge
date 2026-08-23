import pandas as pd
import os
from src.streamer import stream_csv_chunks, calculate_streaming_metrics

def test_stream_and_metrics():
    test_file = "test_stream.csv"
    df = pd.DataFrame({
        "id": [1, 2, 3],
        "value": [10.0, 20.0, 30.0]
    })
    df.to_csv(test_file, index=False)
    
    try:
        chunks = list(stream_csv_chunks(test_file, chunk_size=2))
        assert len(chunks) == 2 # 3 filas con chunk_size=2 generan 2 bloques
        
        metrics = calculate_streaming_metrics(test_file, chunk_size=2)
        assert metrics["total_rows"] == 3
        assert metrics["total_value"] == 60.0
        assert metrics["avg_value"] == 20.0
    finally:
        if os.path.exists(test_file):
            os.remove(test_file)

from src.streamer import stream_csv_chunks, calculate_streaming_metrics

def test_stream_exception_handling():
    # Forzamos un error pasando un archivo que no existe
    chunks = list(stream_csv_chunks("archivo_inexistente_12345.csv"))
    assert len(chunks) == 1
    assert chunks[0].empty

    metrics = calculate_streaming_metrics("archivo_inexistente_12345.csv")
    assert metrics["total_rows"] == 0
    assert metrics["total_value"] == 0.0
    assert metrics["avg_value"] == 0.0