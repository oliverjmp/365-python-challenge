import logging
import numpy as np
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, classification_report
from src.forest import RandomForestModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de Random Forest Classifier (D133) ===")
    
    # Generar un dataset sintético
    X, y = make_classification(n_samples=300, n_features=6, n_informative=4, random_state=42)
    
    # Dividir en entrenamiento y prueba de forma manual simple
    X_train, X_test = X[:240], X[240:]
    y_train, y_test = y[:240], y[240:]
    
    logging.info(f"Dataset de entrenamiento: {X_train.shape[0]} muestras. Test: {X_test.shape[0]} muestras.")
    
    # Instanciar y entrenar el modelo ensamblado
    rf_model = RandomForestModel(n_estimators=50, max_depth=6, random_state=42)
    rf_model.fit(X_train, y_train)
    
    # Evaluar
    predictions = rf_model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    
    logging.info(f"Exactitud (Accuracy) del Random Forest: {acc:.4f}")
    
    # Mostrar importancias de características
    importances = rf_model.get_feature_importances()
    for idx, imp in enumerate(importances):
        logging.info(f"Característica {idx}: Importancia = {imp:.4f}")
        
    logging.info("=== Hito D133 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()