# Arquitectura del Motor de Auditoría - D230

## 📊 Diagrama de Flujo del Motor de Concurrencia
```mermaid
graph TD
    Client[Panel o CLI de Auditoría] -->|Inicia Auditoría| Engine[AuditEngine (ThreadPoolExecutor)]
    Engine -->|Despacha Sonda 1| Probe1[Simulación Asíncrona]
    Engine -->|Despacha Sonda N| ProbeN[Simulación Asíncrona]
    Probe1 --> Results[Consolidación de Métricas]
    ProbeN --> Results
    Results --> JSON[Exportación de Reporte Estructurado]