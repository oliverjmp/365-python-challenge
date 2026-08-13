import logging
from src.pipeline_observer import DataPipeline, LoggingObserver, MetricsObserver

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Patrón Observer en Pipelines (D117) ===")
    
    # Crear el pipeline (Sujeto)
    pipeline = DataPipeline("etl_transacciones_diarias")
    
    # Instanciar observadores
    logger_obs = LoggingObserver()
    metrics_obs = MetricsObserver()
    
    # Suscribir observadores al pipeline
    pipeline.attach(logger_obs)
    pipeline.attach(metrics_obs)
    
    # Ejecutar el pipeline exitosamente
    logging.info("--- Ejecución 1: Exitosa ---")
    pipeline.run(5000)
    
    # Ejecutar el pipeline con fallo simulado
    logging.info("--- Ejecución 2: Con Fallo ---")
    pipeline.run(0)
    
    logging.info("=== Hito D117 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()