import pytest
from pathlib import Path
import respx
import httpx
from httpx import Response
from src.uploader import AsyncFileUploader

@pytest.mark.asyncio
@respx.mock
async def test_upload_single_file_success(tmp_path):
    """Valida la subida exitosa de un archivo mediante peticiones asíncronas simuladas."""
    file_path = tmp_path / "sample.bin"
    file_path.write_bytes(b"content data simulation")

    target_url = "https://api.remoteserver.com/upload"
    respx.post(target_url).mock(return_value=Response(200, json={"message": "Uploaded"}))

    uploader = AsyncFileUploader(target_url=target_url)
    async with httpx.AsyncClient() as client:
        result = await uploader.upload_single_file(client, file_path)

    assert result["status"] == "success"
    assert result["file"] == "sample.bin"

@pytest.mark.asyncio
@respx.mock
async def test_upload_single_file_server_error(tmp_path):
    """Valida el manejo cuando el servidor responde con un código de error (ej. 500)."""
    file_path = tmp_path / "sample.bin"
    file_path.write_bytes(b"content data simulation")

    target_url = "https://api.remoteserver.com/upload"
    respx.post(target_url).mock(return_value=Response(500, json={"error": "Server Error"}))

    uploader = AsyncFileUploader(target_url=target_url)
    async with httpx.AsyncClient() as client:
        result = await uploader.upload_single_file(client, file_path)

    assert result["status"] == "failed"
    assert result["status_code"] == 500

@pytest.mark.asyncio
async def test_upload_single_file_exception_handling(tmp_path, monkeypatch):
    """Fuerza y valida la captura de excepciones generales (bloque except Exception)."""
    file_path = tmp_path / "sample.bin"
    file_path.write_bytes(b"content data simulation")

    class FaultyClient:
        async def post(self, *args, **kwargs):
            raise RuntimeError("Network failure simulated")

    uploader = AsyncFileUploader(target_url="https://api.remoteserver.com/upload")
    # Forzamos un cliente que arroje una excepción directa para cubrir las líneas del except
    result = await uploader.upload_single_file(FaultyClient(), file_path)

    assert result["status"] == "failed"
    assert "Network failure simulated" in result["error"]

@pytest.mark.asyncio
async def test_upload_file_not_found():
    """Valida el manejo de error cuando el fichero local no existe."""
    uploader = AsyncFileUploader(target_url="https://api.remoteserver.com/upload")
    async with httpx.AsyncClient() as client:
        result = await uploader.upload_single_file(client, Path("nonexistent_file.bin"))

    assert result["status"] == "failed"
    assert "error" in result

@pytest.mark.asyncio
@respx.mock
async def test_upload_batch_concurrent(tmp_path):
    """Valida la transferencia concurrente de múltiples ficheros."""
    f1 = tmp_path / "file1.bin"
    f2 = tmp_path / "file2.bin"
    f1.write_bytes(b"data1")
    f2.write_bytes(b"data2")

    target_url = "https://api.remoteserver.com/upload"
    respx.post(target_url).mock(return_value=Response(200, json={"status": "ok"}))

    uploader = AsyncFileUploader(target_url=target_url)
    results = await uploader.upload_batch([f1, f2])

    assert len(results) == 2
    assert all(res["status"] == "success" for res in results)