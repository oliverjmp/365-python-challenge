# D121 - SciPy Statistical Testing

Este hito implementa un **motor analítico para pruebas de hipótesis estadísticas avanzadas (ANOVA, Chi-cuadrado) aplicadas a datasets de negocio** utilizando `SciPy` y `Statsmodels`.

## Características Principales
- **ANOVA de una vía:** Permite evaluar si existen diferencias estadísticamente significativas entre las medias de múltiples grupos de negocio (ej. rendimiento de distintas estrategias comerciales).
- **Prueba de Chi-cuadrado de Independencia:** Analiza la asociación o independencia entre variables categóricas (ej. comportamiento de compra frente a canales de captación).
- **Interpretación Automatizada:** Devuelve conclusiones estructuradas basadas en el nivel de significancia (valor $p$ frente al umbral $\alpha$).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En ciencia de datos y analítica de negocios, tomar decisiones basadas en intuición puede generar pérdidas. Las pruebas de hipótesis validan hallazgos con rigor matemático.

### Ejemplos de Uso:
1. **Optimización de Conversión (A/B/n Testing):**
   * *Caso:* Validar mediante ANOVA si las diferencias de ingresos entre tres variantes de una interfaz web son reales o producto del azar.
2. **Segmentación de Clientes y Comportamiento:**
   * *Caso:* Utilizar Chi-cuadrado para comprobar si la categoría de un cliente (VIP vs Regular) está asociada a su método de pago preferido.

## 📂 Estructura del Proyecto
```text
D121-SciPy-Statistical-Testing/
│
├── src/
│   ├── __init__.py
│   └── statistics_engine.py
├── tests/
│   └── test_statistics.py
├── run_statistics.py
├── requirements.txt
└── README.md