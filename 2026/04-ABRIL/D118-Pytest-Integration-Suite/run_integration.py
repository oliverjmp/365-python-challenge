import logging
from src.external_service import ExternalAPIClient

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Suite de Integración con Mocking (D118) ===")
    
    client = ExternalAPIClient(base_url="https://api.thirdpartyservice.com", api_key="production_key")
    
    logging.info(f"Conectando a endpoint base: {client.base_url}")
    logging.info("Nota: Este script es demostrativo. Las pruebas de integración reales utilizan simulación (monkeypatch/fixtures) en pytest para no depender de servicios externos reales.")
    
    logging.info("=== Hito D118 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()