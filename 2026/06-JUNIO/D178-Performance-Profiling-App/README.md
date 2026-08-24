# D178 - Performance Profiling App (cProfile + Streamlit)

Sistema avanzado de diagnóstico y perfilado de rendimiento en tiempo de ejecución para identificar cuellos de botella y optimizar los tiempos de respuesta de la interfaz analítica en Python.

## Características Principales
- **Integración con cProfile:** Perfilado nativo de funciones y bloques de código pesados para medir costos computacionales detallados.
- **Métricas de Rendimiento en UI:** Visualización integrada de tiempos de ejecución y llamadas de funciones directamente desde la interfaz de Streamlit.
- **Optimización y Depuración:** Detección precisa de latencias y operaciones bloqueantes para garantizar una experiencia de usuario fluida.

## 📂 Estructura del Proyecto
```text
D178-Performance-Profiling-App/
├── src/
│   ├── __init__.py
│   └── profiler_engine.py
├── tests/
│   ├── __init__.py
│   └── test_profiler.py
├── app.py
├── requirements.txt
└── README.md