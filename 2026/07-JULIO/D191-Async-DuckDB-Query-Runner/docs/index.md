# Async DuckDB Query Runner (D191)

Motor de ejecución concurrente y no bloqueante para consultas analíticas pesadas sobre archivos persistentes en el Data Lake, utilizando **asyncio** y la concurrencia nativa de **DuckDB**.

## 🏛️ Características Técnicas
- **Persistencia en Data Lake:** Lectura y escritura sobre bases de datos físicas en disco (`data_lake/async_analytics.db`).
- **Procesamiento Asistido por Hilos:** Ejecución en paralelo de múltiples consultas analíticas pesadas mediante `asyncio.to_thread` sin bloquear el hilo principal de Python.
- **Optimización de I/O Analítico:** Lanzamiento simultáneo de lotes de consultas (`asyncio.gather`) para maximizar el rendimiento del motor analítico.

---

## 📊 Rendimiento Concurrente

| ID Consulta | Carga de Trabajo Analítica | Duración Individual | Estado de Ejecución |
|:------------|:---------------------------|:--------------------|:--------------------|
| **Q_VENTAS_TOTALES** | Agregación por categorías | ~15-30 ms | ✅ **COMPLETADO** |
| **Q_FILTRO_TECNOLOGIA** | Filtrado condicional de registros | ~10-20 ms | ✅ **COMPLETADO** |
| **Q_ESTADISTICAS_GLOBALES** | Métricas agregadas (COUNT, AVG, MAX) | ~15-25 ms | ✅ **COMPLETADO** |

> **Conclusión:** El aislamiento de conexiones por hilo y la asincronía permiten procesar flujos analíticos pesados de forma eficiente y no bloqueante.