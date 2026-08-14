import logging
import pandas as pd
import numpy as np
from src.logistic_engine import LogisticScoringEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Modelo de Regresión Logística y Scoring (D128) ===")
    
    # Simulamos un dataset de scoring crediticio de clientes
    # Variables: [Ingresos Anuales (miles), Historial de Deuda (miles)]
    # Target: 0 = Bajo Riesgo (No paga mal), 1 = Alto Riesgo (Incumplimiento)
    np.random.seed(42)
    data = {
        "ingresos": [25.0, 30.0, 35.0, 40.0, 85.0, 90.0, 110.0, 120.0],
        "deuda": [15.0, 18.0, 12.0, 14.0, 2.0, 5.0, 3.0, 1.0],
        "default": [1, 1, 1, 1, 0, 0, 0, 0]
    }
    df = pd.DataFrame(data)
    
    X = df[["ingresos", "deuda"]]
    y = df["default"]
    
    logging.info("Entrenando modelo de Regresión Logística...")
    engine = LogisticScoringEngine(random_state=42)
    engine.fit(X, y)
    
    logging.info(f"Coeficientes aprendidos: {engine.coefficients}")
    
    # Nuevos clientes a evaluar (Scoring de riesgo)
    new_clients = pd.DataFrame({
        "ingresos": [28.0, 95.0],
        "deuda": [16.0, 4.0]
    }, index=["Cliente A (Riesgoso)", "Cliente B (Seguro)"])
    
    logging.info("Calculando probabilidades de scoring para nuevos clientes...")
    probabilities = engine.predict_proba(new_clients)
    predictions = engine.predict(new_clients)
    
    print("\nResultados de Scoring:")
    for i, (idx, row) in enumerate(new_clients.iterrows()):
        prob_default = probabilities[i][1]
        status = "⚠️ Alto Riesgo (Default)" if predictions[i] == 1 else "✅ Bajo Riesgo"
        logging.info(f"{idx} -> Probabilidad de Incumplimiento: {prob_default:.4f} | Estado: {status}")
    
    logging.info("=== Hito D128 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()