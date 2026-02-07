"""
Proyecto: 365 Python Challenge
Día 48: Table Scraper to CSV
Objetivo: Extraer una tabla HTML y guardarla en un archivo CSV profesional.
"""

import requests
import csv
from bs4 import BeautifulSoup
from pathlib import Path

class TableScraper:
    def __init__(self, url):
        self.url = url
        self.output_path = Path(__file__).parent / "datos_extraidos.csv"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    def get_table_data(self):
        print(f"📡 Conectando con la fuente de datos...")
        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'lxml')

            # Localizar la tabla (en este caso buscamos la primera que aparezca)
            table = soup.find('table')
            if not table:
                print("❌ No se encontró ninguna tabla en esta URL.")
                return

            dataset = []
            
            # 1. Extraer cabeceras (th)
            headers = [th.get_text().strip() for th in table.find_all('th')]
            if not headers:
                # Si no hay <th>, intentamos con la primera fila
                first_row = table.find('tr')
                headers = [td.get_text().strip() for td in first_row.find_all('td')]
            
            # 2. Extraer filas de datos (tr)
            # Ignoramos la primera fila si ya la usamos para cabeceras
            rows = table.find_all('tr')[1:] 
            
            for row in rows:
                cells = row.find_all('td')
                if cells:
                    # Limpiamos el texto de cada celda
                    clean_row = [cell.get_text().strip() for cell in cells]
                    dataset.append(clean_row)

            self.save_to_csv(headers, dataset)

        except Exception as e:
            print(f"❌ Error durante el scraping: {e}")

    def save_to_csv(self, headers, data):
        try:
            with open(self.output_path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(data)
            print(f"✅ Éxito: {len(data)} filas guardadas en '{self.output_path.name}'")
        except Exception as e:
            print(f"❌ Error al guardar CSV: {e}")

if __name__ == "__main__":
    # Usaremos una URL de Wikipedia que contiene tablas de ejemplo
    # (Lista de países por población, por ejemplo)
    target = "https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)"
    
    scraper = TableScraper(target)
    scraper.get_table_data()