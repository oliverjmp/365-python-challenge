import joblib
import os
from typing import Dict, Any, List

class ModelInferenceService:
    """Servicio encargado de cargar el modelo serializado y realizar predicciones."""
    
    def __init__(self, model_path: str = "src/models/model.joblib"):
        self.model_path = model_path
        self.model = self._load_model()

    def _load_model(self) -> Any:
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"No se encontró el archivo del modelo en: {self.model_path}")
        return joblib.load(self.model_path)

    def predict(self, features: List[float]) -> Dict[str, Any]:
        """Realiza la inferencia para un vector de características dado."""
        if len(features) == 0:
            raise ValueError("El vector de características no puede estar vacío.")
        
        # El modelo espera una matriz 2D (1 muestra, n features)
        X = [features]
        prediction = self.model.predict(X)
        probability = self.model.predict_proba(X) if hasattr(self.model, "predict_proba") else None
        
        return {
            "prediction": int(prediction[0]),
            "probability": float(max(probability[0])) if probability is not None else None
        }