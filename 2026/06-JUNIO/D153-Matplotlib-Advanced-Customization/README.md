# D153 - Matplotlib Advanced Customization (OOP API)

Este hito implementa la **generación de gráficos analíticos estilizados utilizando la API orientada a objetos (OOP) de Matplotlib**, permitiendo un control milimétrico sobre las capas, ejes duales y paletas de colores corporativas.

## Características Principales
- **Arquitectura OOP Estricta:** Uso directo de las clases `Figure` y `Axes` para aislar contextos de dibujo y evitar efectos colaterales globales (`plt.subplots`).
- **Capas Múltiples Superpuestas:** Integración limpia de gráficos de líneas y barras en un mismo lienzo utilizando ejes gemelos (`twinx()`).
- **Diseño Corporativo Adaptado:** Paletas de colores personalizadas, rejillas optimizadas y gestión limpia de leyendas combinadas.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En analítica de datos avanzada y business intelligence, la visualización personalizada es clave para comunicar insights complejos de forma intuitiva a los stakeholders.

### Ejemplos de Uso:
1. **Dashboards de Rendimiento Comercial:**
   * *Caso:* Comparar el volumen total de ventas (líneas) frente a la tasa de conversión o margen de beneficio porcentual (barras secundarias) en una misma vista temporal.
2. **Monitoreo de Infraestructura y Servidores:**
   * *Caso:* Visualizar el uso de memoria RAM en gigabytes junto al porcentaje de utilización de CPU en intervalos concurrentes.

## 📂 Estructura del Proyecto
```text
D153-Matplotlib-Advanced-Customization/
│
├── src/
│   ├── __init__.py
│   └── plots.py
├── tests/
│   └── test_plots.py
├── run_plot.py
├── requirements.txt
└── README.md