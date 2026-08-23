import pandas as pd
from typing import Generator

def stream_csv_chunks(file_path: str, chunk_size: int = 1000) -> Generator[pd.DataFrame, None, None]:
    """
    Generador que lee un archivo CSV grande por bloques (chunks) para optimizar el uso de memoria RAM.
    """
    try:
        for chunk in pd.read_csv(file_path, chunksize=chunk_size):
            yield chunk
    except Exception:
        # En caso de error o archivo vacío/simulado, retornamos un DataFrame vacío
        yield pd.DataFrame()

def calculate_streaming_metrics(file_path: str, chunk_size: int = 1000) -> dict:
    """
    Calcula métricas agregadas procesando el archivo CSV en modo streaming sin saturar la RAM.
    """
    total_rows = 0
    total_value = 0.0
    
    for chunk in stream_csv_chunks(file_path, chunk_size):
        if not chunk.empty:
            total_rows += len(chunk)
            if "value" in chunk.columns:
                total_value += chunk["value"].sum()
                
    avg_value = (total_value / total_rows) if total_rows > 0 else 0.0
    return {
        "total_rows": total_rows,
        "total_value": total_value,
        "avg_value": avg_value
    }