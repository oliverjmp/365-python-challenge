import hmac
import hashlib
import json
import requests
from typing import Dict, Any

class WebhookDispatcher:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key.encode('utf-8')

    def generate_signature(self, payload: dict) -> str:
        """Genera una firma HMAC-SHA256 para el payload del webhook."""
        # Serializamos usando separators compactos para evitar diferencias de espacios
        payload_bytes = json.dumps(payload, separators=(',', ':'), sort_keys=True).encode('utf-8')
        signature = hmac.new(self.secret_key, payload_bytes, hashlib.sha256).hexdigest()
        return signature

    def send_webhook(self, url: str, event_type: str, data: Dict[str, Any]) -> requests.Response:
        """Envía el webhook añadiendo la firma criptográfica en los encabezados."""
        payload = {
            "event": event_type,
            "data": data
        }
        signature = self.generate_signature(payload)
        headers = {
            "Content-Type": "application/json",
            "X-Webhook-Signature": signature
        }
        response = requests.post(url, data=json.dumps(payload, separators=(',', ':'), sort_keys=True), headers=headers)
        return response