# D134 - Gradient Boosting XGBoost

Este hito implementa un **modelo de boosting de gradiente extremo (`XGBoost`) para modelado predictivo de alto rendimiento**, optimizando árboles de decisión secuenciales mediante la minimización de funciones de pérdida por gradiente.

## Características Principales
- **Optimización por Gradiente Boosting:** Construye árboles de forma secuencial donde cada nuevo árbol corrige los errores residuales de los anteriores.
- **Regularización Avanzada:** Incluye penalizaciones L1 (Lasso) y L2 (Ridge) integradas para prevenir el sobreajuste (*overfitting*).
- **Eficiencia Computacional:** Paralelización nativa de procesos para un entrenamiento extremadamente rápido en grandes volúmenes de datos.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
XGBoost es ampliamente reconocido como uno de los algoritmos más potentes y utilizados en competencias de ciencia de datos (como Kaggle) y en entornos de producción de alta exigencia.

### Ejemplos de Uso:
1. **Predicción de Riesgo Crediticio y Defaults:**
   * *Caso:* Determinar si un solicitante de crédito caerá en impago basándose en historiales financieros complejos.
   * *Uso:* Explotar la alta capacidad predictiva de XGBoost para capturar relaciones no lineales complejas entre variables socioeconómicas.
2. **Sistemas de Recomendación y Conversión de Leads:**
   * *Caso:* Estimar la probabilidad de que un usuario compre un producto en una plataforma de comercio electrónico.
   * *Uso:* Manejar grandes volúmenes de datos dispersos con alta precisión y velocidad de inferencia.

## 📂 Estructura del Proyecto
```text
D134-Gradient-Boosting-XGBoost/
│
├── src/
│   ├── __init__.py
│   └── xgb_model.py
├── tests/
│   └── test_xgb_model.py
├── run_xgboost.py
├── requirements.txt
└── README.md