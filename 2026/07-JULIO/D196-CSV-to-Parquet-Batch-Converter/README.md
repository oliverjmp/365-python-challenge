# D196 - CSV to Parquet Batch Converter

Pipeline automatizado de conversión por lotes para ficheros CSV de gran tamaño, utilizando **Generadores de Python** para control de memoria RAM y escritura eficiente en formato columnar **PyArrow Parquet**.

## 🏛️ Casos de Uso Empresariales
1. **Ingesta de Ficheros Kilométricos:** Permite procesar archivos CSV de gigabytes que exceden la capacidad de la memoria RAM del servidor, leyéndolos de forma fragmentada (*chunks*).
2. **Optimización de Almacenamiento en Data Lake:** Convierte datos planos en bruto (`data_lake/raw/`) a formatos columnares comprimidos de alta velocidad analítica (`data_lake/processed/`).
3. **Auditoría y Trazabilidad:** Monitoreo en tiempo real del flujo de registros mediante interfaces de consola avanzadas con **`rich`**.

## 📂 Estructura del Proyecto
```text
D196-CSV-to-Parquet-Batch-Converter/
├── data_lake/
│   ├── raw/                  # Ficheros CSV de origen masivo
│   └── processed/            # Ficheros Parquet optimizados
├── docs/
│   └── index.md              # Portal de documentación MkDocs
├── src/
│   ├── __init__.py
│   └── batch_converter.py    # Motor lógico con Generadores
├── tests/
│   ├── __init__.py
│   └── test_batch_converter.py # Suite de pruebas pytest
├── run_converter.py          # Script ejecutable principal con rich
├── mkdocs.yml                # Configuración de MkDocs
├── requirements.txt          # Dependencias
└── README.md                 # Documentación técnica