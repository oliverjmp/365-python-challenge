# D152 - Dynamic Sidebar Filters

Este hito implementa un **panel de control interactivo en Streamlit con filtros dinámicos en tiempo real**, permitiendo realizar una segmentación multidimensional de conjuntos de datos mediante Pandas.

## Características Principales
- **Filtros Dinámicos en Sidebar:** Widgets avanzados de selección múltiple y rangos numéricos.
- **Motor de Filtrado Desacoplado:** Lógica de datos separada en `DataFilterEngine` para facilitar pruebas unitarias estrictas.
- **Métricas en Tiempo Real:** Actualización inmediata de indicadores clave de rendimiento (KPIs) según los filtros aplicados.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Los tableros con filtros dinámicos son fundamentales en analítica de negocios (*Business Intelligence*) para permitir a los usuarios explorar la información libremente sin modificar las fuentes de datos originales.

### Ejemplos de Uso:
1. **Paneles de Monitoreo Financiero:**
   * *Caso:* Filtrar transacciones por región, rango de montos y categoría comercial al instante.
2. **Dashboards de Recursos Humanos o Operaciones:**
   * *Caso:* Segmentar empleados o métricas de rendimiento por departamentos de forma ágil y responsiva.

## 📂 Estructura del Proyecto
```text
D152-Dynamic-Sidebar-Filters/
│
├── src/
│   ├── __init__.py
│   └── filter_engine.py
├── tests/
│   ├── __init__.py
│   └── test_filter_engine.py
├── app.py
├── requirements.txt
└── README.md