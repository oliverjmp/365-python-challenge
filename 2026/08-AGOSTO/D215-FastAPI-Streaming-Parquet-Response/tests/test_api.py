from fastapi.testclient import TestClient
from src.streaming_api import app, create_sample_parquet
import os
from unittest.mock import patch

client = TestClient(app)

def test_download_parquet_endpoint():
    response = client.get("/download/parquet")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/octet-stream"
    assert "attachment; filename=dataset_exportado.parquet" in response.headers["content-disposition"]
    assert len(response.content) > 0

def test_create_sample_parquet():
    path = create_sample_parquet()
    assert os.path.exists(path)
    os.unlink(path)

def test_download_parquet_not_found():
    with patch("src.streaming_api.create_sample_parquet", return_value="archivo_inexistente.parquet"):
        response = client.get("/download/parquet")
        assert response.status_code == 404
        assert response.json() == {"detail": "Fichero Parquet no encontrado."}