# Arquitectura del Subsistema Analítico - D219

```mermaid
graph TD
    Client[Cliente / CLI / API] -->|Llamada única| Facade[AnalyticsCoreFacade]
    Facade --> Sub1[ArrowMemoryManagementSubsystem]
    Facade --> Sub2[ColumnarIngestionSubsystem]
    Facade --> Sub3[AnalyticalProcessingSubsystem]