import hmac
import hashlib
import json
from fastapi import FastAPI, Request, Header, HTTPException, status

app = FastAPI()
SECRET_KEY = "mi-secreto-compartido-super-seguro".encode('utf-8')

def verify_signature(payload_body: bytes, received_signature: str) -> bool:
    """Verifica si la firma recibida coincide con la calculada localmente."""
    expected_signature = hmac.new(SECRET_KEY, payload_body, hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_signature, received_signature)

@app.post("/webhook")
async def receive_webhook(request: Request, x_webhook_signature: str = Header(None)):
    if not x_webhook_signature:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Firma de webhook faltante"
        )
    
    body_bytes = await request.body()
    
    if not verify_signature(body_bytes, x_webhook_signature):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Firma criptográfica inválida"
        )
    
    payload = await request.json()
    return {"status": "success", "received_event": payload.get("event")}