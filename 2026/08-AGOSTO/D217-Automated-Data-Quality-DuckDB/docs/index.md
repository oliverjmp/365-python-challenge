# Portal Técnico: D217 - Automated Data Quality con DuckDB

## 🏢 Resumen Ejecutivo
El hito **D217** introduce un marco arquitectónico avanzado para la **automatización de la calidad de datos** (*Data Quality*). Mediante el uso de restricciones declarativas a nivel de motor (`PRIMARY KEY`, `NOT NULL`, `CHECK`) y aserciones analíticas en **DuckDB**, garantizamos que ningún registro corrupto o anómalo contamine las capas subsiguientes del ciclo analítico.

---

## 🎯 Objetivos y Principios Arquitectónicos
* **Integridad Declarativa:** Validación in-memory en tiempo de ingesta mediante restricciones SQL nativas.
* **Tolerancia a Fallos por Diseño:** Rechazo automático de transacciones que violen las reglas de dominio del negocio.
* **Observabilidad Analítica:** Generación de métricas de calidad en tiempo real para auditorías técnicas.