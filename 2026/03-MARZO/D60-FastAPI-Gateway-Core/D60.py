from fastapi import FastAPI, HTTPException, status, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, EmailStr
import time
import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("FastAPI-Gateway-Core")

app = FastAPI(
    title="Enterprise Gateway Core",
    version="1.0.0",
    description="Microservicio backend de alto rendimiento con validación estricta de esquemas."
)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time-Seconds"] = str(round(process_time, 4))
    logger.info(f"Path: {request.url.path} | Latency: {process_time:.4f}s")
    return response

class AnalyticsIngestPayload(BaseModel):
    client_id: int = Field(..., gt=0, description="Identificador único del cliente corporativo.")
    transaction_amount: float = Field(..., gt=0.0, description="Monto monetario de la transacción analítica.")
    operator_email: EmailStr = Field(..., description="Correo electrónico verificado del operador responsable.")
    metadata_tag: str = Field(..., min_length=3, max_length=50, description="Etiqueta de clasificación interna.")

class AnalyticsResponse(BaseModel):
    status: str
    processed_id: int
    message: str

@app.post(
    "/api/v1/ingest", 
    response_model=AnalyticsResponse, 
    status_code=status.HTTP_201_CREATED,
    summary="Ingesta segura de métricas analíticas"
)
async def ingest_analytics_data(payload: AnalyticsIngestPayload):
    try:
        logger.info(f"Procesando transacción para cliente ID: {payload.client_id}")
        return AnalyticsResponse(
            status="success",
            processed_id=payload.client_id,
            message="Payload validado e ingerido correctamente en el motor analítico."
        )
    except Exception as e:
        logger.error(f"Error crítico en la transacción: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Fallo interno al procesar el flujo analítico."
        )

@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check():
    return {"status": "healthy", "engine": "FastAPI + Pydantic v2"}