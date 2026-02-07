"""
Proyecto: 365 Python Challenge
Día 50: Image Batch Downloader
Objetivo: Descargar automáticamente imágenes de una web y guardarlas localmente.
"""

import requests
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin
import sys

class ImageDownloader:
    def __init__(self, url):
        self.url = url
        # Definimos la ruta absoluta basada en la ubicación del script
        self.base_dir = Path(__file__).parent.absolute()
        self.download_path = self.base_dir / "Descargas_D50"
        self.download_path.mkdir(exist_ok=True)
        
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) OliverBot/2.0"
        }

    def run(self, max_files=5):
        print(f"\n" + "═"*50)
        print(f"🔥 HITO D50: INICIANDO DESCARGA MASIVA")
        print(f"🌐 Fuente: {self.url}")
        print("═"*50)

        try:
            response = requests.get(self.url, headers=self.headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontrar todas las etiquetas de imagen
            images = soup.find_all('img')
            print(f"🔍 Se detectaron {len(images)} imágenes potenciales.")

            count = 0
            for img in images:
                if count >= max_files:
                    break
                
                img_url = img.get('src')
                if not img_url:
                    continue

                # Convertir ruta relativa a absoluta
                full_url = urljoin(self.url, img_url)
                
                # Filtrar solo formatos de imagen comunes
                if any(ext in full_url.lower() for ext in ['.jpg', '.jpeg', '.png', '.webp', '.svg']):
                    if self.download_image(full_url, count):
                        count += 1

            print(f"\n✅ Proceso terminado. {count} imágenes en /Descargas_D50")

        except Exception as e:
            print(f"❌ Error en el orquestador: {e}")

    def download_image(self, url, index):
        try:
            # Extraer extensión limpia (evitando parámetros como ?width=200)
            ext = url.split('.')[-1].split('?')[0]
            if len(ext) > 4: ext = "jpg" # Fallback si la extensión es rara
            
            filename = f"asset_{index + 1}.{ext}"
            file_path = self.download_path / filename

            # Descarga binaria con Stream
            with requests.get(url, headers=self.headers, stream=True) as r:
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    # Escribimos el contenido en bloques (chunks) para ser eficientes
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            
            print(f"   📥 Guardado: {filename}")
            return True
        except Exception as e:
            print(f"   ⚠️ Fallo al descargar {url}: {e}")
            return False

if __name__ == "__main__":
    # Probamos con Wikipedia (página principal tiene iconos y fotos)
    target_site = "https://es.wikipedia.org/wiki/Wikipedia:Portada"
    
    bot = ImageDownloader(target_site)
    bot.run(max_files=10)