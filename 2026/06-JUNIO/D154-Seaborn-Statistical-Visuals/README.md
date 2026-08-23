# D154 - Seaborn Statistical Visuals

Este hito implementa **gráficos estadísticos avanzados utilizando Seaborn y NumPy**, enfocándose en el análisis exploratorio de datos mediante distribuciones bivariadas con estimación de densidad (KDE) y mapas de calor de correlación matricial.

## Características Principales
- **Simulación Numérica Controlada:** Generación de variables aleatorias correlacionadas mediante distribuciones normales de NumPy.
- **Mapas de Calor Matriciales (`sns.heatmap`):** Visualización clara de coeficientes de correlación de Pearson con escalas de color normalizadas.
- **Distribuciones Bivariadas (`sns.jointplot`):** Análisis conjunto de pares de variables combinando histogramas marginales y contornos de densidad suavizados.

## 💡 Casos de Uso Prácticos
1. **Análisis Exploratorio de Datos (EDA):** Detección rápida de multicolinealidad en modelos de Machine Learning mediante matrices de correlación.
2. **Estudios Biométricos y Demográficos:** Visualización de la relación bivariada entre variables continuas complejas (ej. peso vs altura o ingresos vs gasto).

## 📂 Estructura del Proyecto
```text
D154-Seaborn-Statistical-Visuals/
│
├── src/
│   ├── __init__.py
│   └── stats_plots.py
├── tests/
│   └── test_stats_plots.py
├── run_stats_plot.py
├── requirements.txt
└── README.md