import logging
from src.pipeline_model import MLPipelineModel

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de Pytest ML Pipeline Tests (D147) ===")

    # Datos de ejemplo simulados
    X_train = [[1.5, 2.3, 0.1], [0.2, 0.1, 0.9], [2.1, 1.8, 0.3], [0.1, 0.4, 0.8]]
    y_train = [0, 1, 0, 1]

    model = MLPipelineModel(C=0.5)
    logging.info("Entrenando pipeline con datos de muestra...")
    model.fit(X_train, y_train)
    logging.info("Pipeline entrenado exitosamente.")

    X_test = [[1.2, 2.0, 0.2], [0.3, 0.2, 0.7]]
    predictions = model.predict(X_test)
    probabilities = model.predict_proba(X_test)

    logging.info(f"Predicciones obtenidas: {predictions.tolist()}")
    logging.info(f"Probabilidades asociadas:\n{probabilities}")
    logging.info("=== Hito D147 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()