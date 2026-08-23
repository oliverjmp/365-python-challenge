import logging
import os
import json
from src.architecture_auditor import ArchitectureAuditor

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Auditoría de Arquitectura del Semestre (D160) ===")

    registry_path = "semestre_registry.json"
    report_path = "informe_auditoria_arquitectura.json"

    # Crear un archivo de registro simulado con los hitos clave del semestre
    sample_registry = {
        "semester_period": "01-ENERO al 30-JUNIO 2026",
        "components": [
            {"name": "D153-Matplotlib-Automation", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D154-Seaborn-Advanced-Viz", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D155-Plotly-Interactive-Dashboards", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D156-Streamlit-Executive-App", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D157-Pandas-Profiling-Automation", "coverage_percentage": 90.0, "status": "active"},
            {"name": "D158-ReportLab-Dynamic-PDF-Canvas", "coverage_percentage": 100.0, "status": "active"},
            {"name": "D159-Matplotlib-PDF-Integration", "coverage_percentage": 99.0, "status": "active"}
        ]
    }

    with open(registry_path, "w", encoding="utf-8") as f:
        json.dump(sample_registry, f, indent=4, ensure_ascii=False)

    logging.info(f"Registro de componentes cargado desde: {registry_path}")

    auditor = ArchitectureAuditor(registry_path)
    data = auditor.load_registry_data()
    
    logging.info("Ejecutando evaluación de rendimiento y métricas de cobertura...")
    summary = auditor.audit_component_performance(data["components"])
    logging.info(f"Resumen de Auditoría: {summary}")

    saved_path = auditor.generate_report(data["components"], report_path)
    logging.info(f"¡Informe de auditoría arquitectónica generado exitosamente en: '{saved_path}'!")
    logging.info("=== Hito D160 Ejecutado Exitosamente ===")

if __name__ == "__main__":  # pragma: no cover
    main()