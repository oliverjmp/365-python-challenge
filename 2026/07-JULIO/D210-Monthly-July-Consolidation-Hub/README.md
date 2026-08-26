# D210 - Monthly July Consolidation Hub

Consolidación estructural, limpieza de deuda técnica y empaquetado integral del bloque de hitos del mes de **Julio** para la arquitectura de ingeniería de datos.

## 🏛️ Estructura del Proyecto

D210-Monthly-July-Consolidation-Hub/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── docs/
│   ├── index.md           # Página principal de documentación técnica del hito
│   └── architecture.md    # Arquitectura detallada del hub de consolidación y flujos
├── src/
│   ├── __init__.py
│   └── consolidation_hub.py # Lógica central de agregación y cálculo de KPIs de julio
├── tests/
│   ├── __init__.py
│   └── test_consolidation.py # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit para el reporte consolidado
├── main.py                # Script CLI para la ejecución automatizada de la consolidación
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Índigo)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Auditoría de Cierre de Ciclo Mensual:**
   - Consolidación automatizada del estado operacional, métricas y niveles de calidad de todos los componentes desarrollados a lo largo del mes.
2. **Gobierno y Eliminación de Deuda Técnica:**
   - Verificación de cumplimiento estricto de políticas de cobertura de código y estandarización arquitectónica antes del despliegue final.
3. **Reportes Ejecutivos Centralizados:**
   - Presentación de indicadores clave de rendimiento (KPIs) mediante interfaces visuales interactivas y scripts automatizados de línea de comandos.

## ⚙️ Componentes Técnicos
- **Hub de Consolidación (`src/consolidation_hub.py`):** Motor analítico respaldado por DuckDB para el procesamiento de datos del mes.
- **Dashboard Interactivo (`app.py`):** Interfaz visual en **Streamlit** para la visualización gerencial de KPIs globales.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color índigo corporativo.

## 🚀 Ejecución y Comandos de Pruebas

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (con cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecución del Script CLI de Consolidación:**
  `python main.py`

- **Lanzamiento del Dashboard Interactivo:**
  `streamlit run app.py`

- **Lanzamiento del Portal de Documentación:**
  `mkdocs serve`