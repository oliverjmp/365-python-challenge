import requests
from typing import Dict, Any

def trigger_webhook(url: str, payload: Dict[str, Any], timeout: int = 5) -> Dict[str, Any]:
    """
    Envía una petición POST a un endpoint de webhook especificado y retorna el resultado.
    """
    if not url or not url.startswith("http"):
        return {
            "success": False,
            "status_code": 0,
            "response": "URL inválida o vacía."
        }

    try:
        response = requests.post(url, json=payload, timeout=timeout)
        try:
            resp_body = response.json()
        except ValueError:
            resp_body = response.text

        return {
            "success": response.ok,
            "status_code": response.status_code,
            "response": resp_body
        }
    except requests.exceptions.RequestException as e:
        return {
            "success": False,
            "status_code": 500,
            "response": str(e)
        }