# Arquitectura del Servicio de Streaming - D215

## 📐 Diagrama de Flujo de Datos

```mermaid
graph TD
    A[Cliente HTTP / TestClient] -->|GET /download/parquet| B[FastAPI Endpoint]
    B -->|Genera Chunks en Disco| C[iter_file Generator]
    C -->|StreamingResponse de Bytes| A