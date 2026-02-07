import requests
import sqlite3
import logging

# ============================================================
# CONFIGURACIÓN DE LOGGING
# ============================================================
logging.basicConfig(
    filename="etl_clima.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("=== INICIO DEL PIPELINE ETL ===")

# ============================================================
# 1. EXTRACCIÓN DE DATOS DESDE API
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
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        logging.info("Datos extraídos correctamente desde la API.")
        return respuesta.json()
    except Exception as e:
        logging.error(f"Error en la extracción: {e}")
        return None

# ============================================================
# 2. TRANSFORMACIÓN DE DATOS
# ============================================================

def transformar_datos(json_data, ciudad):
    try:
        horas = json_data["hourly"]["time"]
        temperaturas = json_data["hourly"]["temperature_2m"]
        humedades = json_data["hourly"]["relativehumidity_2m"]
        vientos = json_data["hourly"]["windspeed_10m"]

        registros = []
        for i in range(len(horas)):
            registros.append((
                horas[i],
                temperaturas[i],
                vientos[i],
                humedades[i],
                ciudad
            ))

        logging.info("Transformación completada.")
        return registros

    except Exception as e:
        logging.error(f"Error en la transformación: {e}")
        return []

# ============================================================
# 3. CARGA EN BASE DE DATOS SQLITE
# ============================================================

def cargar_datos(registros):
    try:
        conn = sqlite3.connect("clima.db")
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS weather_data (
                fecha TEXT,
                temperatura REAL,
                viento REAL,
                humedad REAL,
                ciudad TEXT
            )
        """)

        cursor.executemany("""
            INSERT INTO weather_data (fecha, temperatura, viento, humedad, ciudad)
            VALUES (?, ?, ?, ?, ?)
        """, registros)

        conn.commit()
        conn.close()

        logging.info("Datos cargados correctamente en SQLite.")

    except Exception as e:
        logging.error(f"Error en la carga: {e}")

# ============================================================
# 4. MOSTRAR PRONÓSTICO DE 5 DÍAS (MÁX Y MÍN)
# ============================================================

def mostrar_pronostico_5_dias(json_data, ciudad):
    print(f"\nPronóstico para {ciudad} (próximos 5 días):")
    print("-----------------------------------------")

    fechas = json_data["daily"]["time"]
    maximas = json_data["daily"]["temperature_2m_max"]
    minimas = json_data["daily"]["temperature_2m_min"]

    for i in range(5):
        print(f"{fechas[i]} → Máx: {maximas[i]}°C | Mín: {minimas[i]}°C")

# ============================================================
# EJECUCIÓN DEL PIPELINE
# ============================================================

if __name__ == "__main__":
    ciudad = "Alcobendas"
    lat, lon = 40.4168, -3.7038

    datos = extraer_datos(lat, lon)

    if datos:
        registros = transformar_datos(datos, ciudad)
        cargar_datos(registros)
        mostrar_pronostico_5_dias(datos, ciudad)

    logging.info("=== FIN DEL PIPELINE ETL ===")
    print("Pipeline ETL completado correctamente.")
