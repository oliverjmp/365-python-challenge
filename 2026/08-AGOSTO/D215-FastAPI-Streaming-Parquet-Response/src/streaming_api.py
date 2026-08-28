import os
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import tempfile

app = FastAPI(title="D215 - FastAPI Streaming Parquet Response", version="1.0.0")

# Archivo Parquet temporal simulado para demostración y pruebas
def create_sample_parquet() -> str:
    df = pd.DataFrame({
        "id": range(1, 1001),
        "categoria": ["A", "B", "C", "D"] * 250,
        "valor": [i * 1.5 for i in range(1, 1001)]
    })
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".parquet")
    pq.write_table(pa.Table.from_pandas(df), tmp.name)
    return tmp.name

# Generador por chunks para StreamingResponse
def iter_file(file_path: str, chunk_size: int = 65536):
    with open(file_path, "rb") as f:
        while chunk := f.read(chunk_size):
            yield chunk

@app.get("/download/parquet")
def download_parquet():
    """Endpoint para la descarga optimizada de un fichero Parquet mediante streaming."""
    file_path = create_sample_parquet()
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Fichero Parquet no encontrado.")
    
    return StreamingResponse(
        iter_file(file_path),
        media_type="application/octet-stream",
        headers={"Content-Disposition": "attachment; filename=dataset_exportado.parquet"}
    )