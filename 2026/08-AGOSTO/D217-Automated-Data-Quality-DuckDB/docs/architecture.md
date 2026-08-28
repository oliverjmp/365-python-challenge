# Arquitectura del Sistema de Calidad - D217

## 📐 Diagrama de Flujo de Validación y Constraints

```mermaid
graph TD
    A[Datos de Entrada: CSV / Parquet / Pandas] -->|Carga en Memoria| B[DuckDB Validation Engine]
    B -->|Aplicación de Constraints| C{¿Violación de Reglas?}
    C -- Sí -->|Lanza Excepción / Bloquea Ingesta| D[Registro de Incidencias / Rechazo]
    C -- No -->|Persistencia Estructurada| E[Ejecución de Aserciones Analíticas]
    E --> F[Métricas de Calidad y Dashboard Streamlit]