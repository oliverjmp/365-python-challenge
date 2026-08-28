# Arquitectura del Trigger Asíncrono - D228

## 📊 Diagrama de Flujo de Solicitudes y Despacho

```mermaid
graph TD
    Client[Cliente / Frontend HTTP] -->|POST /tasks/trigger| FastAPI[Microservicio FastAPI]
    FastAPI -->|Despacho no bloqueante .delay()| Broker[(Redis Broker)]
    FastAPI -->|Retorna HTTP 202 + Task ID| Client
    
    Broker -->|Asigna tarea| Worker[Celery Worker en Segundo Plano]
    Worker -->|Almacena resultado/estado| Backend[(Redis Backend)]
    
    Client -->|GET /tasks/{task_id}| FastAPI
    FastAPI -->|Consulta estado| Backend
    FastAPI -->|Retorna estado actual| Client