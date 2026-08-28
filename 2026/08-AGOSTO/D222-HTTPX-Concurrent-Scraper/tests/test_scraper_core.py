import pytest
from unittest.mock import AsyncMock, MagicMock
from src.scraper_core import HTTPXConcurrentScraper

@pytest.mark.asyncio
async def test_fetch_url_success():
    scraper = HTTPXConcurrentScraper()
    mock_client = AsyncMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.is_success = True
    mock_client.get.return_value = mock_response

    result = await scraper.fetch_url(mock_client, "https://example.com")
    assert result["url"] == "https://example.com"
    assert result["status_code"] == 200
    assert result["success"] is True

@pytest.mark.asyncio
async def test_fetch_url_exception():
    scraper = HTTPXConcurrentScraper()
    mock_client = AsyncMock()
    mock_client.get.side_effect = Exception("Connection Timeout")

    result = await scraper.fetch_url(mock_client, "https://unreachable.com")
    assert result["success"] is False
    assert result["status_code"] == 0
    assert "error" in result

@pytest.mark.asyncio
async def test_scrape_batch_empty_list():
    scraper = HTTPXConcurrentScraper()
    with pytest.raises(ValueError, match="La lista de URLs a ingestar no puede estar vacía."):
        await scraper.scrape_batch([])

@pytest.mark.asyncio
async def test_scrape_batch_success(monkeypatch):
    scraper = HTTPXConcurrentScraper()
    
    # Mock para simular el cliente AsyncClient de httpx dentro de scrape_batch
    class MockAsyncClientContext:
        async def __aenter__(self):
            mock_client = AsyncMock()
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.is_success = True
            mock_client.get.return_value = mock_response
            return mock_client
        async def __aexit__(self, exc_type, exc_val, exc_tb):
            pass

    monkeypatch.setattr("httpx.AsyncClient", lambda *args, **kwargs: MockAsyncClientContext())

    summary = await scraper.scrape_batch(["https://example.com"])
    assert summary["total_urls"] == 1
    assert summary["successful_requests"] == 1
    assert summary["failed_requests"] == 0