# D123 - Advanced Pandas Window Ops

Este hito implementa **operaciones avanzadas de ventanas deslizantes (`rolling`) y agregaciones pesadas en memoria mediante vectorización con Pandas**.

## Características Principales
- **Procesamiento Vectorizado:** Operaciones optimizadas de alto rendimiento sobre DataFrames sin bucles `for` lentos en las filas.
- **Métricas Estadísticas Dinámicas:** Cálculo simultáneo de medias móviles, desviaciones estándar ponderadas y Z-Scores móviles para detección temprana de anomalías en series temporales.
- **Robustez ante Divisiones por Cero:** Manejo seguro de valores constantes mediante umbrales flotantes estables.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En análisis financiero e IoT industrial, las métricas de ventana deslizante permiten suavizar ruido y detectar comportamientos fuera de control en tiempo real.

### Ejemplos de Uso:
1. **Monitoreo de Sensores Industriales (IoT):**
   * *Caso:* Detectar picos de temperatura o presión en turbinas comparando el valor actual frente a su media y desviación móvil histórica.
2. **Detección de Fraude en Transacciones Bursátiles:**
   * *Caso:* Evaluar volúmenes de compra en ventanas deslizantes de tiempo para identificar comportamientos atípicos de liquidez.

## 📂 Estructura del Proyecto
```text
D123-Advanced-Pandas-Window-Ops/
│
├── src/
│   ├── __init__.py
│   └── window_processor.py
├── tests/
│   └── test_window.py
├── run_window.py
├── requirements.txt
└── README.md