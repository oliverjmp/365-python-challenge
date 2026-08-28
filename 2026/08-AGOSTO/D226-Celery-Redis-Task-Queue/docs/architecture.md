# Arquitectura de Colas Distribuidas Celery + Redis - D226

## 📊 Diagrama de Componentes y Flujo de Mensajería

```mermaid
graph TD
    API[Cliente / Servidor Web FastAPI / Flask] -->|Despacho de Tarea .delay()| Broker[(Redis Message Broker)]
    
    subgraph Workers Celery Distribuidos
        Broker -->|Extracción de Mensaje por Cola| Worker1[Celery Worker 1]
        Broker -->|Extracción de Mensaje por Cola| Worker2[Celery Worker 2]
    end

    Worker1 -->|Almacenamiento de Estado y Resultados| Backend[(Redis Result Backend)]
    Worker2 -->|Almacenamiento de Estado y Resultados| Backend
    
    API -->|Consulta de Estado asynchronous .get()| Backend