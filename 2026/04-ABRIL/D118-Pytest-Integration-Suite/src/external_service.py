import requests
from typing import Dict, Any

class ExternalAPIClient:
    """Cliente para interactuar con servicios externos (ej. APIs REST de terceros)."""
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def get_user_data(self, user_id: int) -> Dict[str, Any]:
        """Consulta datos de un usuario en el servicio externo."""
        headers = {"Authorization": f"Bearer {self.api_key}"}
        response = requests.get(f"{self.base_url}/users/{user_id}", headers=headers)
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise ValueError(f"Usuario con ID {user_id} no encontrado en el servicio externo.")
        else:
            raise ConnectionError(f"Error en servicio externo: Código HTTP {response.status_code}")