# Arquitectura de Contenedores y Volúmenes - D204

## 📐 Topología de Despliegue Local (`Docker Compose`)

La infraestructura opera mediante un esquema de contenedores aislados con comunicación de red interna y mapeo de volúmenes de almacenamiento persistente.

```mermaid
graph TD
    A[Cliente / Streamlit Dashboard] -->|HTTP GET /analytics/summary| B(Contenedor: FastAPI Analytics API)
    B -->|Consulta SQL Vectorial| C(Motor In-Memory: DuckDB)
    C -->|Lectura Directa via read_csv_auto| D[(Volumen Local Compartido: ./data/source_data.csv)]