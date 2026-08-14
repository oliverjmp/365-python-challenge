import logging
import pandas as pd
import numpy as np
from src.tree_engine import DecisionTreeEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Clasificador de Árbol de Decisión (D129) ===")
    
    # Dataset simulado de segmentación de clientes o riesgo
    # Variables: [Antigüedad (años), Gasto Anual (miles)]
    # Target: 0 = Cliente Estándar, 1 = Cliente VIP
    np.random.seed(42)
    df = pd.DataFrame({
        "antiguedad": [0.5, 1.0, 1.5, 2.0, 6.0, 7.0, 8.5, 9.0],
        "gasto_anual": [5.0, 8.0, 6.0, 10.0, 50.0, 65.0, 60.0, 80.0],
        "segmento": [0, 0, 0, 0, 1, 1, 1, 1]
    })
    
    X = df[["antiguedad", "gasto_anual"]]
    y = df["segmento"]
    
    logging.info("Entrenando Árbol de Decisión con criterio de ganancia de información (Entropía)...")
    engine = DecisionTreeEngine(criterion="entropy", max_depth=3, random_state=42)
    engine.fit(X, y)
    
    logging.info(f"Importancias de características: {engine.feature_importances}")
    
    # Nuevos clientes a clasificar
    new_clients = pd.DataFrame({
        "antiguedad": [1.2, 7.5],
        "gasto_anual": [7.5, 70.0]
    }, index=["Cliente 1 (Estándar)", "Cliente 2 (VIP)"])
    
    logging.info("Clasificando nuevos clientes...")
    predictions = engine.predict(new_clients)
    probabilities = engine.predict_proba(new_clients)
    
    print("\nResultados de Clasificación:")
    for i, (idx, row) in enumerate(new_clients.iterrows()):
        cls = "💎 Cliente VIP" if predictions[i] == 1 else "👤 Cliente Estándar"
        prob = probabilities[i][predictions[i]]
        logging.info(f"{idx} -> Predicción: {cls} (Confianza: {prob:.4f})")
        
    dot_structure = engine.export_tree_dot()
    logging.info(f"Estructura DOT generada correctamente (Longitud: {len(dot_structure)} caracteres).")
    logging.info("=== Hito D129 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()