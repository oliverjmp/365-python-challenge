import logging
import pandas as pd
from src.window_processor import AdvancedWindowProcessor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Procesador Avanzado de Ventanas Deslizantes (D123) ===")
    
    # Crear un dataset de series temporales simuladas de sensores industriales
    raw_data = {
        "temperatura": [22.5, 23.0, 22.8, 35.4, 23.1, 22.9, 23.2],
        "presion": [101.2, 101.3, 101.1, 105.0, 101.2, 101.0, 101.1]
    }
    df = pd.DataFrame(raw_data)
    
    logging.info(f"Dataset original cargado con {len(df)} registros.")
    
    processor = AdvancedWindowProcessor(df)
    logging.info("Calculando ventanas deslizantes y agregaciones vectorizadas (window=3)...")
    
    metrics_df = processor.compute_advanced_metrics(window_size=3)
    
    logging.info("Resultados calculados exitosamente:")
    print(metrics_df.tail(3))
    
    logging.info("=== Hito D123 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()