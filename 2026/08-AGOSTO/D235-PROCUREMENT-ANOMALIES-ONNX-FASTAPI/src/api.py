from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import onnxruntime as rt
import numpy as np

app = FastAPI(
    title="Procurement Anomaly Detection API",
    description="Microservicio ONNX para detectar anomalías en compras corporativas."
)

MODEL_PATH = "models/anomaly_model.onnx"

# Carga del modelo global con protección de fallos
try:
    session = rt.InferenceSession(MODEL_PATH)
    input_name = session.get_inputs()[0].name
except Exception:
    session = None

class ProcurementData(BaseModel):
    monto: float = Field(..., gt=0, description="Monto total de la orden de compra")
    frecuencia_proveedor: float = Field(..., ge=0, description="Frecuencia histórica del proveedor")
    desviacion_precio: float = Field(..., description="Desviación porcentual frente al mercado")

@app.get("/health")
def health_check():
    if session is None:
        raise HTTPException(status_code=500, detail="Modelo ONNX no disponible en el servidor.")
    return {"status": "operational", "model": "ONNX loaded"}

@app.post("/detect")
def detect_anomaly(data: ProcurementData):
    if session is None:
        raise HTTPException(status_code=500, detail="Modelo ONNX no disponible en el servidor.")
    
    # Preparar el tensor de entrada esperado por ONNX
    features = np.array([[data.monto, data.frecuencia_proveedor, data.desviacion_precio]], dtype=np.float32)
    
    try:
        # Ejecución ultrarrápida en el runtime de ONNX
        pred_onx = session.run(None, {input_name: features})
        is_anomaly = int(pred_onx[0][0])
        return {"anomaly_detected": bool(is_anomaly)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error de inferencia ONNX: {str(e)}")