import logging
from src.anomaly_detector import MultivariateAnomalyDetector

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Motor de Detección de Anomalías Multivariadas (D122) ===")
    
    # Simulamos métricas operativas normales de servidores (CPU %, Memoria %)
    normal_operations = [
        [45.2, 60.1],
        [46.0, 59.8],
        [44.8, 61.2],
        [45.5, 60.0],
        [43.9, 58.5],
        [46.1, 60.4],
        [45.0, 59.9]
    ]
    
    detector = MultivariateAnomalyDetector(contamination=0.15, random_state=42)
    
    logging.info("Entrenando Isolation Forest con métricas base del sistema...")
    detector.fit(normal_operations)
    
    # Nuevos registros a auditar (incluyendo un pico anómalo de recursos)
    incoming_metrics = [
        [45.1, 60.2],   # Comportamiento normal
        [99.8, 95.4]    # Comportamiento anómalo crítico
    ]
    
    logging.info("Auditando nuevos registros en busca de anomalías...")
    results = detector.predict(incoming_metrics)
    
    for i, (metrics, is_anom) in enumerate(zip(incoming_metrics, results["anomaly_flags"])):
        status = "⚠️ ANOMALÍA DETECTADA" if is_anom else "✅ Normal"
        logging.info(f"Muestra {i+1} {metrics} -> Estado: {status} (Score: {results['anomaly_scores'][i]:.4f})")
    
    logging.info(f"Total de anomalías encontradas en el lote: {results['total_anomalies']}")
    logging.info("=== Hito D122 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()