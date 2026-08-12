import logging
from src.cleaner import DataCleaningPipeline

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Pipeline de Limpieza Masiva (Hito D104) ===")
    
    pipeline = DataCleaningPipeline(input_path="data/raw_data.csv")
    
    try:
        cleaned_df = pipeline.run_pipeline()
        logging.info("Datos limpios obtenidos con éxito:")
        print("\n", cleaned_df, "\n")
        logging.info("=== Pipeline Ejecutado Exitosamente ===")
    except Exception as e:
        logging.error(f"[X] Error crítico en la ejecución del pipeline: {e}")

if __name__ == "__main__":
    main()