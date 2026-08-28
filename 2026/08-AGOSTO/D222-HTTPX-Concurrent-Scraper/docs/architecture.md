# Arquitectura del Sistema de Ingesta Concurrente - D222

## 📊 Diagrama de Componentes y Flujo Keep-Alive

```mermaid
graph TD
    Client[Orquestador Asíncrono / HTTPXClient] -->|Pool de Conexiones Keep-Alive| Pool[Gestor de Conexiones HTTPX]
    
    subgraph Peticiones Concurrentes en Paralelo
        Pool -->|Solicitud 1| Server1[(Servidor Web Destino A)]
        Pool -->|Solicitud 2| Server2[(Servidor Web Destino B)]
        Pool -->|Solicitud N| ServerN[(Servidor Web Destino N)]
    end

    Server1 -->|Respuesta HTTP sin renegociar TCP| Gather[Agregación de Resultados: asyncio.gather]
    Server2 -->|Respuesta HTTP sin renegociar TCP| Gather
    ServerN -->|Respuesta HTTP sin renegociar TCP| Gather
    
    Gather --> Output[Consolidación de Métricas y Datasets de Ingesta]