# D187 - Partitioned-Dataset-Manager

Plataforma de ingeniería de datos para la escritura y lectura eficiente de datasets masivos particionados jerárquicamente por criterios de fecha y región geográfica utilizando **PyArrow Datasets**.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Organización Jerárquica de Ficheros:** Creación automática de estructuras de directorios particionadas (`region` / `fecha`) sobre formato columnar Parquet.
2. **Partition Pruning y Predicate Pushdown:** Filtrado inteligente a nivel físico de directorios para evitar lecturas innecesarias en disco.
3. **Ecosistema Completo:** Pruebas unitarias de cobertura con pytest y documentación técnica automatizada con MkDocs.

## 💼 Casos Prácticos en el Mundo Real
- **Gestión de Data Lakes Multi-región:** Almacenamiento optimizado de transacciones globales donde las consultas analíticas de los equipos locales solo leen las particiones correspondientes a su zona geográfica y rango de fechas específico, reduciendo costes de I/O en la nube.
- **Procesamiento de Series Temporales Masivas:** Organización de registros de IoT, telemetría o logs particionados por día/mes, permitiendo a los pipelines de Machine Learning cargar únicamente las ventanas temporales requeridas para el entrenamiento de modelos sin agotar la memoria RAM.

## 📂 Estructura del Proyecto
```text
D187-Partitioned-Dataset-Manager/
├── data_lake/             # Almacenamiento de datasets particionados
├── docs/
│   └── index.md           # Portal de documentación técnica (MkDocs)
├── src/
│   ├── __init__.py
│   ├── dataset_manager_engine.py  # Motor de particionado y lectura selectiva
│   └── main_demo.py       # Script ejecutable principal de consola
├── tests/
│   ├── __init__.py
│   └── test_dataset_manager.py   # Pruebas unitarias con pytest
├── mkdocs.yml             # Configuración del portal MkDocs
├── requirements.txt       # Dependencias del entorno de desarrollo
└── README.md              # Documentación técnica avanzada del hito