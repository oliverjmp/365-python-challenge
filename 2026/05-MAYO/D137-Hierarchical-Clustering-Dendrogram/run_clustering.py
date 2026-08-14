import logging
import numpy as np
from src.cluster_analyzer import HierarchicalClusterAnalyzer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Análisis de Conglomerados Jerárquicos (D137) ===")

    # Generación de datos sintéticos con 3 grupos claros
    np.random.seed(42)
    cluster_1 = np.random.normal(loc=0.0, scale=0.5, size=(10, 2))
    cluster_2 = np.random.normal(loc=5.0, scale=0.5, size=(10, 2))
    cluster_3 = np.random.normal(loc=10.0, scale=0.5, size=(10, 2))
    dataset = np.vstack([cluster_1, cluster_2, cluster_3])

    logging.info(f"Dataset generado con forma: {dataset.shape}")

    # Inicializar analizador
    analyzer = HierarchicalClusterAnalyzer(dataset, method="ward")

    # 1. Calcular matriz de enlace (Linkage Matrix)
    logging.info("Calculando matriz de enlace jerárquico (Method: Ward)...")
    linkage_matrix = analyzer.compute_linkage()
    logging.info(f"Matriz de enlace obtenida con dimensiones: {linkage_matrix.shape}")

    # 2. Extraer conglomerados planos basados en una distancia de corte
    threshold = 3.0
    clusters = analyzer.extract_clusters(linkage_matrix, threshold=threshold, criterion="distance")
    unique_clusters = np.unique(clusters)
    logging.info(f"Conglomerados extraídos (Umbral={threshold}): {len(unique_clusters)} grupos encontrados.")
    logging.info(f"Asignación de clusters por muestra: {clusters}")

    # 3. Obtener estructura para dendrograma analítico
    dendro_info = analyzer.get_dendrogram_data(linkage_matrix, truncate_mode="level", p=3)
    logging.info(f"Estructura del dendrograma calculada con éxito. Claves disponibles: {list(dendro_info.keys())}")

    logging.info("=== Hito D137 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()