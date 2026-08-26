# Arquitectura de Agregaciones Avanzadas - D213

## 📐 Flujo de Procesamiento Analítico

```mermaid
graph TD
    A[Dataset en Memoria / DataFrame] -->|Puente Apache Arrow| B[DuckDB In-Memory Engine]
    B -->|GROUP BY ROLLUP| C[Subtotales Jerárquicos]
    B -->|GROUP BY CUBE| D[Combinaciones Multidimensionales Cruzadas]