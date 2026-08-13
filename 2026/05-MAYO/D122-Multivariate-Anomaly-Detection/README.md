# D122 - Multivariate Anomaly Detection

Este hito implementa un **motor estadístico de detección de anomalías multivariadas mediante Isolation Forests** utilizando `NumPy` y `Scikit-learn`.

## Características Principales
- **Algoritmo Isolation Forest:** Diseñado específicamente para aislar anomalías en lugar de perfilar puntos normales, siendo altamente eficiente en espacios multivariados de alta dimensión.
- **Entrenamiento y Predicción Modular:** Permite ajustar umbrales de contaminación y auditar lotes de datos operativos en tiempo real.
- **Métricas de Gravedad:** Devuelve puntuaciones de decisión que cuantifican qué tan atípica es una observación respecto al comportamiento histórico.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En arquitectura de datos y ciberseguridad, detectar comportamientos fuera de lo común de forma temprana previene fallos sistémicos.

### Ejemplos de Uso:
1. **Monitoreo de Infraestructura y Servidores:**
   * *Caso:* Identificar sobrecargas simultáneas de CPU y Memoria que no se detectan analizando cada métrica por separado de forma univariada.
2. **Detección de Fraude en Transacciones Financieras:**
   * *Caso:* Descubrir patrones de pagos inusuales combinando variables como monto, ubicación geográfica y frecuencia horaria.

## 📂 Estructura del Proyecto
```text
D122-Multivariate-Anomaly-Detection/
│
├── src/
│   ├── __init__.py
│   └── anomaly_detector.py
├── tests/
│   └── test_anomaly.py
├── run_anomaly.py
├── requirements.txt
└── README.md