# Streamlit DuckDB Analytics App (D195)

Tablero web interactivo de alto rendimiento impulsado por **DuckDB** como motor analítico subyacente y **Streamlit** para la visualización de métricas de negocio en tiempo real.

## 🏛️ Características Técnicas
- **Motor Analítico en Memoria:** Consultas SQL de alto rendimiento ejecutadas directamente sobre archivos y tablas persistidas en el **Data Lake**.
- **Interfaz Interactiva:** Filtrado dinámico de datos, agregaciones automáticas y visualización gráfica avanzada en Streamlit.
- **Persistencia Corporativa:** Almacenamiento optimizado en `data_lake/analytics_warehouse.db`.

---

## 📊 Rendimiento del Motor Analítico

| Operación Analítica | Tecnología | Latencia Promedio | Estado Técnico |
|:--------------------|:-----------|:------------------|:---------------|
| **Consultas Agregadas SQL** | DuckDB Columnar | ~2-8 ms | ✅ **COMPLETADO** |
| **Renderizado de Métricas** | Streamlit UI | Inmediato | ✅ **COMPLETADO** |

> **Conclusión:** La combinación de DuckDB y Streamlit proporciona un stack analítico ligero, escalable y extremadamente rápido para la toma de decisiones empresariales.