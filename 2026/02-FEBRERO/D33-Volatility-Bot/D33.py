import requests
import time
from datetime import datetime

def monitor_volatilidad():
    print("\n" + "🚨 " * 15)
    print("  BOT DE VOLATILIDAD LIVE - DÍA 33  ")
    print("🚨 " * 15)

    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    
    precio_anterior = None
    intentos = 0
    max_intentos = 5 # Lo correremos 5 veces para la prueba

    try:
        while intentos < max_intentos:
            res = requests.get(url, params=params)
            datos = res.json()
            precio_actual = datos['bitcoin']['usd']
            hora = datetime.now().strftime("%H:%M:%S")

            if precio_anterior is None:
                print(f"[{hora}] 🏁 Inicio Monitoreo. Precio base: ${precio_actual:,.2f}")
            else:
                diferencia = precio_actual - precio_anterior
                porcentaje = (diferencia / precio_anterior) * 100
                
                # Definimos volatilidad como un cambio > 0.01% para la prueba rápida
                if abs(porcentaje) > 0.01:
                    status = "🔥 MOVIMIENTO DETECTADO"
                else:
                    status = "⚖️ Estable"

                print(f"[{hora}] Bitcoin: ${precio_actual:,.2f} | Var: {porcentaje:+.4f}% | {status}")

            precio_anterior = precio_actual
            intentos += 1
            
            if intentos < max_intentos:
                print("⏳ Esperando 15 segundos para la próxima lectura...")
                time.sleep(15) # Pausa para no saturar la API

        print("\n✅ Sesión de monitoreo finalizada.")

    except Exception as e:
        print(f"❌ Error en el bot: {e}")

if __name__ == "__main__":
    monitor_volatilidad()