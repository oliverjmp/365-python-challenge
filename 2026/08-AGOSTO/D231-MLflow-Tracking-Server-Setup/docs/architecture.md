# Arquitectura de Trazabilidad MLOps - D231

## 📊 Diagrama de Flujo del Ciclo de Experimentos ML
```mermaid
graph TD
    Script[Script de Entrenamiento / Streamlit App] -->|Registra Parámetros y Métricas| Tracker[MLflowTracker Wrapper]
    Tracker -->|API REST / Python Client| MLflowServer[MLflow Tracking Core]
    MLflowServer -->|Persistencia relacional| SQLite[(Base de Datos SQLite: mlflow.db)]
    MLflowServer -->|Almacenamiento de binarios| Artifacts[(Directorio de Artefactos)]