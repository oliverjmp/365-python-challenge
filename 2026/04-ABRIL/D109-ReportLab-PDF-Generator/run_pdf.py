import logging
from pathlib import Path
from src.generator import ExecutiveReportGenerator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("=== Iniciando Generador Programático de Reportes PDF (Hito D109) ===")
    
    output_path = "reporte_ejecutivo_d109.pdf"
    generator = ExecutiveReportGenerator(output_filename=output_path)
    
    data = {
        "title": "Informe Anual de Desempeño Operativo 2026",
        "date": "12 de Abril, 2026",
        "author": "Departamento de Ingeniería de Datos"
    }
    
    logging.info("Construyendo documento estructurado y gráficos vectoriales...")
    filepath = generator.generate_pdf(data)
    
    file_info = Path(filepath)
    if file_info.exists():
        logging.info(f"¡PDF generado con éxito en: {file_info.absolute()} (Tamaño: {file_info.stat().st_size} bytes)")
    
    logging.info("=== Hito D109 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()