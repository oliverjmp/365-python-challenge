# Arquitectura de Pruebas y Fixtures - D205

## 📐 Topología de Ejecución y Ciclo de Vida de Fixtures

El siguiente diagrama detalla el flujo mediante el cual el motor de pruebas interactúa con la capa de datos in-memory:

```mermaid
graph TD
    A[Pytest Test Runner] -->|Inyección de Dependencias| B(Fixture: duckdb_memory_conn)
    B -->|Configuración de Esquema DDL| C[(DuckDB In-Memory Instance)]
    C -->|Poblamiento Sintético DML| D[QueryValidator Service]
    D -->|Evaluación de Aserciones SQL| E[Reporte de Cobertura y Métricas]