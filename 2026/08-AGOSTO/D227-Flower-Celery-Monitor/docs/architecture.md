# Arquitectura de Monitoreo con Celery Flower - D227

## 📊 Diagrama de Componentes y Auditoría en Tiempo Real

```mermaid
graph TD
    Worker[Celery Workers Ejecutando Tareas] -->|Actualización de Estado / Metadatos| Broker[(Redis Message Broker / Backend)]
    
    Broker -->|Consulta de Métricas y Eventos| Flower[Celery Flower Dashboard / Puerto 5555]
    
    Admin[Ingeniero de Operaciones / SRE] -->|Supervisión Web HTTP en Tiempo Real| Flower
    Admin -->|Inspección y Revocación de Tareas| Flower