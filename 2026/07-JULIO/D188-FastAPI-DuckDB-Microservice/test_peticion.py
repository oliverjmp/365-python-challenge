import httpx

# Probamos la petición directamente mediante código con timeout corto
try:
    print("Enviando petición a la API...")
    response = httpx.get("http://127.0.0.1:8080/health", timeout=3.0)
    print("¡Respuesta recibida con éxito!")
    print("Status code:", response.status_code)
    print("Contenido:", response.json())
except Exception as e:
    print("Error en la petición:", e)