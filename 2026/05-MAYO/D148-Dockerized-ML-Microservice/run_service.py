import logging
from src.service import MLInferenceService

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Microservicio Dockerizado de ML (D148) ===")
    
    service = MLInferenceService()
    logging.info("Modelo cargado e inicializado en memoria correctamente.")

    # Simulación de petición de inferencia
    sample_data = [[2.5, 2.1], [1.1, 0.9]]
    logging.info(f"Procesando inferencia para datos: {sample_data}")
    
    response = service.predict(sample_data)
    logging.info(f"Respuesta del microservicio: {response}")
    
    logging.info("=== Hito D148 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()