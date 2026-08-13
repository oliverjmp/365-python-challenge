import logging
import hmac
import hashlib
import json
from fastapi.testclient import TestClient
from src.receiver import app, WEBHOOK_SECRET

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración del Receptor de Webhooks Seguro (D113) ===")
    
    client = TestClient(app)
    
    payload = {
        "event": "pipeline.finished",
        "timestamp": "2026-04-14T11:30:00Z",
        "data": {"pipeline_name": "etl_ventas", "records_processed": 5000}
    }
    
    body_bytes = json.dumps(payload).encode("utf-8")
    
    # Generar firma HMAC legítima
    mac = hmac.new(WEBHOOK_SECRET, msg=body_bytes, digestmod=hashlib.sha256)
    valid_signature = f"sha256={mac.hexdigest()}"
    
    logging.info("Enviando petición simulada con firma HMAC válida...")
    response = client.post(
        "/webhook",
        content=body_bytes,
        headers={"X-Hub-Signature-256": valid_signature, "Content-Type": "application/json"}
    )
    
    logging.info(f"Respuesta del servidor Webhook: {response.status_code} -> {response.json()}")
    logging.info("=== Hito D113 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()