import logging
import os
from src.consolidator import AprilBlockConsolidator

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Consolidación y Cierre del Bloque de Abril (D120) ===")
    
    # Lista representativa de hitos desarrollados durante abril
    april_milestones = [
        "D110-Openpyxl-Financial-Modeler",
        "D116-Design-Pattern-Factory",
        "D118-Pytest-Integration-Suite",
        "D119-Code-Coverage-Enforcer"
    ]
    
    # Asumimos que estamos un nivel arriba o en la ruta de abril
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    
    consolidator = AprilBlockConsolidator(april_path=parent_dir)
    
    logging.info("Ejecutando auditoría de deuda técnica y empaquetado...")
    report = consolidator.generate_consolidation_report(april_milestones)
    
    print("\n" + report)
    logging.info("=== Hito D120 Ejecutado Exitosamente. ¡Bloque de Abril Concluido! ===")

if __name__ == "__main__":
    main()