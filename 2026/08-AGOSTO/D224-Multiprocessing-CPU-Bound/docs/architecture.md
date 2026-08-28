# Arquitectura de Procesamiento Paralelo CPU-Bound - D224

## 📊 Diagrama de Componentes y Ejecución Multiproceso

```mermaid
graph TD
    Master[Proceso Principal / Orquestador] -->|Asignación de Lotes via ProcessPoolExecutor| Pool[Pool de Procesos del Sistema Operativo]

    subgraph Núcleos Físicos de CPU (Sin restricciones de GIL)
        Pool -->|Proceso 1| Core1[Core CPU 1: compute_heavy_math]
        Pool -->|Proceso 2| Core2[Core CPU 2: compute_heavy_math]
        Pool -->|Proceso N| CoreN[Core CPU N: compute_heavy_math]
    end

    Core1 -->|Serialización IPC / Pickle| Collect[Consolidación de Resultados en Master]
    Core2 -->|Serialización IPC / Pickle| Collect
    CoreN -->|Serialización IPC / Pickle| Collect