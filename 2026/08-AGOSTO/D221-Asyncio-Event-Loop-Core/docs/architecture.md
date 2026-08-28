# Arquitectura del Bucle de Eventos Asíncrono - D221

## 📊 Diagrama de Componentes y Flujo Concurrente

```mermaid
graph TD
    Client[Cliente / Script Principal] -->|Invocación: execute_concurrent_workload| Core[AsyncEventLoopCore]
    
    subgraph Event Loop de Python
        Core -->|Lanzamiento Masivo| Task1[Corrutina I/O 1]
        Core -->|Lanzamiento Masivo| Task2[Corrutina I/O 2]
        Core -->|Lanzamiento Masivo| TaskN[Corrutina I/O N]
    end

    subgraph Operaciones No Bloqueantes
        Task1 -->|asyncio.sleep / Network| Wait1[(Espera Cooperativa)]
        Task2 -->|asyncio.sleep / Network| Wait2[(Espera Cooperativa)]
        TaskN -->|asyncio.sleep / Network| WaitN[(Espera Cooperativa)]
    end

    Wait1 --> Gather[Agregación de Resultados: asyncio.gather]
    Wait2 --> Gather
    WaitN --> Gather
    
    Gather --> Output[Diccionario de Métricas y Tiempos de Cómputo]