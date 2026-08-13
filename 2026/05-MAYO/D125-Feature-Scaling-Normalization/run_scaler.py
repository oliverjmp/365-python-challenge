import logging
import pandas as pd
import numpy as np
from src.scaler_engine import FeatureScalerEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Motor de Estandarización y Normalización (D125) ===")
    
    # Dataset con valores atípicos (outliers) y distribuciones sesgadas
    raw_data = {
        "salario": [30000.0, 35000.0, 42000.0, 48000.0, 55000.0, 500000.0], # Outlier extremo
        "antiguedad": [1.0, 2.0, 3.0, 5.0, 7.0, 15.0]
    }
    df = pd.DataFrame(raw_data)
    
    logging.info("Dataset original:")
    print(df)
    
    # 1. Escalado Robusto (Ideal frente a outliers)
    logging.info("\nAplicando RobustScaler (resistente a valores atípicos)...")
    robust_engine = FeatureScalerEngine(method="robust")
    df_robust = robust_engine.fit_transform(df)
    print("\nResultados con RobustScaler:")
    print(df_robust)
    
    # 2. Transformación de Potencia (Yeo-Johnson para normalizar sesgos)
    logging.info("\nAplicando PowerTransformer (Yeo-Johnson para distribuciones sesgadas)...")
    power_engine = FeatureScalerEngine(method="power")
    df_power = power_engine.fit_transform(df)
    print("\nResultados con PowerTransformer:")
    print(df_power)
    
    logging.info("=== Hito D125 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()