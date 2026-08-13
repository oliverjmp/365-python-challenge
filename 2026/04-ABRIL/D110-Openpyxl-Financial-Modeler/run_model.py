import logging
import pandas as pd
from src.modeler import FinancialModeler

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Constructor Automatizado de Modelos Financieros (D110) ===")
    
    # Datos de prueba para el modelo financiero
    data = pd.DataFrame({
        "Concepto": ["Ingresos por Licencias", "Servicios de Consultoría", "Costos de Servidores", "Gastos de Marketing"],
        "Mes 1": [8500.0, 3200.0, 1500.0, 2000.0],
        "Mes 2": [9200.0, 4100.0, 1500.0, 2500.0],
        "Mes 3": [11000.0, 3800.0, 1800.0, 3000.0]
    })
    
    modeler = FinancialModeler(data)
    file_name = "modelo_financiero_d110.xlsx"
    
    output_path = modeler.generate_excel_model(file_name)
    logging.info(f"¡Modelo financiero generado con éxito en: {output_path}!")
    logging.info("=== Hito D110 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()