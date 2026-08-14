import logging
import numpy as np
import pandas as pd
from src.kmeans_clusterer import KMeansClusterEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de K-Means Clustering (D136) ===")

    # Simular base de datos de clientes (ej. Ingresos vs Puntaje de Compras)
    np.random.seed(42)
    n_samples = 300
    
    cluster_1 = np.random.normal(loc=20.0, scale=5.0, size=(n_samples // 3, 2))
    cluster_2 = np.random.normal(loc=50.0, scale=8.0, size=(n_samples // 3, 2))
    cluster_3 = np.random.normal(loc=80.0, scale=6.0, size=(n_samples // 3, 2))
    
    X_data = np.vstack([cluster_1, cluster_2, cluster_3])
    df_clients = pd.DataFrame(X_data, columns=["ingresos_anuales_kUSD", "score_gastos_1_100"])

    logging.info(f"Dataset de clientes generado: {df_clients.shape[0]} registros cargados.")

    # Instanciar motor K-Means con 3 clústeres (segmentos de clientes)
    engine = KMeansClusterEngine(n_clusters=3, random_state=42)
    
    logging.info("Ejecutando K-Means fit_predict para segmentación...")
    labels = engine.fit_predict(df_clients)
    
    df_clients["segmento_cluster"] = labels

    logging.info(f"Inercia del modelo: {engine.inertia:.4f}")
    logging.info("Centroides de los clústeres encontrados:")
    for idx, center in enumerate(engine.cluster_centers):
        logging.info(f"  Clúster {idx} -> Centroide: Ingresos={center[0]:.2f}, Score={center[1]:.2f}")

    print("\nPrimeras filas del DataFrame segmentado:")
    print(df_clients.head())

    logging.info("=== Hito D136 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()