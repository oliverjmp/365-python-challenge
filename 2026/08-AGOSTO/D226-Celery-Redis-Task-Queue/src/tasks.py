import time
from src.celery_app import celery_app

@celery_app.task(bind=True, name="tasks.heavy_background_computation")
def heavy_background_computation(self, duration: int = 3, task_name: str = "DefaultTask") -> dict:
    """Tarea distribuida pesada simulada para ejecución en segundo plano por workers de Celery."""
    if duration < 0:
        raise ValueError("La duración de la tarea no puede ser negativa.")
    
    # Simulación de procesamiento intensivo o llamada bloqueante a red/base de datos
    time.sleep(duration)
    
    return {
        "task_id": self.request.id,
        "task_name": task_name,
        "duration_seconds": duration,
        "status": "COMPLETED"
    }