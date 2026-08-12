import logging
from src.detector import OutlierDetectionEngine

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Motor Estadístico de Detección de Outliers (Hito D105) ===")
    
    engine = OutlierDetectionEngine(input_path="data/metrics.csv")
    
    try:
        raw_data = engine.load_data()
        logging.info(f"Datos originales cargados: {raw_data}")

        outliers_iqr = engine.detect_outliers_iqr(raw_data)
        logging.info(f"Outliers detectados (IQR): {raw_data[outliers_iqr]}")

        treated_data = engine.treat_outliers(raw_data, method="iqr")
        logging.info(f"Datos tratados sin outliers: {treated_data}")
        
        logging.info("=== Motor D105 Ejecutado Exitosamente ===")
    except Exception as e:
        logging.error(f"[X] Error crítico en la ejecución del motor: {e}")

if __name__ == "__main__":
    main()