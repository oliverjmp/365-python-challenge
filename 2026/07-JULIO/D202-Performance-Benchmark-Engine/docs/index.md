# D202 - Performance Benchmark Engine

Sistema avanzado de medición y certificación de rendimiento analítico comparando arquitecturas basadas en **Pandas** y **DuckDB** mediante Python.

---

## 🏛️ Descripción General del Hito

El hito **D202** implementa un motor de pruebas de rendimiento (*benchmarking*) automatizado para evaluar cuantitativamente la eficiencia en consultas de agregación masiva. En la ingeniería de datos moderna, elegir el motor de procesamiento adecuado impacta directamente en los costos de infraestructura y los tiempos de entrega de información.

---

## 🚀 Arquitectura Técnica y Capacidades

1. **Motor de Tiempo (`src/benchmark_runner.py`):**
   - Generación dinámica de datasets escalables en memoria.
   - Medición precisa de ejecuciones múltiples mediante `timeit`.
   - Comparación directa entre operaciones con DataFrames de Pandas y consultas SQL sobre DuckDB in-process.

2. **Dashboard Interactivo (`app.py`):**
   - Interfaz en **Streamlit** para simular cargas de trabajo variables y visualizar métricas de velocidad comparadas.

3. **Pruebas de Calidad (`tests/test_benchmark.py`):**
   - Cobertura estricta al 100% garantizada mediante `pytest`.

---

## 💼 Casos de Uso Empresariales
- **Toma de Decisiones Arquitectónicas:** Justificación técnica basada en datos sobre cuándo utilizar Pandas frente a motores analíticos columnares como DuckDB.
- **Pruebas de Carga en ETLs:** Medición preventiva de rendimiento antes de desplegar transformaciones pesadas a producción.