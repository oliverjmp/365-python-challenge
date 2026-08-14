# D133 - Ensemble Random Forest Classifier

Este hito implementa un **modelo ensamblado de alta precisión basado en `RandomForestClassifier`** utilizando `Scikit-learn`, combinando múltiples árboles de decisión para mitigar el sobreajuste y mejorar la generalización.

## Características Principales
- **Ensamble de Árboles (Bagging):** Construye múltiples árboles de decisión sobre subconjuntos aleatorios de los datos y promedia sus resultados.
- **Importancia de Características:** Permite extraer métricas cuantitativas sobre qué variables tienen mayor peso en las decisiones del modelo.
- **Robustez Frente al Overfitting:** Reduce la varianza típica de un único árbol de decisión profundo.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Random Forest es uno de los algoritmos de Machine Learning más robustos y versátiles de la industria debido a su alta precisión por defecto y baja sensibilidad a valores atípicos.

### Ejemplos de Uso:
1. **Detección de Fraude Bancario:**
   * *Caso:* Clasificar transacciones financieras como legítimas o fraudulentas basándose en montos, ubicaciones y comportamientos históricos.
   * *Uso:* Aprovechar el ensamble para reducir falsos positivos combinando múltiples perspectivas de decisión.
2. **Medicina Predictiva:**
   * *Caso:* Diagnóstico de enfermedades a partir de múltiples biomarcadores clínicos.
   * *Uso:* Utilizar el análisis de importancia de características para identificar qué síntomas o variables biológicas son más determinantes en el diagnóstico.

## 📂 Estructura del Proyecto
```text
D133-Ensemble-Random-Forest/
│
├── src/
│   ├── __init__.py
│   └── forest.py
├── tests/
│   └── test_forest.py
├── run_forest.py
├── requirements.txt
└── README.md