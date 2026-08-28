# Arquitectura del Pipeline de Enmascaramiento - D216

## 📐 Diagrama de Flujo del Pipeline SQL

```mermaid
graph TD
    A[Datos Crudos con PII: Pandas DataFrame] -->|Carga en Memoria| B[DuckDB In-Memory Engine]
    B -->|Transformación SQL Avanzada| C[Enmascaramiento de Tarjetas & Truncado de Nombres]
    B -->|Hash Criptográfico SHA256| D[Anonimización de Emails]
    C --> E[Dataset Seguro Resultante]
    D --> E