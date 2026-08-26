# Portal Técnico: D214 - Parquet Metadata Inspector

## 🏢 Resumen Ejecutivo
El hito **D214** implementa un inspector programático robusto para examinar la estructura interna de los archivos **Apache Parquet** utilizando **PyArrow**. 

Permite auditar esquemas, metadatos de almacenamiento columnar, versiones de formato y estadísticas de compresión a nivel de grupo de filas sin necesidad de cargar todo el contenido del dataset en memoria.

---

## 🎯 Objetivos y Principios Arquitectónicos
* **Inspección sin Carga Masiva:** Lectura directa del pie de página (*footer*) del archivo Parquet.
* **Auditoría de Esquemas:** Validación precisa de tipos de datos, nulos y metadatos personalizados.
* **Optimización de Almacenamiento:** Análisis de grupos de filas y tamaños de compresión.