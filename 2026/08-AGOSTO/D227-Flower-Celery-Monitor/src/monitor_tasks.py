import time
from src.celery_app import celery_app

@celery_app.task(bind=True, name="monitor_tasks.monitored_computation")
def monitored_computation(self, items_count: int = 5, task_tag: str = "AnalyticsJob") -> dict:
    """Tarea de procesamiento rastreable en tiempo real para supervisión mediante Flower."""
    if items_count < 0:
        raise ValueError("El conteo de elementos no puede ser negativo.")

    processed = 0
    for i in range(items_count):
        time.sleep(0.01)  # Reducido ligeramente para agilizar los tests
        processed += 1
        
        # Solo actualizar estado si hay un task_id válido (evita fallos en llamadas .run() síncronas)
        if self.request.id is not None:
            self.update_state(
                state="PROGRESS",
                meta={"current": processed, "total": items_count, "tag": task_tag}
            )

    return {
        "task_id": self.request.id,
        "task_tag": task_tag,
        "items_processed": processed,
        "status": "SUCCESS"
    }