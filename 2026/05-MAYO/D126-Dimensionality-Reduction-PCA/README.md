# D126 - Dimensionality Reduction with PCA

Este hito implementa un **motor robusto de reducción de dimensionalidad mediante Análisis de Componentes Principales (PCA)** utilizando `Scikit-learn` para comprimir datasets de alta cardinalidad preservando la máxima varianza explicada posible.

## Características Principales
- **Compresión Inteligente:** Permite reducir características altamente correlacionadas a un conjunto ortogonal de componentes principales (`PC1`, `PC2`, etc.).
- **Selección Dinámica Basada en Varianza:** Soporta umbrales flotantes (ej. `n_components=0.95`) para retener automáticamente el número exacto de dimensiones necesarias para alcanzar un porcentaje de varianza objetivo.
- **Pipelines Reutilizables:** Ajuste seguro en datos de entrenamiento (`fit_transform`) y proyección coherente en nuevos datos (`transform`).

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En ciencia de datos, la maldición de la dimensionalidad degrada el rendimiento de los modelos y aumenta el coste computacional.

### Ejemplos de Uso:
1. **Procesamiento de Imágenes y Visión Artificial:**
   * *Caso:* Reducir matrices masivas de píxeles manteniendo los patrones visuales esenciales antes de alimentar un clasificador.
2. **Genómica y Expresión Génica:**
   * *Caso:* Analizar miles de variables genéticas simultáneas eliminando la multicolinealidad.

## 📂 Estructura del Proyecto
```text
D126-Dimensionality-Reduction-PCA/
│
├── src/
│   ├── __init__.py
│   └── pca_engine.py
├── tests/
│   └── test_pca.py
├── run_pca.py
├── requirements.txt
└── README.md