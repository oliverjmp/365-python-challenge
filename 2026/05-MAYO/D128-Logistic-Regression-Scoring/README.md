# D128 - Logistic Regression Scoring

Este hito implementa un **modelo robusto de clasificación binaria basado en Regresión Logística** utilizando `Scikit-learn` para estimar probabilidades de eventos y realizar scoring analítico de clientes.

## Características Principales
- **Estimación de Probabilidades (`predict_proba`):** Cuantifica la probabilidad exacta de ocurrencia de un evento binario (ej. riesgo de impago, deserción o conversión).
- **Interpretabilidad de Coeficientes:** Permite auditar el peso e impacto directo de cada variable explicativa sobre la decisión del modelo.
- **Pipelines Reutilizables:** Estructura modular orientada a producción con validaciones estrictas de estado y tipos de datos.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
La regresión logística es el estándar de la industria para problemas de clasificación binaria debido a su velocidad y alta interpretabilidad.

### Ejemplos de Uso:
1. **Scoring Crediticio y Admisión de Riesgos:**
   * *Caso:* Estimar la probabilidad de que un solicitante de crédito caiga en impago en función de sus ingresos y deudas actuales.
2. **Campañas de Marketing (Propensity Modeling):**
   * *Caso:* Calcular la probabilidad de que un usuario haga clic en una oferta o compre un producto para priorizar presupuestos de pauta.

## 📂 Estructura del Proyecto
```text
D128-Logistic-Regression-Scoring/
│
├── src/
│   ├── __init__.py
│   └── logistic_engine.py
├── tests/
│   └── test_logistic.py
├── run_logistic.py
├── requirements.txt
└── README.md