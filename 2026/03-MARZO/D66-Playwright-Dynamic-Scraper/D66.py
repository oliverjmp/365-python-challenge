"""
Día 66 — Playwright Dynamic Scraper
====================================
Pipeline de extracción de datos para páginas renderizadas dinámicamente
vía JavaScript (SPA), donde `requests` + `BeautifulSoup` no funcionan
porque el HTML inicial no contiene los datos objetivo.

Arquitectura:
    - MockCatalogServer: levanta un servidor HTTP local en un hilo daemon,
      sirviendo una página de catálogo cuyo contenido se inyecta vía JS
      tras un delay (simulando una llamada a API asíncrona real).
    - DynamicCatalogScraper: usa Playwright (Chromium headless) para
      navegar, esperar explícitamente al selector dinámico y extraer
      los datos estructurados del DOM ya renderizado.

Nota de diseño: se usa un mock server local en vez de un sitio público
real para que el proyecto sea 100% reproducible y no dependa de que un
tercero cambie su HTML/estructura con el tiempo.
"""

from __future__ import annotations

import functools
import http.server
import json
import logging
import socket
import threading
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Generator, List, Optional

from playwright.sync_api import (
    Browser,
    Page,
    TimeoutError as PlaywrightTimeoutError,
    sync_playwright,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s",
)
logger = logging.getLogger("D66-Dynamic-Scraper")

MOCK_SITE_DIR = Path(__file__).resolve().parent / "mock_site"
OUTPUT_PATH = Path(__file__).resolve().parent / "scraped_products.json"

DYNAMIC_LOAD_TIMEOUT_MS = 8_000
PRODUCT_CARD_SELECTOR = ".product-card"


@dataclass(frozen=True)
class ScrapedProduct:
    """Registro tipado de un producto extraído del catálogo dinámico."""

    sku: str
    name: str
    price: float
    in_stock: bool


class MockCatalogServer:
    """Servidor HTTP local que sirve el catálogo mock para pruebas deterministas.

    Se ejecuta en un hilo daemon para que el proceso principal no quede
    bloqueado y el servidor se cierre automáticamente al finalizar el script.
    """

    def __init__(self, directory: Path) -> None:
        self._directory = directory
        self._httpd: Optional[http.server.ThreadingHTTPServer] = None
        self._thread: Optional[threading.Thread] = None
        self.port: int = self._find_free_port()

    @staticmethod
    def _find_free_port() -> int:
        """Reserva un puerto libre del sistema operativo para evitar colisiones."""
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(("127.0.0.1", 0))
            return s.getsockname()[1]

    def start(self) -> str:
        """Arranca el servidor y devuelve la URL base."""
        handler = functools.partial(
            http.server.SimpleHTTPRequestHandler, directory=str(self._directory)
        )
        self._httpd = http.server.ThreadingHTTPServer(("127.0.0.1", self.port), handler)
        self._thread = threading.Thread(target=self._httpd.serve_forever, daemon=True)
        self._thread.start()

        base_url = f"http://127.0.0.1:{self.port}"
        logger.info(f"Mock catalog server activo en: {base_url}")
        return base_url

    def stop(self) -> None:
        """Detiene el servidor de forma ordenada."""
        if self._httpd is not None:
            self._httpd.shutdown()
            self._httpd.server_close()
            logger.info("Mock catalog server detenido correctamente.")


class DynamicCatalogScraper:
    """Extrae el catálogo de productos de una página renderizada vía JavaScript."""

    def __init__(self, browser: Browser) -> None:
        self._browser = browser

    def scrape(self, url: str) -> List[ScrapedProduct]:
        """Navega a `url`, espera el render dinámico y extrae los productos.

        Raises:
            PlaywrightTimeoutError: si el catálogo no termina de renderizarse
                dentro del tiempo límite configurado.
        """
        page: Page = self._browser.new_page()
        products: List[ScrapedProduct] = []

        try:
            logger.info(f"Navegando a: {url}")
            page.goto(url, wait_until="domcontentloaded")

            # Espera explícita al selector inyectado por JS — NUNCA usar
            # time.sleep() fijo en scraping dinámico: es frágil y lento.
            logger.info("Esperando renderizado asíncrono del catálogo...")
            page.wait_for_selector(
                PRODUCT_CARD_SELECTOR, timeout=DYNAMIC_LOAD_TIMEOUT_MS
            )
            page.wait_for_selector(
                'body[data-catalog-ready="true"]', timeout=DYNAMIC_LOAD_TIMEOUT_MS
            )

            cards = page.query_selector_all(PRODUCT_CARD_SELECTOR)
            logger.info(f"Catálogo renderizado. {len(cards)} tarjetas de producto detectadas.")

            for card in cards:
                sku = card.get_attribute("data-sku") or "N/A"
                name_el = card.query_selector(".product-name")
                price_el = card.query_selector(".product-price")
                stock_el = card.query_selector(".product-stock")

                name = name_el.inner_text().strip() if name_el else "N/A"
                price_raw = price_el.get_attribute("data-price") if price_el else "0"
                in_stock = bool(
                    stock_el and "in-stock" in (stock_el.get_attribute("class") or "")
                )

                products.append(
                    ScrapedProduct(
                        sku=sku,
                        name=name,
                        price=float(price_raw),
                        in_stock=in_stock,
                    )
                )

        except PlaywrightTimeoutError as e:
            logger.error(f"Timeout esperando el renderizado dinámico: {e}")
            raise
        finally:
            page.close()

        return products


@contextmanager
def playwright_browser() -> Generator[Browser, None, None]:
    """Context manager que garantiza el cierre del browser y de Playwright."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            yield browser
        finally:
            browser.close()


def export_results(products: List[ScrapedProduct], elapsed_seconds: float) -> None:
    """Serializa los resultados del scraping a un artefacto JSON con metadata."""
    report = {
        "execution_time_seconds": round(elapsed_seconds, 4),
        "total_products_scraped": len(products),
        "in_stock_count": sum(1 for p in products if p.in_stock),
        "out_of_stock_count": sum(1 for p in products if not p.in_stock),
        "products": [asdict(p) for p in products],
    }
    OUTPUT_PATH.write_text(json.dumps(report, indent=4, ensure_ascii=False), encoding="utf-8")
    logger.info(f"[SUCCESS] Artefacto exportado en: {OUTPUT_PATH}")


def main() -> None:
    """Orquesta el ciclo completo: levantar mock server, scrapear, exportar."""
    logger.info("=== [D66] INICIANDO DYNAMIC SCRAPER CON PLAYWRIGHT ===")

    mock_server = MockCatalogServer(MOCK_SITE_DIR)

    try:
        base_url = mock_server.start()
        target_url = f"{base_url}/index.html"

        start_time = time.perf_counter()

        with playwright_browser() as browser:
            scraper = DynamicCatalogScraper(browser)
            products = scraper.scrape(target_url)

        elapsed = time.perf_counter() - start_time

        export_results(products, elapsed)

        print(f"\n[ÉXITO] Scraping completado en {elapsed:.2f}s")
        print(f"Productos extraídos: {len(products)}")
        for p in products:
            stock_label = "En stock" if p.in_stock else "Agotado"
            print(f"  - [{p.sku}] {p.name} | €{p.price:.2f} | {stock_label}")

    except PlaywrightTimeoutError:
        logger.error("[ERROR CRÍTICO] El catálogo dinámico no se renderizó a tiempo.")
        raise
    except Exception as e:
        logger.error(f"[ERROR CRÍTICO] Falló la ejecución del scraper: {e}", exc_info=True)
        raise
    finally:
        mock_server.stop()
        logger.info("=== [D66] PIPELINE FINALIZADO ===")


if __name__ == "__main__":
    main()