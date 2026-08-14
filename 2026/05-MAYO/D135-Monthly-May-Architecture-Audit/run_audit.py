import logging
import os
from src.auditor import ArchitectureAuditor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Auditoría Mensual de Arquitectura - Mayo (D135) ===")

    # Simular lista de artefactos críticos desarrollados a lo largo del mes
    may_milestones = [
        "src/__init__.py",
        "src/auditor.py",
        "requirements.txt",
        "README.md",
        "non_existent_model_artifact.pkl" # Simulando un faltante para prueba de validación
    ]

    auditor = ArchitectureAuditor()
    
    logging.info("Verificando existencia de componentes e hitos en la arquitectura...")
    audit_results = auditor.verify_required_artifacts(may_milestones)
    
    logging.info(f"Total de componentes auditados: {audit_results['total_checked']}")
    logging.info(f"Componentes faltantes detectados: {audit_results['missing_count']}")
    
    if audit_results['missing_artifacts']:
        for missing in audit_results['missing_artifacts']:
            logging.warning(f"Artefacto faltante o no encontrado: {missing}")

    # Generar reporte de auditoría JSON
    report_file = auditor.generate_audit_report(audit_results, output_filename="may_architecture_audit_report.json")
    logging.info(f"Reporte de auditoría exportado exitosamente en: {report_file}")
    
    logging.info("=== Hito D135 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()