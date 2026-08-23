import logging
import os
from src.pdf_generator import ExecutivePDFGenerator

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Generación de Informe Ejecutivo en PDF (D158) ===")

    output_pdf = "informe_gerencial_ejecutivo.pdf"
    generator = ExecutivePDFGenerator(output_pdf)

    # Datos estructurados simulados para la tabla ejecutiva
    report_data = [
        ["Indicador Clave", "Departamento", "Desempeño"],
        ["Eficiencia Operativa", "Logística", "98.4%"],
        ["Satisfacción del Cliente", "Soporte", "4.8 / 5.0"],
        ["Reducción de Costos", "Finanzas", "12.5%"],
        ["Nuevos Leads Calificados", "Marketing", "+1,450"],
        ["Tiempo Promedio de Respuesta", "TI", "14 minutos"]
    ]

    logging.info(f"Compilando documento PDF estructurado en: {output_pdf}")
    
    saved_path = generator.generate_report(
        title="Reporte Gerencial de Operaciones",
        subtitle="Monitoreo Estratégico y Métricas de Desempeño - Q2 2026",
        data_rows=report_data
    )

    logging.info(f"¡PDF generado con éxito y guardado en '{saved_path}'!")
    logging.info("=== Hito D158 Ejecutado Exitosamente ===")

if __name__ == "__main__":  # pragma: no cover
    main()