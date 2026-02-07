import requests
import time
from datetime import datetime

# CONFIGURACIÓN (Reemplaza con tus datos o déjalos vacíos para probar el error handling)
TOKEN_TELEGRAM = "TU_TOKEN_AQUÍ"
CHAT_ID = "TU_ID_AQUÍ"

def enviar_telegram(mensaje):
    url = f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": mensaje}
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"⚠️ No se pudo enviar a Telegram: {e}")

def monitor_volatilidad_pro():
    print("\n" + "🤖 " * 15)
    print("  BOT DE VOLATILIDAD + TELEGRAM - DÍA 34  ")
    print("🤖 " * 15)

    url_crypto = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    
    precio_anterior = None

    while True: # Monitoreo infinito
        try:
            res = requests.get(url_crypto, params=params)
            
            # BLINDAJE: Si la API nos bloquea (Error 429), esperamos y reintentamos
            if res.status_code == 429:
                print("⏳ Límite de API alcanzado. Esperando 60 segundos...")
                time.sleep(60)
                continue

            datos = res.json()
            
            # Verificamos que 'bitcoin' esté en la respuesta antes de leerlo
            if 'bitcoin' not in datos:
                print("⚠️ Respuesta inesperada de la API. Reintentando...")
                time.sleep(10)
                continue

            precio_actual = datos['bitcoin']['usd']
            hora = datetime.now().strftime("%H:%M:%S")

            if precio_anterior is not None:
                diferencia = precio_actual - precio_anterior
                porcentaje = (diferencia / precio_anterior) * 100
                
                if abs(porcentaje) > 0.01: # Umbral de alerta
                    msg = f"🚨 ALERTA VOLATILIDAD\nBitcoin: ${precio_actual:,.2f}\nCambio: {porcentaje:+.4f}%"
                    print(f"[{hora}] {msg.replace('\n', ' ')}")
                    enviar_telegram(msg)
                else:
                    print(f"[{hora}] Bitcoin: ${precio_actual:,.2f} | Estable")

            precio_anterior = precio_actual
            time.sleep(30) # Aumentamos el tiempo para evitar bloqueos

        except KeyboardInterrupt:
            print("\n🛑 Bot detenido por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error inesperado: {e}")
            time.sleep(10)

if __name__ == "__main__":
    monitor_volatilidad_pro()