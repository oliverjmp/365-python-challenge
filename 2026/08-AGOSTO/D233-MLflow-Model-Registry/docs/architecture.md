# Arquitectura del Model Registry - D233

## 📊 Diagrama de Ciclo de Vida del Modelo
```mermaid
graph TD
    Trainer[Entrenamiento del Modelo] -->|Log Model & Register| Registry[MLflow Model Registry]
    Registry -->|Versión 1, 2, 3...| Staging[Etapa: Staging]
    Staging -->|Aprobación de Calidad| Production[Etapa: Production]
    Production -->|Desaprobación / Sustitución| Archived[Etapa: Archived]
    Registry --> SQLite[(Base de Datos SQLite)]