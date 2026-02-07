"""
Proyecto: 365 Python Challenge
Día 47: Web Scraping Foundations
Objetivo: Extraer el título y los enlaces de una página web real.
"""

import requests
from bs4 import BeautifulSoup
import sys
from pathlib import Path

class WebScraper:
    def __init__(self, url):
        self.url = url
        # Definimos 'headers' para parecer un navegador real y no un bot simple
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

    def fetch_data(self):
        try:
            print(f"📡 Enviando petición a: {self.url}...")
            response = requests.get(self.url, headers=self.headers, timeout=10)
            
            # Verificar si la petición fue exitosa (Status Code 200)
            response.raise_for_status()
            
            return response.text
        except requests.exceptions.HTTPError as e:
            print(f"❌ Error HTTP: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
        return None

    def parse_html(self, html_content):
        if not html_content:
            return

        # Creamos la 'Sopa' (objeto BeautifulSoup)
        soup = BeautifulSoup(html_content, 'lxml')

        # 1. Extraer el título de la página
        title = soup.title.string if soup.title else "Sin título"
        print(f"\n📌 Título de la web: {title}")

        # 2. Extraer el primer H1 (Encabezado principal)
        h1 = soup.find('h1')
        if h1:
            print(f"📝 Encabezado principal: {h1.get_text().strip()}")

        # 3. Extraer todos los enlaces (etiquetas <a>)
        print("\n🔗 Algunos enlaces encontrados:")
        links = soup.find_all('a', limit=5) # Limitamos a 5 para no saturar la consola
        for link in links:
            href = link.get('href')
            text = link.get_text().strip()
            if href and text:
                print(f"   - {text}: {href}")

if __name__ == "__main__":
    # Usaremos una página de ejemplo diseñada para scraping
    target_url = "https://example.com"
    
    scraper = WebScraper(target_url)
    raw_html = scraper.fetch_data()
    scraper.parse_html(raw_html)

    print("\n" + "═"*40)
    print("✨ Scraping inicial completado con éxito.")
    print("═"*40)