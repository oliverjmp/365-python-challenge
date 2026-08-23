# D170 - A_B Testing Visualizer

Dashboard interactivo desarrollado en Streamlit para el análisis visual, simulación y contraste de hipótesis estadísticas en pruebas A/B utilizando SciPy y Plotly.

## Características Principales
- **Simulación de Datos A/B:** Configuración de tamaños de muestra y tasas de conversión base para los grupos Control y Tratamiento.
- **Pruebas Estadísticas Automatizadas:** Cálculo de valor p (`p-value`) mediante pruebas de proporciones de dos muestras utilizando SciPy.
- **Visualización Interactiva:** Gráficos de barras comparativos de altas prestaciones con Plotly.

## 📂 Estructura del Proyecto
```text
D170-A_B-Testing-Visualizer/
├── src/
│   ├── __init__.py
│   └── stats_analyzer.py
├── tests/
│   ├── __init__.py
│   └── test_stats.py
├── app_ab.py
├── requirements.txt
└── README.md