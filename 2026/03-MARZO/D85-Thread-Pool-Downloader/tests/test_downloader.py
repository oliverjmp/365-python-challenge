import pytest
from unittest.mock import patch, MagicMock
from src.downloader import ThreadPoolDownloader

@patch("src.downloader.requests.get")
def test_download_success(mock_get):
    """Valida que una descarga exitosa devuelva el estado correcto."""
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b"Mocked data content"
    mock_get.return_value = mock_response

    downloader = ThreadPoolDownloader(max_workers=2)
    urls = ["http://example.com/file1", "http://example.com/file2"]
    results = downloader.download_all(urls)

    assert len(results) == 2
    assert all(res["success"] is True for res in results)
    assert all(res["status_code"] == 200 for res in results)

@patch("src.downloader.requests.get")
def test_download_failure(mock_get):
    """Valida el manejo de errores cuando falla la petición a un recurso."""
    mock_get.side_effect = Exception("Connection error")

    downloader = ThreadPoolDownloader(max_workers=2)
    urls = ["http://example.com/error"]
    results = downloader.download_all(urls)

    assert len(results) == 1
    assert results[0]["success"] is False
    assert results[0]["status_code"] is None
    assert "Connection error" in results[0]["error"]