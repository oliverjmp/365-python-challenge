from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List
from src.model_service import ModelInferenceService

app = FastAPI(
    title="ML Inference API",
    description="Microservicio web para inferencia en tiempo real de modelos de Machine Learning.",
    version="1.0.0"
)

# Inicializamos el servicio de inferencia con manejo seguro
try:
    inference_service = ModelInferenceService()
except Exception:
    inference_service = None

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., json_schema_extra={"example": [0.5, -1.2, 3.4, 0.1]})

class PredictionResponse(BaseModel):
    prediction: int
    probability: float

@app.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    """Endpoint de verificación de estado del servicio y del modelo."""
    if inference_service is None or getattr(inference_service, "model", None) is None:
        raise HTTPException(status_code=500, detail="El modelo de Machine Learning no está cargado correctamente.")
    return {"status": "healthy", "model_loaded": True}

@app.post("/predict", response_model=PredictionResponse, status_code=status.HTTP_200_OK)
def predict(payload: PredictionRequest):
    """Realiza la predicción en tiempo real enviando un arreglo de características."""
    if inference_service is None:
        raise HTTPException(status_code=500, detail="Servicio de inferencia no disponible.")
    try:
        result = inference_service.predict(payload.features)
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno durante la inferencia: {str(e)}")