# Arquitectura del Pipeline de Entrenamiento - D232

## 📊 Diagrama de Flujo del Pipeline MLOps
```mermaid
graph TD
    Data[Generador de Datos Sintéticos / Dataset] -->|Split Train/Test| Trainer[ModelPipelineTrainer Wrapper]
    Trainer -->|Ajuste de Estimador| Model[RandomForestClassifier (Scikit-Learn)]
    Model -->|Evaluación de Métricas| Metrics[Accuracy / Precision]
    Trainer -->|Registra Parámetros y Métricas| MLflowServer[MLflow Tracking API]
    Trainer -->|Empaqueta Binario| Artifacts[Artefacto del Modelo]
    MLflowServer --> SQLite[(Base de Datos SQLite)]