# Portal Técnico: D215 - FastAPI Streaming Parquet Response

## 🏢 Resumen Ejecutivo
El hito **D215** implementa un servicio web asíncrono utilizando **FastAPI** y `StreamingResponse` para optimizar la transferencia de grandes volúmenes de datos tabulares almacenados en formato **Apache Parquet**, evitando la saturación de memoria RAM en el servidor web.

---

## 🎯 Objetivos Clave
* **Eficiencia de Memoria:** Transmisión de ficheros por bloques de bytes (*chunks*).
* **Escalabilidad Web:** Arquitectura lista para producción con Uvicorn y FastAPI.