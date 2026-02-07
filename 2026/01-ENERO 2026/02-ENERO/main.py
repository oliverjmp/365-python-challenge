import requests
import pandas as pd

# ============================================================
# 1. EXTRACCIÓN DESDE LA API OFICIAL DE COINGECKO
# ============================================================

def extraer_datos():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parametros = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    respuesta = requests.get(url, params=parametros)
    respuesta.raise_for_status()
    return respuesta.json()

# ============================================================
# 2. TRANSFORMACIÓN DE DATOS
# ============================================================

def transformar_datos(json_data):
    datos_limpios = []

    for item in json_data:
        nombre = item["name"]
        precio = item["current_price"]
        cambio_24h = item["price_change_percentage_24h"]
        marketcap = item["market_cap"]

        datos_limpios.append([
            nombre,
            f"${precio:,.2f}",
            f"{cambio_24h:.2f}%" if cambio_24h is not None else "N/A",
            f"${marketcap:,.0f}"
        ])

    return datos_limpios

# ============================================================
# 3. EXPORTACIÓN A CSV
# ============================================================

def guardar_csv(datos):
    df = pd.DataFrame(datos, columns=["Nombre", "Precio", "Cambio 24h", "Market Cap"])
    df.to_csv("precios_crypto.csv", index=False)
    return df

# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

if __name__ == "__main__":
    print("Extrayendo datos reales desde la API de CoinGecko...")

    datos_api = extraer_datos()
    datos_limpios = transformar_datos(datos_api)
    df = guardar_csv(datos_limpios)

    print("\nTop 10 criptomonedas extraídas:")
    print(df)

    print("\nArchivo 'precios_crypto.csv' generado correctamente.")
