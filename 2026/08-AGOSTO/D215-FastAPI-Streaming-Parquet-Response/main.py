import httpx
from src.streaming_api import app
from fastapi.testclient import TestClient

def main():
    print("=== D215: Validación CLI del Servicio de Streaming Parquet ===")
    client = TestClient(app)
    
    response = client.get("/download/parquet")
    print(f"Código de Estado HTTP: {response.status_code}")
    print(f"Tipo de Contenido: {response.headers.get('content-type')}")
    print(f"Cabecera Content-Disposition: {response.headers.get('content-disposition')}")
    print(f"Tamaño del contenido recibido: {len(response.content)} bytes")
    print("\n[✔] Prueba de cliente CLI finalizada con éxito.")

if __name__ == "__main__":
    main()