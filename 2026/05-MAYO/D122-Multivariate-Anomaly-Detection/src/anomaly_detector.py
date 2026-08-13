import numpy as np
from sklearn.ensemble import IsolationForest
from typing import Dict, Any, List

class MultivariateAnomalyDetector:
    """Motor de detección de anomalías multivariadas utilizando Isolation Forests."""
    
    def __init__(self, contamination: float = 0.1, random_state: int = 42):
        self.contamination = contamination
        self.random_state = random_state
        self.model = IsolationForest(contamination=self.contamination, random_state=self.random_state)
        self.is_fitted = False

    def fit(self, data: List[List[float]]) -> None:
        """Entrena el modelo de Isolation Forest con datos históricos normales o de referencia."""
        X = np.array(data)
        self.model.fit(X)
        self.is_fitted = True

    def predict(self, data: List[List[float]]) -> Dict[str, Any]:
        """Predice si las muestras son normales (1) o anomalías (-1)."""
        if not self.is_fitted:
            raise ValueError("El modelo debe ser entrenado (fit) antes de realizar predicciones.")
        
        X = np.array(data)
        predictions = self.model.predict(X)
        scores = self.model.decision_function(X)
        
        # Convertimos las predicciones a booleanos de anomalía (True si es anomalía)
        is_anomaly = [p == -1 for p in predictions]
        
        return {
            "predictions": predictions.tolist(),
            "anomaly_flags": is_anomaly,
            "anomaly_scores": scores.tolist(),
            "total_anomalies": sum(is_anomaly)
        }