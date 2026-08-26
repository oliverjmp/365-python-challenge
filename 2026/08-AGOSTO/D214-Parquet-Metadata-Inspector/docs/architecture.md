# Arquitectura del Inspector de Metadatos - D214

## 📐 Flujo de Extracción de Metadatos con PyArrow

```mermaid
graph TD
    A[Fichero Físico Parquet] -->|pyarrow.parquet.ParquetFile| B[Footer / Metadata Reader]
    B -->|get_schema_info| C[Esquema y Tipos de Datos]
    B -->|get_file_metadata| D[Conteo de Filas y Versión]
    B -->|get_row_group_statistics| E[Estadísticas por Row Group]