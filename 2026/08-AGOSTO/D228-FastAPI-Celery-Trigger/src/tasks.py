import time
from src.celery_app import celery_app

@celery_app.task(bind=True, name="tasks.heavy_computation")
def heavy_computation(self, duration: int = 2, task_name: str = "DefaultTask") -> dict:
    """Tarea asíncrona simulada para procesamiento pesado."""
    if duration < 0:
        raise ValueError("La duración no puede ser negativa.")
    
    time.sleep(duration)
    return {
        "task_id": self.request.id,
        "task_name": task_name,
        "duration": duration,
        "status": "COMPLETED"
    }