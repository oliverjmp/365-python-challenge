import logging
from src.validators import InferencePayload
from pydantic import ValidationError

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de Pydantic ML Payload Validator (D143) ==0")
    
    # 1. Ejemplo exitoso
    valid_data = {"model_version": "v1.2.0", "features": [0.2, 0.8, 0.5], "threshold": 0.6}
    try:
        payload = InferencePayload(**valid_data)
        logging.info(f"✅ Payload válido procesado con éxito: {payload.model_dump()}")
    except ValidationError as e:
        logging.error(f"Error inesperado: {e}")

    # 2. Ejemplo con fallo de regla de negocio
    invalid_data = {"model_version": "v2.0.0", "features": [0.5]}
    try:
        InferencePayload(**invalid_data)
    except ValidationError as e:
        logging.info(f"⚠️ Validación detenida correctamente por regla de negocio:\n{e}")

    logging.info("=== Hito D143 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()