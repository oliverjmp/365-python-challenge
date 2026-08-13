import logging
import pandas as pd
import numpy as np
from src.linear_regression_engine import MultipleLinearRegressionEngine

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Motor de Regresión Lineal Múltiple (D127) ===")
    
    # Simular datos de rendimiento académico basados en horas de estudio y horas de sueño
    np.random.seed(42)
    n_samples = 100
    horas_estudio = np.random.uniform(1, 10, n_samples)
    horas_sueno = np.random.uniform(4, 9, n_samples)
    
    # Ecuación objetivo real con un pequeño componente de ruido aleatorio
    calificacion = 5.0 + 1.2 * horas_estudio + 0.8 * horas_sueno + np.random.normal(0, 0.5, n_samples)
    
    df = pd.DataFrame({
        "horas_estudio": horas_estudio,
        "horas_sueno": horas_sueno,
        "calificacion": calificacion
    })
    
    X = df[["horas_estudio", "horas_sueno"]]
    y = df["calificacion"]
    
    logging.info(f"Dataset de entrenamiento generado con {n_samples} muestras.")
    
    # Instanciar y ajustar el motor
    reg_engine = MultipleLinearRegressionEngine()
    reg_engine.fit(X, y)
    
    logging.info(f"Intercepto del modelo: {reg_engine.intercept:.4f}")
    logging.info(f"Coeficientes: {reg_engine.coefficients}")
    
    # Evaluar rendimiento
    metrics = reg_engine.evaluate(X, y)
    logging.info(f"Métricas de evaluación - MSE: {metrics['mse']:.4f}, RMSE: {metrics['rmse']:.4f}, R²: {metrics['r2']:.4f}")
    
    # Análisis de residuos para homocedasticidad
    residuals_df = reg_engine.analyze_residuals(X, y)
    logging.info("Análisis de residuos completado. Primeras filas:")
    print(residuals_df.head())
    
    logging.info("=== Hito D127 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()