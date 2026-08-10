import pytest
import pandas as pd
from src.table_scraper import DynamicTableScraper

def test_scrape_table_success():
    html = "<table id='data-table'><tr><th>Nombre</th><th>Edad</th></tr><tr><td>Oliver</td><td>30</td></tr></table>"
    scraper = DynamicTableScraper(html)
    df = scraper.scrape_table(table_id='data-table')
    assert not df.empty
    assert df.iloc[0]['Nombre'] == 'Oliver'
    assert int(df.iloc[0]['Edad']) == 30

def test_scrape_table_not_found():
    scraper = DynamicTableScraper("<html></html>")
    df = scraper.scrape_table(table_id='fake')
    assert df.empty

def test_scrape_table_exception(monkeypatch):
    scraper = DynamicTableScraper("<table id='data-table'></table>")
    # Forzamos un error en el método find de BeautifulSoup
    monkeypatch.setattr("bs4.element.Tag.find_all", lambda *a, **kw: (_ for _ in ()).throw(ValueError("Simulado")))
    df = scraper.scrape_table(table_id='data-table')
    assert df.empty

def test_scrape_table_exception(monkeypatch):
    """Fuerza una excepción para cubrir el bloque de error."""
    # Instanciamos con HTML válido para pasar el primer filtro
    scraper = DynamicTableScraper("<table><tr><td>Data</td></tr></table>")
    
    # Inyectamos el error en find_all, que se ejecuta DENTRO del bloque try
    def mock_find_all(*args, **kwargs):
        raise Exception("Error forzado")

    monkeypatch.setattr("bs4.element.Tag.find_all", mock_find_all)
    
    # Esto activará el 'except Exception:' en la línea 27
    df = scraper.scrape_table()
    assert df.empty