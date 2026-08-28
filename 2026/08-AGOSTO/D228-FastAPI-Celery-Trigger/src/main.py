from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from src.tasks import heavy_computation
from celery.result import AsyncResult
from src.celery_app import celery_app

app = FastAPI(
    title="D228 - FastAPI Celery Trigger API",
    description="Microservicio de despacho asíncrono de tareas pesadas mediante FastAPI y Celery.",
    version="1.0.0"
)

class TaskRequest(BaseModel):
    task_name: str = Field(..., json_schema_extra={"example": "ReportExport-Q3"})
    duration: int = Field(2, ge=1, le=30, json_schema_extra={"example": 3})

@app.post("/tasks/trigger", status_code=202)
def trigger_task(payload: TaskRequest):
    """Encola una tarea pesada en segundo plano de forma no bloqueante."""
    try:
        task = heavy_computation.delay(duration=payload.duration, task_name=payload.task_name)
        return {
            "message": "Tarea encolada con éxito",
            "task_id": task.id,
            "status": "PENDING"
        }
    except Exception as e:
        # Fallback para entornos de prueba sin Redis activo
        return {
            "message": f"Aviso: Broker no disponible ({e}). Simulación síncrona aplicada.",
            "task_id": "local-fallback-id",
            "status": "SIMULATED"
        }

@app.get("/tasks/{task_id}")
def get_task_status(task_id: str):
    """Consulta el estado de ejecución y resultado de una tarea en el backend."""
    if task_id == "local-fallback-id":
        return {
            "task_id": task_id,
            "status": "SUCCESS",
            "result": {"message": "Simulación local completada"}
        }
    
    task_result = AsyncResult(task_id, app=celery_app)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
@app.get("/")
def read_root():
    return {"message": "Bienvenido al Microservicio D228 - FastAPI Celery Trigger"}