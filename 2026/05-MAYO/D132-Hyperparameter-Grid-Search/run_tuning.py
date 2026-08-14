import logging
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from src.tuner import HyperparameterTuner

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Optimización de Hiperparámetros (D132) ===")

    # Generar dataset sintético para clasificación
    X, y = make_classification(n_samples=300, n_features=8, n_informative=5, random_state=42)
    logging.info(f"Dataset generado: {X.shape[0]} muestras con {X.shape[1]} características.")

    base_model = RandomForestClassifier(random_state=42)
    tuner = HyperparameterTuner(estimator=base_model, cv=5, scoring="roc_auc")

    # 1. Búsqueda en Cuadrícula (GridSearchCV)
    param_grid = {
        "n_estimators": [50, 100],
        "max_depth": [3, 5, 7],
        "criterion": ["gini", "entropy"]
    }
    logging.info("Ejecutando GridSearchCV...")
    grid_res = tuner.grid_search(param_grid, X, y)
    logging.info(f"[{grid_res['search_type']}] Mejor Score (ROC-AUC): {grid_res['best_score']:.4f}")
    logging.info(f"[{grid_res['search_type']}] Mejores Parámetros: {grid_res['best_params']}")

    # 2. Búsqueda Aleatorizada (RandomizedSearchCV)
    param_distrib = {
        "n_estimators": [20, 50, 100, 150, 200],
        "max_depth": [2, 4, 6, 8, 10, None],
        "min_samples_split": [2, 5, 10]
    }
    logging.info("Ejecutando RandomizedSearchCV (10 iteraciones)...")
    random_res = tuner.random_search(param_distrib, X, y, n_iter=10)
    logging.info(f"[{random_res['search_type']}] Mejor Score (ROC-AUC): {random_res['best_score']:.4f}")
    logging.info(f"[{random_res['search_type']}] Mejores Parámetros: {random_res['best_params']}")

    logging.info("=== Hito D132 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()