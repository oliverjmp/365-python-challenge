# JSON SemiStructured Parsing (D186)

Procesamiento analítico de cargas útiles **JSON anidadas** mediante el uso de operadores nativos de extracción de claves en **DuckDB**, aplicando almacenamiento columnar comprimido en formato Parquet.

## 🏛️ Fundamentos de Arquitectura para Datos Semi-estruturados
1. **Extracción Directa sin Esquema Rígido (`->` y `->>`):** Permite consultar atributos internos de objetos JSON anidados directamente en la sentencia SQL sin necesidad de aplanar previamente todo el dataset en memoria.
2. **Tipado Dinámico y Conversión (`CAST`):** Transformación en tiempo de ejecución de valores extraídos de JSON a tipos numéricos o booleanos para agregaciones analíticas de alta precisión.
3. **Eficiencia de Almacenamiento Columnar (ZSTD):** Persistencia de payloads complejos optimizada para lecturas secuenciales rápidas.

---

## 📈 Resultados del Motor Analítico

| Tipo de Evento | Plataforma | Código Resp. | Total Ocurrencias | Latencia Promedio (ms) |
|:---------------|:-----------|:-------------|:------------------|:-----------------------|
| **USER_LOGIN** | Web-Chrome | 200 | 3,125 | 87.45 |
| **CHECKOUT_CART** | iOS | 200 | 3,125 | 92.10 |
| **API_REQUEST** | Android | 500 | 312 | 145.20 |

> **Visualización Interactiva:** El proyecto incluye un **Dashboard Ejecutivo en Streamlit** para explorar el comportamiento de las métricas de eventos ejecutando: `python -m streamlit run src/dashboard.py`.