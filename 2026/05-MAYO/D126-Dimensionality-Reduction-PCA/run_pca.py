import logging
import pandas as pd
import numpy as np
from src.pca_engine import PCADimensionalityEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Motor de Reducción de Dimensionalidad PCA (D126) ===")
    
    # Simular un dataset de alta cardinalidad (ej. 100 muestras, 8 características correlacionadas)
    np.random.seed(42)
    X = np.random.rand(100, 5)
    # Crear alta correlación artificial sumando columnas
    df = pd.DataFrame({
        "Var1": X[:, 0],
        "Var2": X[:, 1],
        "Var3": X[:, 0] * 2 + np.random.normal(0, 0.01, 100),
        "Var4": X[:, 1] * 1.5 + np.random.normal(0, 0.01, 100),
        "Var5": X[:, 2]
    })
    
    logging.info(f"Dimensiones del dataset original: {df.shape}")
    
    # Aplicar PCA preservando el 95% de la varianza explicada
    logging.info("\nAplicando PCA para preservar al menos el 95% de la varianza...")
    pca_engine = PCADimensionalityEngine(n_components=0.95)
    df_reduced = pca_engine.fit_transform(df)
    
    logging.info(f"Dimensiones del dataset reducido: {df_reduced.shape}")
    logging.info(f"Nuevas columnas: {list(df_reduced.columns)}")
    logging.info(f"Varianza explicada por componente: {pca_engine.explained_variance_ratio}")
    logging.info(f"Varianza total acumulada: {np.sum(pca_engine.explained_variance_ratio):.4f}")
    
    print("\nPrimeras filas del dataset reducido:")
    print(df_reduced.head())
    
    logging.info("=== Hito D126 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()