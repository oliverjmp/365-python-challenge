import hmac
import hashlib
from fastapi import FastAPI, Request, HTTPException, Header
from pydantic import BaseModel

app = FastAPI(title="Webhook Receiver Seguro (D113)")

# Clave secreta compartida simulada para firmar los webhooks
WEBHOOK_SECRET = b"mi_secreto_compartido_ultrasecreto"

class WebhookPayload(BaseModel):
    event: str
    timestamp: str
    data: dict

def verify_hmac_signature(body: bytes, signature_header: str) -> bool:
    """Verifica de forma segura la firma HMAC-SHA256 enviada en la cabecera."""
    if not signature_header:
        return False
    
    # Calcular el HMAC esperado
    mac = hmac.new(WEBHOOK_SECRET, msg=body, digestmod=hashlib.sha256)
    expected_signature = f"sha256={mac.hexdigest()}"
    
    # Comparación segura frente a ataques de temporización (timing attacks)
    return hmac.compare_digest(expected_signature, signature_header)

@app.post("/webhook")
async def receive_webhook(request: Request, x_hub_signature_256: str = Header(None)):
    """Endpoint receptor que valida la firma criptográfica antes de procesar el payload."""
    body_bytes = await request.body()
    
    if not verify_hmac_signature(body_bytes, x_hub_signature_256):
        raise HTTPException(status_code=401, detail="Firma HMAC inválida o faltante")
    
    payload = await request.json()
    
    # Lógica de procesamiento del evento recibido
    event_type = payload.get("event", "unknown")
    
    return {
        "status": "success",
        "message": f"Webhook '{event_type}' recibido y validado exitosamente.",
        "processed": True
    }