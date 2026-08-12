import logging
from src.audit_manager import QuarterlyPipelineAudit

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Auditoría Trimestral de Pipelines (Hito D100) ===")
    auditor = QuarterlyPipelineAudit()
    
    report = auditor.generate_health_report()
    
    if report.get("status") == "EMPTY":
        logging.warning("[!] No se encontraron pipelines registrados para auditar.")
        return

    logging.info(f" -> Periodo Auditado: {report.get('quarter')}")
    logging.info(f" -> Total de Pipelines Analizados: {report.get('total_pipelines')}")
    logging.info(f" -> Exitosos: {report.get('success_count')} | Fallidos: {report.get('failed_count')} | Advertencias: {report.get('warning_count')}")
    logging.info(f" -> Tasa de Éxito Global: {report.get('success_rate_percent')}%")
    logging.info(f" -> Estado de Salud del Trimestre: [{report.get('health_status')}]")
    logging.info("=== Auditoría Trimestral Completada con Éxito ===")

if __name__ == "__main__":
    main()