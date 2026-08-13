import logging
from src.quality_gate import QualityGateEnforcer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Validador Estricto de Cobertura (D119) ===")
    
    # Configuramos una puerta de calidad estricta del 100%
    enforcer = QualityGateEnforcer(min_coverage_percentage=100.0)
    
    logging.info(f"Verificando el cumplimiento del umbral de cobertura ({enforcer.min_coverage_percentage}%)...")
    passed, message = enforcer.check_coverage()
    
    if passed:
        logging.info("[✓] Quality Gate superado exitosamente. Código apto para despliegue.")
        print(message)
    else:
        logging.error("[X] Quality Gate fallido. El nivel de pruebas no cumple con los estándares.")
        print(message)
        
    logging.info("=== Hito D119 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()