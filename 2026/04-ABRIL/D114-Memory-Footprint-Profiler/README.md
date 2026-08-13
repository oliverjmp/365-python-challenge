# D114 - Memory Footprint Profiler

Este hito implementa un **diagnóstico y optimización del consumo de memoria RAM en scripts de procesamiento masivo** utilizando la librería nativa de Python `tracemalloc`.

## Características Principales
- **Monitoreo de Picos de Memoria (Peak Memory):** Rastrea con precisión cuánta RAM consume una función durante su ejecución crítica.
- **Métricas Integradas:** Combina el diagnóstico de huella de memoria junto al tiempo de ejecución en segundos (`time.perf_counter`).
- **Independencia de Entorno:** Al utilizar la biblioteca estándar de Python, no requiere dependencias pesadas de terceros para perfilado básico.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En proyectos de Big Data, Machine Learning o procesamiento masivo de archivos (como logs gigantes o datasets financieros), las fugas de memoria o el uso excesivo de RAM pueden tumbar servidores enteros.

### Ejemplos de Uso:
1. **Auditoría de Scripts ETL Masivos:**
   * *Caso:* Diagnosticar si la carga completa de archivos CSV pesados a la memoria RAM supera los límites permitidos del servidor (OOM - Out of Memory).
2. **Optimización de Estructuras de Datos:**
   * *Caso:* Comparar el consumo de memoria entre utilizar listas tradicionales frente a generadores (`yield`) o estructuras optimizadas.

## 📂 Estructura del Proyecto
```text
D114-Memory-Footprint-Profiler/
│
├── src/
│   ├── __init__.py
│   └── profiler.py
├── tests/
│   └── test_profiler.py
├── run_profiler.py
├── requirements.txt
└── README.md