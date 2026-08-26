# D212 - DuckDB & MotherDuck Cloud Sync

Sincronización híbrida de bases de datos analíticas locales con la nube de **MotherDuck** utilizando **DuckDB** y Python.

## 🏛️ Estructura del Proyecto

D212-DuckDB-MotherDuck-Cloud-Sync/
├── .coveragerc            # Configuración de políticas estrictas de cobertura (fail_under = 100)
├── docs/
│   ├── index.md           # Página principal de documentación técnica del hito
│   └── architecture.md    # Arquitectura detallada de sincronización híbrida DuckDB / MotherDuck
├── src/
│   ├── __init__.py
│   └── duck_sync.py       # Lógica central del gestor de base de datos y sincronización
├── tests/
│   ├── __init__.py
│   └── test_duck_sync.py  # Pruebas unitarias estrictas con pytest y 100% de cobertura
├── app.py                 # Dashboard interactivo en Streamlit para simulación de sync híbrido
├── main.py                # Script CLI de demostración y pruebas de integración analítica
├── mkdocs.yml             # Configuración del portal web corporativo (Tema Teal)
├── requirements.txt       # Dependencias y librerías del entorno
└── README.md              # Documentación principal en la raíz del proyecto

## 💼 Casos Prácticos de Uso

1. **Analítica Local con Resguardo en la Nube:**
   - Procesamiento de ingestas masivas de datos en estaciones de trabajo o servidores edge, sincronizando resultados consolidados hacia MotherDuck.
2. **Consultas Híbridas Colaborativas:**
   - Combinación de tablas locales temporales con datasets corporativos globales almacenados en la nube analítica.
3. **Optimización de Costos en Cloud Data Warehousing:**
   - Desplazamiento de cómputo pesado hacia el motor local de DuckDB antes de realizar sincronizaciones selectivas.

## ⚙️ Componentes Técnicos
- **Gestor Híbrido (`src/duck_sync.py`):** Encapsulación de conexiones DuckDB y simulación de sincronización con MotherDuck.
- **CLI Demostrativo (`main.py`):** Script ejecutable de validación de tablas y consultas analíticas.
- **Documentación Formal:** Portal técnico estructurado con MkDocs bajo un esquema de color verde teal corporativo.

## 🚀 Comandos para Ejecutar

- **Instalación de dependencias:**
  `pip install -r requirements.txt`

- **Ejecución de pruebas unitarias (con cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecución del Script CLI Demostrativo:**
  `python main.py`

- **Lanzamiento del Dashboard Interactivo (Streamlit):**
  `streamlit run app.py`

- **Lanzamiento del Portal de Documentación (MkDocs):**
  `mkdocs serve`