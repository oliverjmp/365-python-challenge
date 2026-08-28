from celery import Celery

# Configuración central de la instancia Celery con Redis como Broker y Backend de resultados
celery_app = Celery(
    "enterprise_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)