import logging
import numpy as np
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from src.validator import CrossValidationStrategy

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de Validación Cruzada (D131) ===")
    
    # Generar un dataset sintético de clasificación binaria desbalanceada
    X, y = make_classification(n_samples=200, n_features=5, n_informative=3, weights=[0.8, 0.2], random_state=42)
    
    logging.info(f"Dataset generado: {X.shape[0]} muestras, {X.shape[1]} características.")
    
    model = RandomForestClassifier(random_state=42)
    validator = CrossValidationStrategy(n_splits=5, shuffle=True, random_state=42)
    
    # 1. Evaluación con K-Fold Estándar
    kfold_res = validator.evaluate_kfold(model, X, y, scoring='roc_auc')
    logging.info(f"Resultado [{kfold_res['strategy']}]: Media ROC-AUC = {kfold_res['mean_score']:.4f} (±{kfold_res['std_score']:.4f})")
    
    # 2. Evaluación con Stratified K-Fold
    skfold_res = validator.evaluate_stratified_kfold(model, X, y, scoring='roc_auc')
    logging.info(f"Resultado [{skfold_res['strategy']}]: Media ROC-AUC = {skfold_res['mean_score']:.4f} (±{skfold_res['std_score']:.4f})")
    
    logging.info("=== Hito D131 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()