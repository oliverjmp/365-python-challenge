# D218 - PyArrow Memory Footprint Optimizer

Configuración avanzada de piscinas de memoria (*Memory Pools*) en **Apache Arrow** para evitar la fragmentación en RAM durante procesamiento analítico masivo.

## 🏛️ Estructura del Proyecto

D218-Memory-Footprint-Optimizer-Arrow/
├── .coveragerc            # Cobertura estricta obligatoria (fail_under = 100)
├── docs/
│   ├── index.md           # Portal técnico hiper-ampliado y profesional
│   └── architecture.md    # Arquitectura detallada de pools de memoria y RAM
├── src/
│   ├── __init__.py
│   └── memory_optimizer.py # Lógica de asignación y monitorización de Pools
├── tests/
│   ├── __init__.py
│   └── test_optimizer.py  # Pruebas unitarias estrictas con pytest (100% Cobertura)
├── app.py                 # Dashboard interactivo en Streamlit
├── main.py                # Script CLI de validación de asignadores
├── mkdocs.yml             # Configuración del portal MkDocs
├── requirements.txt       # Dependencias del entorno
└── README.md              # Documentación principal

## 🚀 Comandos de Ejecución

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Garantizando el 100% de cobertura exacta):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar script CLI de validación:**
  `python main.py`

- **Lanzar Dashboard Interactivo (Streamlit):**
  `streamlit run app.py`

- **Servir documentación técnica:**
  `mkdocs serve`

## 💼 Casos Prácticos de Uso

1. **Procesamiento de Big Data en Entornos con Recursos Limitados (Edge / Cloud Nodes):**
   - Evita fallos por falta de memoria (*OOM Killer*) al procesar ficheros Parquet o CSV que superan la memoria RAM disponible gracias al control estricto de búferes contiguos.
2. **Optimización de Pipelines ETL de Alto Rendimiento:**
   - Reduce de forma drástica la sobrecarga de llamadas al sistema operativo para reservar memoria, acelerando la velocidad de transformación de millones de filas de datos tabulares.
3. **Mitigación de la Fragmentación de Heap en Aplicaciones Python ConCURRENTES:**
   - Previene el crecimiento descontrolado de la memoria virtual residente (*RSS*) en servicios web o workers de analítica que procesan solicitudes masivas de forma continua.