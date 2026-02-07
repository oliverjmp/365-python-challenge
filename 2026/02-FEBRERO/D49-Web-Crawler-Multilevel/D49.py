"""
Proyecto: 365 Python Challenge
Día 49: Multilevel Web Crawler
Objetivo: Navegar de una lista principal a páginas individuales para extraer info profunda.
"""

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

class WebCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OliverBot/1.0"}
        self.results = []

    def crawl(self, limit=5):
        print(f"🚀 Iniciando Crawler en: {self.base_url}")
        
        try:
            response = requests.get(self.base_url, headers=self.headers)
            soup = BeautifulSoup(response.text, 'lxml')

            # 1. Descubrimiento: Buscamos enlaces a artículos (en este caso de Wikipedia)
            # Buscamos enlaces dentro de la tabla que procesamos ayer
            links = soup.find_all('a', href=True)
            
            valid_links = []
            for link in links:
                href = link['href']
                # Solo queremos enlaces a países (que empiezan con /wiki/ y no tienen ':' )
                if href.startswith('/wiki/') and ':' not in href:
                    full_url = urljoin(self.base_url, href)
                    if full_url not in valid_links:
                        valid_links.append(full_url)
            
            print(f"🔗 Se encontraron {len(valid_links)} enlaces potenciales. Procesando los primeros {limit}...")

            # 2. Navegación Profunda
            for i, url in enumerate(valid_links[:limit]):
                print(f"   📥 [{i+1}/{limit}] Entrando a: {url.split('/')[-1]}...")
                
                self.extract_deep_data(url)
                
                # REGLA DE ORO: Pausa de cortesía para no ser bloqueados
                time.sleep(1) 

        except Exception as e:
            print(f"❌ Error en el crawler: {e}")

    def extract_deep_data(self, url):
        """Entra en la subpágina y extrae un dato específico (ej. el primer párrafo)."""
        try:
            res = requests.get(url, headers=self.headers)
            sub_soup = BeautifulSoup(res.text, 'lxml')
            
            title = sub_soup.find('h1').get_text()
            # Buscamos el primer párrafo real que no esté vacío
            paragraphs = sub_soup.find_all('p')
            summary = "Sin resumen"
            for p in paragraphs:
                if len(p.get_text().strip()) > 50:
                    summary = p.get_text().strip()[:100] + "..."
                    break
            
            self.results.append({"titulo": title, "resumen": summary})
            print(f"      ✅ Extraído: {title}")
            
        except Exception as e:
            print(f"      ⚠️ Error extrayendo de {url}: {e}")

    def show_results(self):
        print("\n" + "═"*50)
        print("📊 RESUMEN DE RECOLECCIÓN PROFUNDA")
        print("═"*50)
        for item in self.results:
            print(f"📍 {item['titulo']}\n   📝 {item['resumen']}\n")

if __name__ == "__main__":
    # URL de inicio: Países por población
    start_url = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    
    bot = WebCrawler(start_url)
    bot.crawl(limit=3) # Limitamos a 3 para la prueba rápida
    bot.show_results()