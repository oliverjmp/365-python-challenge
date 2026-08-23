import logging
import pandas as pd
import numpy as np
from src.data_auditor import DataAuditorEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Auditoría Exploratoria Automatizada (D157) ===")

    # 1. Crear un dataset sintético robusto para la auditoría
    np.random.seed(42)
    n_rows = 1_000
    
    data = {
        "cliente_id": np.arange(1000, 1000 + n_rows),
        "edad": np.random.choice([np.nan, 22, 34, 45, 52, 61, 29, 40], size=n_rows),
        "ingresos_anuales": np.random.normal(50000, 15000, size=n_rows),
        "segmento": np.random.choice(["Retail", "Corporate", "VIP", "SME", None], size=n_rows, p=[0.4, 0.2, 0.1, 0.2, 0.1]),
        "activo": np.random.choice([True, False], size=n_rows)
    }
    
    df_synthetic = pd.DataFrame(data)
    logging.info(f"Dataset sintético generado con forma: {df_synthetic.shape}")

    # 2. Inicializar el motor de auditoría
    auditor = DataAuditorEngine(df_synthetic)

    # 3. Exportar reporte interactivo en HTML
    output_html = "reporte_auditoria_financiera.html"
    logging.info(f"Generando y exportando reporte interactivo a '{output_html}'...")
    
    saved_path = auditor.export_report_to_html(
        output_path=output_html, 
        title="Auditoría Exploratoria - Segmentación de Clientes"
    )
    
    logging.info(f"¡Reporte exportado con éxito en: {saved_path}!")
    logging.info("=== Hito D157 Ejecutado Exitosamente ===")

if __name__ == "__main__":  # pragma: no cover
    main()