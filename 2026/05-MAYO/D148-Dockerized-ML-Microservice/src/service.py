import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from typing import Union, Dict, Any

class MLInferenceService:
    """Microservicio básico de inferencia de Machine Learning."""

    def __init__(self):
        self.model = LogisticRegression(random_state=42)
        self.is_ready = False
        self._initialize_dummy_model()

    def _initialize_dummy_model(self) -> None:
        """Entrena el modelo con datos sintéticos iniciales para dejarlo listo (ready)."""
        X_train = np.array([[1.0, 2.0], [2.0, 1.0], [3.0, 3.0], [4.0, 5.0]])
        y_train = np.array([0, 0, 1, 1])
        self.model.fit(X_train, y_train)
        self.is_ready = True

    def predict(self, features: Union[list, np.ndarray, pd.DataFrame]) -> Dict[str, Any]:
        """Realiza una inferencia a partir de características de entrada."""
        if not self.is_ready:
            raise RuntimeError("El servicio no está listo para inferencias.")

        X_df = pd.DataFrame(features) if not isinstance(features, pd.DataFrame) else features
        if X_df.empty:
            raise ValueError("Las características de entrada no pueden estar vacías.")

        predictions = self.model.predict(X_df)
        probabilities = self.model.predict_proba(X_df)

        return {
            "predictions": predictions.tolist(),
            "probabilities": probabilities.tolist(),
            "status": "success"
        }