# Arquitectura de Apache Flight Data Transfer - D211

## 📐 Topología de Red y Transferencia In-Memory

```mermaid
graph TD
    A[Cliente / Aplicación Analítica] -->|Solicitud gRPC (Ticket)| B[Apache Flight Server / src/flight_server.py]
    B -->|Acceso Directo a Búferes| C[Tabla Apache Arrow en Memoria]
    C -->|Stream Columnar Sin Serialización| A