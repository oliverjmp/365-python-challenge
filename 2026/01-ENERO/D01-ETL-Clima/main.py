import requests
import sqlite3
import logging
import sys
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE RUTAS DINÁMICAS (Best Practice)
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "clima.db"
LOG_PATH = BASE_DIR / "etl_clima.log"

# ============================================================
# CONFIGURACIÓN DE LOGGING (Optimizado para Orquestador)
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding='utf-8', mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

# ============================================================
# 1. EXTRACCIÓN DE DATOS
# ============================================================
def extraer_datos(lat, lon):
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            "&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
            "&daily=temperature_2m_max,temperature_2m_min"
            "&timezone=auto"
        )
        respuesta = requests.get(url, timeout=15)
        respuesta.raise_for_status()
        logging.info("API: Extraccion exitosa.")
        return respuesta.json()
    except Exception as e:
        logging.error(f"API Error: {e}")
        return None

# ============================================================
# 2. TRANSFORMACIÓN
# ============================================================
def transformar_datos(json_data, ciudad):
    try:
        h = json_data["hourly"]
        registros = [
            (h["time"][i], h["temperature_2m"][i], h["windspeed_10m"][i], h["relativehumidity_2m"][i], ciudad) 
            for i in range(len(h["time"]))
        ]
        logging.info(f"Transformacion: {len(registros)} registros listos.")
        return registros
    except KeyError as e:
        logging.error(f"Data Error: Llave faltante {e}")
        return []

# ============================================================
# 3. CARGA (Persistence)
# ============================================================
def cargar_datos(registros):
    if not registros: return
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS weather_data") # Limpieza para test fresh
            cursor.execute("""
                CREATE TABLE weather_data (
                    fecha TEXT, temperatura REAL, viento REAL, humedad REAL, ciudad TEXT
                )
            """)
            cursor.executemany("INSERT INTO weather_data VALUES (?, ?, ?, ?, ?)", registros)
        logging.info(f"Carga: OK en {DB_PATH.name}")
    except Exception as e:
        logging.error(f"DB Error: {e}")

# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================
if __name__ == "__main__":
    logging.info("=== INICIO D01 ===")
    
    # Coordenadas Alcobendas
    lat, lon = 40.5475, -3.6421
    
    raw_data = extraer_datos(lat, lon)
    
    if raw_data:
        datos_procesados = transformar_datos(raw_data, "Alcobendas")
        cargar_datos(datos_procesados)
        
        logging.info("=== FIN D01 - EXITOSO ===")
        print("D01_STATUS: SUCCESS", flush=True)
        
        # EL PASO MÁS IMPORTANTE PARA EL ORQUESTADOR:
        sys.exit(0) 
    else:
        logging.error("=== FIN D01 - FALLIDO ===")
        print("D01_STATUS: FAILED", flush=True)
        sys.exit(1)
