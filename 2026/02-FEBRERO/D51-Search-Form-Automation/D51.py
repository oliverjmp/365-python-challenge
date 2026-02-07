"""
Proyecto: 365 Python Challenge
Día 51: Search Form Automation
Objetivo: Automatizar una búsqueda en Wikipedia y extraer los enlaces de los resultados.
"""

import requests
from bs4 import BeautifulSoup

class SearchBot:
    def __init__(self):
        # La URL base donde Wikipedia procesa las búsquedas
        self.url = "https://es.wikipedia.org/w/index.php"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OliverSearchBot/1.0"
        }

    def search(self, query):
        print(f"\n🔍 Iniciando búsqueda automatizada para: '{query}'")
        
        # Parámetros que el formulario de Wikipedia espera (se ven en la URL al buscar manualmente)
        payload = {
            'search': query,
            'title': 'Especial:Buscar',
            'profile': 'advanced',
            'fulltext': '1'
        }

        try:
            # Enviamos la petición con los parámetros (params)
            response = requests.get(self.url, params=payload, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Verificamos la URL final construida por requests
            print(f"📡 URL generada: {response.url}\n")

            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Buscamos los contenedores de los títulos de resultados
            # En Wikipedia actual, los títulos están en divs con esta clase:
            results = soup.select('.mw-search-result-heading')

            if not results:
                print("⚠️ No se encontraron resultados para esa consulta.")
                return

            print(f"✨ Se han encontrado {len(results)} coincidencias:")
            for i, res in enumerate(results, 1):
                link_tag = res.find('a')
                if link_tag:
                    title = link_tag.get_text()
                    # Reconstruimos la URL absoluta
                    link_url = "https://es.wikipedia.org" + link_tag.get('href')
                    print(f"   [{i}] {title}")
                    print(f"       🔗 {link_url}")

        except Exception as e:
            print(f"❌ Error en la conexión: {e}")

if __name__ == "__main__":
    bot = SearchBot()
    
    # Prueba el bot con cualquier tema
    bot.search("Python (lenguaje de programación)")