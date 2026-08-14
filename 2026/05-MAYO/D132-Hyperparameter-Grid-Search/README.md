# D132 - Hyperparameter Grid Search & Random Search

Este hito implementa un **motor automatizado para la optimización de hiperparámetros en modelos predictivos de Machine Learning**, combinando las estrategias de `GridSearchCV` y `RandomizedSearchCV` de `Scikit-learn`.

## Características Principales
- **GridSearchCV:** Evalúa exhaustivamente todas las combinaciones posibles en el espacio de parámetros especificado.
- **RandomizedSearchCV:** Muestrea de forma aleatoria un número fijo de combinaciones de hiperparámetros, ideal para espacios de búsqueda grandes y optimización de tiempo de cómputo.
- **Evaluación mediante Validación Cruzada Integrada:** Evalúa cada combinación cruzadamente ($K$-Fold) con métricas personalizadas (`accuracy`, `roc_auc`, `f1`, etc.).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Ajustar manualmente los hiperparámetros de un algoritmo (como la profundidad de un árbol o el número de estimadores en un bosque) es ineficiente y puede llevar a modelos subóptimos o sobreajustados.

### Ejemplos de Uso:
1. **Modelos de Predicción de Abandono de Clientes (Churn):**
   * *Caso:* Optimizar un modelo XGBoost o Random Forest para maximizar el recall/ROC-AUC.
   * *Uso:* Utilizar *RandomizedSearchCV* para explorar rápidamente rangos amplios de número de árboles, tasa de aprendizaje y profundidad máxima.
2. **Clasificación de Riesgo Crediticio:**
   * *Caso:* Refinar la precisión de un modelo donde los hiperparámetros deben ajustarse cuidadosamente bajo validación cruzada estricta para evitar sobreajuste en producción.

## 📂 Estructura del Proyecto
```text
D132-Hyperparameter-Grid-Search/
│
├── src/
│   ├── __init__.py
│   └── tuner.py
├── tests/
│   └── test_tuner.py
├── run_tuning.py
├── requirements.txt
└── README.md