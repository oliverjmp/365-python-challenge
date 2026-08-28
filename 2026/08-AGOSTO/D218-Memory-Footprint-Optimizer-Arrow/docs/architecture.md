# Arquitectura del Sistema de Gestión de Memoria - D218

## 📐 Diagrama de Secuencia y Flujo de Memoria Columnar

```mermaid
graph TD
    A[Dataset Masivo / Pandas DataFrame] -->|Solicitud de Búfer Columnar| B[PyArrow Memory Pool]
    B -->|Asignación Contigua en Heap| C{Asignador Activo}
    C -->|jemalloc / system| D[Memoria Caché Optimizada sin Fragmentación]
    D --> E[Transformación / Operaciones Analíticas In-Memory]
    E --> F[Liberación y Reciclaje de Bloques en Pool]
    F --> G[Reporte de Métricas y Footprint (Streamlit / CLI)]