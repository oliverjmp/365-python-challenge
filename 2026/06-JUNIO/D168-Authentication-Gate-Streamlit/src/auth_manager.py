import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

def load_config(config_path: str = "config.yaml") -> dict:
    """
    Carga el fichero de configuración YAML con las credenciales y parámetros de cookies.
    """
    with open(config_path, "r") as file:
        config = yaml.load(file, Loader=SafeLoader)
    return config

def init_authenticator(config: dict):
    """
    Inicializa la instancia de autenticación de Streamlit-Authenticator.
    """
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days']
    )
    return authenticator