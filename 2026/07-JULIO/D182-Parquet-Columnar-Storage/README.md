# D182 - Parquet Columnar Storage

Pipeline de conversión masiva de ficheros CSV planos a formato columnar comprimido Parquet utilizando `PyArrow`.

## Características Principales
- **Almacenamiento Columnar:** Reduce drásticamente el espacio en disco y acelera las lecturas analíticas en comparación con archivos de texto plano (CSV).
- **Compresión Integrada:** Soporta algoritmos eficientes como Snappy o Gzip.
- **Cobertura Total:** Validado con pruebas unitarias estrictas bajo `pytest` garantizando el **100% de cobertura**.

## 💡 Casos de Uso Prácticos
1. **Optimización de Almacenamiento en Data Lakes:**
   * *Caso:* Reducir el tamaño de almacenamiento de logs o transacciones masivas en CSV hasta un 80% manteniendo metadatos integrados.
2. **Preparación para Motores Analíticos (como DuckDB):**
   * *Caso:* Convertir fuentes de datos heredadas a Parquet para que herramientas modernas lean las columnas necesarias al instante sin escanear todo el fichero.

## Estructura del Proyecto
```text
D182-Parquet-Columnar-Storage/
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   └── parquet_pipeline.py
├── tests/
│   ├── __init__.py
│   └── test_parquet.py
├── mkdocs.yml
├── requirements.txt
└── README.md