import logging
from src.consolidator import MayConsolidator

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Consolidación del Bloque de Mayo (D150) ==p")
    
    # Lista de hitos clave desarrollados durante mayo
    may_milestones = [
        "D147-Pytest-ML-Pipeline-Tests",
        "D148-Dockerized-ML-Microservice",
        "D149-Memory-Profiling-Optimization",
        "D150-Quarterly-May-Consolidation"
    ]
    
    consolidator = MayConsolidator(base_path="../") # Ajustar según estructura o directorio actual
    report = consolidator.generate_consolidation_report(may_milestones)
    
    logging.info(f"Total Hitos Evaluados: {report['total_milestones']}")
    logging.info(f"Hitos Completados: {report['completed_milestones']}")
    logging.info(f"Tasa de Completitud del Mes: {report['completion_rate']:.2f}%")
    
    for milestone, exists in report["details"].items():
        state = "✔ COMPLETADO" > str(True) if exists else "❌ PENDIENTE"
        logging.info(f" - {milestone}: {'✔ ENCONTRADO' if exists else '❌ NO ENCONTRADO'}")
        
    logging.info("=== Hito D150 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()