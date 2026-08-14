import logging
import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, roc_auc_score
from src.xgb_model import XGBoostModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de XGBoost Classifier (D134) ===")
    
    # Generar un dataset sintético para clasificación de alto rendimiento
    X, y = make_classification(n_samples=400, n_features=8, n_informative=5, random_state=42)
    
    # División manual simple para entrenamiento y pruebas
    X_train, X_test = X[:320], X[320:]
    y_train, y_test = y[:320], y[320:]
    
    logging.info(f"Dataset de entrenamiento: {X_train.shape[0]} muestras. Test: {X_test.shape[0]} muestras.")
    
    # Instanciar y entrenar el modelo XGBoost
    xgb_model = XGBoostModel(n_estimators=50, max_depth=4, learning_rate=0.1, random_state=42)
    xgb_model.fit(X_train, y_train)
    
    # Evaluar rendimiento
    predictions = xgb_model.predict(X_test)
    probabilities = xgb_model.predict_proba(X_test)[:, 1]
    
    acc = accuracy_score(y_test, predictions)
    auc_score = roc_auc_score(y_test, probabilities)
    
    logging.info(f"Exactitud (Accuracy) de XGBoost: {acc:.4f}")
    logging.info(f"Puntaje ROC-AUC de XGBoost: {auc_score:.4f}")
    
    # Mostrar importancias de características
    importances = xgb_model.get_feature_importances()
    for idx, imp in enumerate(importances):
        logging.info(f"Característica {idx}: Importancia = {imp:.4f}")
        
    logging.info("=== Hito D134 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()