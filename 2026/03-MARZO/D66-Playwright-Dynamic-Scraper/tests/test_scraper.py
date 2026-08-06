"""
Tests de integración para el pipeline de scraping dinámico D66.

Requiere que los browsers de Playwright estén instalados:
    playwright install chromium

Nota: son tests de integración reales (levantan un servidor HTTP local
y un browser Chromium headless), no mocks de Playwright — validan el
comportamiento end-to-end del scraper contra el catálogo dinámico real.
"""

import sys
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

# Permite importar D66.py como módulo desde el directorio padre
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from D66 import (  # noqa: E402
    DynamicCatalogScraper,
    MockCatalogServer,
    MOCK_SITE_DIR,
    ScrapedProduct,
)


@pytest.fixture(scope="module")
def running_mock_server():
    """Levanta el servidor mock una vez para todo el módulo de tests."""
    server = MockCatalogServer(MOCK_SITE_DIR)
    base_url = server.start()
    yield base_url
    server.stop()


@pytest.fixture(scope="module")
def browser():
    """Browser Chromium headless compartido entre tests del módulo."""
    with sync_playwright() as p:
        b = p.chromium.launch(headless=True)
        yield b
        b.close()


def test_mock_server_starts_and_serves_html(running_mock_server):
    """El servidor mock debe levantar y exponer una URL HTTP válida."""
    assert running_mock_server.startswith("http://127.0.0.1:")


def test_scraper_extracts_all_products(running_mock_server, browser):
    """El scraper debe extraer exactamente los 6 productos del catálogo mock."""
    scraper = DynamicCatalogScraper(browser)
    products = scraper.scrape(f"{running_mock_server}/index.html")

    assert len(products) == 6
    assert all(isinstance(p, ScrapedProduct) for p in products)


def test_scraper_extracts_correct_fields(running_mock_server, browser):
    """Valida que el primer producto tenga los campos exactos esperados."""
    scraper = DynamicCatalogScraper(browser)
    products = scraper.scrape(f"{running_mock_server}/index.html")

    first = next(p for p in products if p.sku == "ENT-1001")
    assert first.name == "Servidor Rack ProLine X200"
    assert first.price == pytest.approx(4899.00)
    assert first.in_stock is True


def test_scraper_detects_out_of_stock_items(running_mock_server, browser):
    """Valida que el scraper distinga correctamente productos agotados."""
    scraper = DynamicCatalogScraper(browser)
    products = scraper.scrape(f"{running_mock_server}/index.html")

    out_of_stock_skus = {p.sku for p in products if not p.in_stock}
    assert out_of_stock_skus == {"ENT-1003", "ENT-1006"}