# Arquitectura del Patrón Productor-Consumidor - D223

## 📊 Diagrama de Componentes y Flujo de Cola

```mermaid
graph TD
    Prod[Corrutina Productora] -->|asyncio.Queue.put / Backpressure| Queue[(asyncio.Queue Buffer Compartido)]
    
    subgraph Workers Consumidores Concurrentes
        Queue -->|asyncio.Queue.get| Cons1[Consumidor 1]
        Queue -->|asyncio.Queue.get| Cons2[Consumidor 2]
        Queue -->|asyncio.Queue.get| Cons3[Consumidor N]
    end

    Cons1 -->|task_done / Registro| Results[(Contenedor de Resultados)]
    Cons2 -->|task_done / Registro| Results
    Cons3 -->|task_done / Registro| Results