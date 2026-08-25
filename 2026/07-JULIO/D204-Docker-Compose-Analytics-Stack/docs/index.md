# Portal Técnico: D204 - Docker Compose Analytics Stack

## 🏢 Resumen Ejecutivo
El hito **D204** establece una arquitectura de microservicios orientada a servicios analíticos de alta concurrencia. Combinando **FastAPI**, **DuckDB** y la orquestación mediante **Docker Compose**, este sistema desacopla el motor de procesamiento analítico del almacenamiento persistente a través de volúmenes de datos montados en caliente (*hot-mounting*).

---

## 🎯 Objetivos Arquitectónicos
* **Desacoplamiento de Servicios:** Separación clara entre la capa de exposición API y la capa de cómputo analítico in-memory.
* **Persistencia Externa:** Los datasets analíticos residen en volúmenes Docker independientes, permitiendo actualizaciones de datos sin necesidad de reconstruir las imágenes de contenedor (`docker build`).
* **Rendimiento Vectorial:** Procesamiento masivo de consultas estructuradas gracias a las capacidades de motor analítico embebido de DuckDB sobre archivos planos optimizados.

---

## 📊 Especificaciones de la Interfaz Analítica
El microservicio expone endpoints RESTful bajo contratos OpenAPI estrictos, permitiendo la ingesta, agregación y procesamiento en tiempo real de transacciones corporativas multi-región.