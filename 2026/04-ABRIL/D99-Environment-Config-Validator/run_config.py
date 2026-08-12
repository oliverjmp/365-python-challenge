import logging
from src.config import Settings

# Configuración básica del sistema de logs
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Validación de Configuración del Sistema (D99) ===")
    try:
        # Al instanciar Settings, Pydantic valida automáticamente el entorno
        config = Settings()
        logging.info("[✓] Configuración cargada y validada exitosamente con Pydantic.")
        logging.info(f" -> Entorno de Aplicación (APP_ENV): {config.app_env}")
        logging.info(f" -> Conexión a Base de Datos (DATABASE_URL): {config.database_url[:15]}... [PROTEGIDO]")
        logging.info(f" -> Clave Secreta de API (API_SECRET_KEY): {'*' * len(config.api_secret_key)}")
        logging.info(f" -> Conexiones Máximas Permitidas: {config.max_connections}")
    except Exception as e:
        logging.error(f"[X] Error crítico en la validación de variables de entorno: {e}")

if __name__ == "__main__":
    main()