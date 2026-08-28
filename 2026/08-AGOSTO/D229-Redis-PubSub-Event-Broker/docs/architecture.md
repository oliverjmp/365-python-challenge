# Arquitectura y Topología de Eventos - D229

## 📊 Diagrama de Flujo y Topología Pub/Sub

```mermaid
graph TD
    subgraph Productores / Microservicios Emisores
        P1[Servicio de Pedidos] -->|Publica JSON| C1[(Canal: orders)]
        P2[Servicio de Usuarios] -->|Publica JSON| C2[(Canal: notifications)]
    end

    subgraph Motor de Broker (Redis)
        C1 --> Redis[(Redis Pub/Sub Engine)]
        C2 --> Redis
    end

    subgraph Consumidores / Suscriptores
        Redis -->|Broadcast| S1[Worker de Facturación]
        Redis -->|Broadcast| S2[Servicio de Email]
        Redis -->|Broadcast| S3[Dashboard de Auditoría]
    end