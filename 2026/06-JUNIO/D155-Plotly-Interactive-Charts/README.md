# D155 - Plotly Interactive Charts

Este hito implementa **visualizaciones interactivas de alta respuesta utilizando Plotly Express y Graph Objects**, integrando tooltips dinámicos, diseño responsivo y ejes temporales sincronizados.

## Características Principales
- **Plotly Express (`px.scatter`):** Creación rápida de gráficos interactivos enriquecidos con leyendas por categoría y metadatos en tooltips.
- **Graph Objects y Subplots (`go.Figure` & `make_subplots`):** Paneles múltiples con ejes X sincronizados y herramientas de rastreo unificadas (`hovermode="x unified"`).
- **Exportación Web Autónoma:** Generación de archivos HTML interactivos listos para producción o despliegues locales.

## 📂 Estructura del Proyecto
```text
D155-Plotly-Interactive-Charts/
│
├── src/
│   ├── __init__.py
│   └── interactive_plots.py
├── tests/
│   └── test_interactive_plots.py
├── run_plotly_demo.py
├── requirements.txt
└── README.md