import logging
import numpy as np
from src.drift_detector import DataDriftDetector

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Script de Detección de Data Drift (D145) ===")

    # Simular datos de entrenamiento (baseline de referencia) y datos recientes en producción
    np.random.seed(42)
    reference_baseline = np.random.normal(loc=50.0, scale=5.0, size=500)
    
    # Caso 1: Producción estable (sin drift significativo)
    production_stable = np.random.normal(loc=50.2, scale=5.1, size=500)
    
    # Caso 2: Producción con deriva (drift por cambio de media)
    production_drifty = np.random.normal(loc=54.5, scale=6.0, size=500)

    detector = DataDriftDetector(significance_level=0.05)

    logging.info("--- Evaluando escenario de Producción Estable ---")
    res_stable = detector.detect_drift(reference_baseline, production_stable)
    logging.info(f"Resultado Estable -> Drift Detectado: {res_stable['drift_detected']} | p-value: {res_stable['p_value']:.4f}")

    logging.info("--- Evaluando escenario de Producción con Deriva (Drift) ---")
    res_drifty = detector.detect_drift(reference_baseline, production_drifty)
    logging.info(f"Resultado Con Deriva -> Drift Detectado: {res_drifty['drift_detected']} | p-value: {res_drifty['p_value']:.4f}")

    logging.info("=== Hito D145 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()