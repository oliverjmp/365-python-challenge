# D127 - Supervised Linear Regression

Este hito implementa un **motor predictivo de regresión lineal múltiple con análisis detallado de residuos y homocedasticidad** utilizando `Scikit-learn`, diseñado para modelar relaciones cuantitativas complejas entre múltiples variables independientes y una variable objetivo continua.

## Características Principales
- **Modelado Multivariante:** Capacidad de ajustar relaciones lineales con múltiples características explicativas simultáneamente.
- **Evaluación Integral de Rendimiento:** Cálculo automatizado de métricas clave de bondad de ajuste como Error Cuadrático Medio ($MSE$), Raíz del Error Cuadrático Medio ($RMSE$) y Coeficiente de Determinación ($R^2$).
- **Diagnóstico de Residuos:** Estructura integrada para calcular las diferencias entre valores reales y predichos, permitiendo validar la hipótesis de homocedasticidad en los errores del modelo.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
La regresión lineal múltiple es la piedra angular del análisis predictivo y estadístico en entornos corporativos y científicos.

### Ejemplos de Uso:
1. **Predicción de Precios de Inmuebles:**
   * *Caso:* Estimar el precio de venta de una vivienda en función de metros cuadrados, número de habitaciones y antigüedad.
2. **Proyección de Ventas Comerciales:**
   * *Caso:* Modelar el volumen de ingresos mensuales utilizando inversión en publicidad, tráfico web y número de comerciales activos.

## 📂 Estructura del Proyecto
```text
D127-Supervised-Linear-Regression/
│
├── src/
│   ├── __init__.py
│   └── linear_regression_engine.py
├── tests/
│   └── test_linear_regression.py
├── run_linear_regression.py
├── requirements.txt
└── README.md