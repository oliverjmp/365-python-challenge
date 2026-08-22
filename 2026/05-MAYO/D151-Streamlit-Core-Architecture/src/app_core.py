from typing import Dict, Any

class StreamlitCoreManager:
    """Clase para gestionar el estado de sesión y lógica de la aplicación Streamlit."""

    def __init__(self):
        pass

    def initialize_state(self, session_state: Dict[str, Any]) -> None:
        """Inicializa las variables clave en el estado de sesión si no existen."""
        if "counter" not in session_state:
            session_state["counter"] = 0
        if "user_name" not in session_state:
            session_state["user_name"] = "Invitado"

    def increment_counter(self, session_state: Dict[str, Any]) -> int:
        """Incrementa el contador en el estado de sesión de forma segura."""
        if "counter" not in session_state:
            session_state["counter"] = 0
        session_state["counter"] += 1
        return session_state["counter"]

    def update_user_name(self, session_state: Dict[str, Any], name: str) -> str:
        """Actualiza el nombre de usuario en el estado de sesión."""
        cleaned_name = name.strip() if name else "Invitado"
        session_state["user_name"] = cleaned_name if cleaned_name else "Invitado"
        return session_state["user_name"]