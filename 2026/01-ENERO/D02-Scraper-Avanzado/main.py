import requests
import pandas as pd
import logging
import sys
import random
from pathlib import Path

# ============================================================
# CONFIGURACIÓN DE RUTAS Y LOGGING
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "precios_crypto.csv"
LOG_PATH = BASE_DIR / "crypto_api.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, encoding='utf-8', mode='a'),
        logging.StreamHandler(sys.stdout)
    ]
)

# ============================================================
# 1. EXTRACCIÓN CON REINTENTOS
# ============================================================
def extraer_datos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0",
        "Mozilla/5.0 (X11; Linux x86_64) Firefox/121.0"
    ]
    
    headers = {"User-Agent": random.choice(user_agents)}
    parametros = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    try:
        respuesta = requests.get(url, params=parametros, headers=headers, timeout=15)
        
        # Manejo específico del límite de la API
        if respuesta.status_code == 429:
            logging.error("API Error: Límite de peticiones alcanzado (429). Espera un minuto.")
            return None
            
        respuesta.raise_for_status()
        logging.info("API: Datos de cripto obtenidos con exito.")
        return respuesta.json()
    except Exception as e:
        logging.error(f"Error de conexion API: {e}")
        return None

# ============================================================
# 2. TRANSFORMACIÓN Y CARGA
# ============================================================
def procesar_y_guardar(json_data):
    if not json_data: return False
    
    try:
        datos_limpios = []
        for item in json_data:
            datos_limpios.append({
                "Nombre": item["name"],
                "Precio": item["current_price"], # Guardamos como número para el Excel posterior
                "Cambio_24h": item.get("price_change_percentage_24h", 0),
                "Market_Cap": item.get("market_cap", 0)
            })
        
        df = pd.DataFrame(datos_limpios)
        df.to_csv(CSV_PATH, index=False, encoding='utf-8')
        logging.info(f"CSV: Guardado en {CSV_PATH.name}")
        return True
    except Exception as e:
        logging.error(f"Error procesando DataFrame: {e}")
        return False

# ============================================================
# EJECUCIÓN CON SEÑALIZACIÓN
# ============================================================
if __name__ == "__main__":
    logging.info("=== INICIO D02 ===")
    
    raw = extraer_datos()
    exito = procesar_y_guardar(raw)
    
    if exito:
        logging.info("=== FIN D02 - EXITOSO ===")
        print("D02_STATUS: SUCCESS", flush=True)
        sys.exit(0) # <--- SEÑAL PARA EL ORQUESTADOR
    else:
        logging.error("=== FIN D02 - FALLIDO ===")
        print("D02_STATUS: FAILED", flush=True)
        sys.exit(1)
