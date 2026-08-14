# D131 - Cross-Validation Strategy

Este hito implementa **estrategias avanzadas de validación cruzada (`K-Fold` y `Stratified K-Fold`)** utilizando `Scikit-learn` para garantizar estimaciones métricas confiables y evitar el sobreajuste (*overfitting*) en modelos de Machine Learning.

## Características Principales
- **K-Fold Cross-Validation:** Divide el conjunto de datos en $K$ particiones secuenciales o aleatorias para entrenar y validar de manera rotativa.
- **Stratified K-Fold:** Garantiza que cada pliegue conserve aproximadamente el mismo porcentaje de muestras de cada clase objetivo, esencial para datasets desbalanceados.
- **Manejo de Robustez:** Cuantifica tanto la media como la desviación estándar del rendimiento del modelo entre iteraciones.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Depender de una única partición de tren/prueba (*train-test split*) puede sesgar drásticamente la evaluación del modelo según qué registros caigan en cada subconjunto. La validación cruzada mitiga este riesgo evaluando todo el dataset de forma cruzada.

### Ejemplos de Uso:
1. **Modelos de Crédito y Riesgo Financiero:**
   * *Caso:* Predecir incumplimientos de pago donde los buenos pagadores superan ampliamente a los morosos.
   * *Uso:* Emplear *Stratified K-Fold* para asegurar que cada fold mantenga la proporción real de morosos, evitando métricas de éxito falsas.
2. **Optimización de Hiperparámetros:**
   * *Caso:* Encontrar la configuración óptima de un algoritmo de clasificación sin sobreajustar los datos de entrenamiento particulares.

## 📂 Estructura del Proyecto
```text
D131-Cross-Validation-Strategy/
│
├── src/
│   ├── __init__.py
│   └── validator.py
├── tests/
│   └── test_validator.py
├── run_cv.py
├── requirements.txt
└── README.md