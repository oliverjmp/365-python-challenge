import requests
import json
from datetime import datetime
from pathlib import Path

def tracker_cripto_v1():
    print("\n" + "🌐 " * 15)
    print("  TRACKER DE CRIPTOMONEDAS - DÍA 32  ")
    print("🌐 " * 15)

    # 1. Configuración de la API (Endpoint)
    # Usamos una API pública que no requiere Key para este ejemplo
    url = "https://api.coingecko.com/api/v3/simple/price"
    parametros = {
        "ids": "bitcoin,ethereum,solana",
        "vs_currencies": "usd",
        "include_24hr_change": "true"
    }

    try:
        # 2. Realizar la petición HTTP GET
        print("🛰️  Conectando con el servidor remoto...")
        respuesta = requests.get(url, params=parametros)
        
        # 3. Validar estado de la conexión (Status Code 200 = OK)
        respuesta.raise_for_status()

        # 4. Parsear el JSON (Convertir texto plano a Diccionario Python)
        datos = respuesta.json()

        # 5. Presentación de Datos
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n📈 PRECIOS ACTUALIZADOS ({fecha}):")
        print("-" * 45)
        print(f"{'MONEDA':<12} | {'PRECIO (USD)':<12} | {'CAMBIO 24H'}")
        print("-" * 45)

        for moneda, info in datos.items():
            precio = info['usd']
            cambio = info['usd_24h_change']
            emoji = "🟢" if cambio > 0 else "🔴"
            
            print(f"{moneda.capitalize():<12} | ${precio:<11,.2f} | {emoji} {cambio:.2f}%")

        # 6. Guardar snapshot en un archivo JSON local
        ruta_json = Path(__file__).parent / "ultimo_pull.json"
        with open(ruta_json, "w") as f:
            json.dump(datos, f, indent=4)
        print(f"\n💾 Snapshot guardado en: {ruta_json.name}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")

if __name__ == "__main__":
    tracker_cripto_v1()