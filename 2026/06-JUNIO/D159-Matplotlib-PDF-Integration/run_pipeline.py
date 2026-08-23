import logging
import os
from src.chart_pdf_pipeline import ChartPDFPipeline

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Pipeline de Integración Matplotlib + ReportLab (D159) ===")

    output_pdf = "reporte_gerencial_con_graficos.pdf"
    pipeline = ChartPDFPipeline(output_pdf)

    # Datos estadísticos para el gráfico de barras
    categories = ["Q1-2025", "Q2-2025", "Q3-2025", "Q4-2025", "Q1-2026"]
    values = [45000, 52000, 48500, 61000, 74500]

    # Datos estructurados para la tabla resumen del informe
    table_rows = [
        ["Periodo", "Indicador Principal", "Monto Consolidado"],
        ["Q1-2025", "Ventas Directas", "$45,000 USD"],
        ["Q2-2025", "Ventas Directas", "$52,000 USD"],
        ["Q3-2025", "Ventas Directas", "$48,500 USD"],
        ["Q4-2025", "Ventas Directas", "$61,000 USD"],
        ["Q1-2026", "Ventas Directas", "$74,500 USD"]
    ]

    logging.info(f"Renderizando gráfico estadístico y compilando documento PDF en: {output_pdf}")
    
    saved_path = pipeline.build_report_with_chart(
        title="Análisis Ejecutivo de Rendimiento Anual",
        categories=categories,
        values=values,
        summary_table_data=table_rows
    )

    logging.info(f"¡Reporte gerencial con gráficos incrustados generado con éxito en: '{saved_path}'!")
    logging.info("=== Hito D159 Ejecutado Exitosamente ===")

if __name__ == "__main__":  # pragma: no cover
    main()