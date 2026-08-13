import logging
import pandas as pd
import numpy as np
from src.imputation_engine import DataImputationEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Motor de Imputación de Datos Faltantes (D124) ===")
    
    # Dataset simulado con valores nulos (NaN)
    raw_data = {
        "edad": [25.0, 32.0, np.nan, 47.0, 51.0, np.nan],
        "ingresos": [50000.0, np.nan, 65000.0, 80000.0, 120000.0, 60000.0],
        "puntaje_crediticio": [700.0, 650.0, 720.0, np.nan, 810.0, 690.0]
    }
    df = pd.DataFrame(raw_data)
    
    logging.info("Dataset original con valores nulos:")
    print(df)
    
    # Instanciar y ejecutar motor KNN
    logging.info("\nAplicando imputación inteligente basada en KNN (n_neighbors=2)...")
    knn_engine = DataImputationEngine(method="knn", n_neighbors=2)
    df_knn_imputed = knn_engine.fit_transform(df)
    print("\nResultados con KNN Imputer:")
    print(df_knn_imputed)
    
    # Instanciar y ejecutar motor Iterativo (MICE)
    logging.info("\nAplicando imputación multivariada iterativa (IterativeImputer)...")
    iter_engine = DataImputationEngine(method="iterative", random_state=42)
    df_iter_imputed = iter_engine.fit_transform(df)
    print("\nResultados con Iterative Imputer:")
    print(df_iter_imputed)
    
    logging.info("=== Hito D124 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()