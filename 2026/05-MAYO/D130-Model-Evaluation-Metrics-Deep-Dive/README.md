# D130 - Model Evaluation Metrics Deep Dive

Este hito implementa un **motor especializado en la evaluación integral del rendimiento de modelos de clasificación** utilizando `Scikit-learn`, analizando métricas críticas más allá de la simple exactitud (*accuracy*).

## Características Principales
- **Curva ROC y AUC (Area Under the Curve):** Evalúa la capacidad discriminativa del modelo a través de distintas tasas de falsos y verdaderos positivos.
- **Curva Precision-Recall (PR-AUC):** Ideal para analizar conjuntos de datos desbalanceados donde la clase positiva es minoritaria.
- **Matriz de Confusión Ponderada / Detallada:** Desglose estricto de Verdaderos Positivos, Falsos Positivos, Verdaderos Negativos y Falsos Negativos.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En Machine Learning, depender únicamente del *accuracy* puede llevar a conclusiones erróneas (especialmente con clases desbalanceadas). Las métricas avanzadas permiten afinar los umbrales de decisión del negocio.

### Ejemplos de Uso:
1. **Detección de Fraude Bancario:**
   * *Caso:* Las transacciones fraudulentas representan menos del 1% de los datos.
   * *Uso:* Utilizar PR-AUC y ajustar umbrales para minimizar los falsos positivos (bloquear tarjetas legítimas) maximizando la captura de fraudes reales.
2. **Diagnóstico de Enfermedades Críticas:**
   * *Caso:* Identificar pacientes con patologías graves a partir de estudios clínicos.
   * *Uso:* Maximizar el *Recall* mediante la curva ROC para asegurar que ningún enfermo real sea catalogado erróneamente como sano (evitar falsos negativos).

## 📂 Estructura del Proyecto
```text
D130-Model-Evaluation-Metrics-Deep-Dive/
│
├── src/
│   ├── __init__.py
│   └── evaluator.py
├── tests/
│   └── test_evaluator.py
├── run_evaluation.py
├── requirements.txt
└── README.md