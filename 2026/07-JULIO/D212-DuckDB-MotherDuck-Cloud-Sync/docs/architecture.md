# Arquitectura de Sincronización Híbrida - D212

## 📐 Topología de Datos entre DuckDB y MotherDuck

```mermaid
graph TD
    A[Pipeline / Aplicación Local] -->|Carga de Datos Vectoriales| B[DuckDB Embedded Engine / src/duck_sync.py]
    B -->|Consulta Analítica Local| C[(Base de Datos Local)]
    B -->|Sincronización Híbrida (Cloud Sync)| D[(MotherDuck Cloud Database)]