import pytest
import pandas as pd
from src.table_scraper import DynamicTableScraper

def test_scrape_table_success():
    """Valida la extracción exitosa de una tabla."""
    html = "<table id='data-table'><tr><th>Nombre</th><th>Edad</th></tr><tr><td>Oliver</td><td>30</td></tr></table>"
    scraper = DynamicTableScraper(html)
    df = scraper.scrape_table(table_id='data-table')
    assert not df.empty
    assert df.iloc[0]['Nombre'] == 'Oliver'
    assert int(df.iloc[0]['Edad']) == 30

def test_scrape_table_not_found():
    """Valida el comportamiento cuando no se encuentra la tabla."""
    scraper = DynamicTableScraper("<html></html>")
    df = scraper.scrape_table(table_id='fake')
    assert df.empty
    
def test_scrape_table_exception(monkeypatch):
    """Fuerza una excepción para cubrir el bloque de error."""
    scraper = DynamicTableScraper("<table id='data-table'><tr><td>Data</td></tr></table>")
    
    # Forzamos un error haciendo que find_all lance una excepción dentro del try
    def mock_find_all(*args, **kwargs):
        raise Exception("Error forzado para cobertura")

    monkeypatch.setattr("bs4.BeautifulSoup.find_all", mock_find_all)
    
    # Esto activará el bloque except Exception: garantizando el 100% de cobertura
    df = scraper.scrape_table(table_id='data-table')
    assert df.empty