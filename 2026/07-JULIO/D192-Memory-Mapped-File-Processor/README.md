# D192 - Memory Mapped File Processor

Procesador de ficheros binarios masivos de alto rendimiento mediante el mapeo directo en la memoria virtual del sistema operativo utilizando el módulo nativo **`mmap`** de Python, almacenamiento persistente en el Data Lake e interfaz de consola avanzada con **`rich`**.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Persistencia Estructurada en Data Lake:** Creación y gestión de ficheros binarios pesados en la ruta `data_lake/binary_records.bin`.
2. **Mapeo en Memoria Virtual (`mmap`):** Acceso optimizado a disco sin sobrecargar la memoria RAM, ideal para procesar datasets o logs binarios gigantescos.
3. **Escaneo y Extracción con Rich:** Búsqueda ultrarrápida de patrones binarios expuesta mediante tablas estilizadas y paneles interactivos en consola.

## 💡 Casos de Uso del Mundo Real
- **Procesamiento de Logs Binarios Masivos:** Analizar gigabytes de registros de eventos en servidores sin agotar la memoria física del equipo.
- **Bases de Datos Embebidas e Índices:** Lectura directa de bloques de datos indexados en archivos estructurados de tamaño considerable.

## 📂 Estructura del Proyecto
```text
D192-Memory-Mapped-File-Processor/
├── data_lake/
│   └── binary_records.bin   # Fichero binario persistente gestionado por mmap
├── docs/
│   └── index.md             # Documentación técnica corporativa (MkDocs)
├── src/
│   ├── __init__.py
│   └── mmap_engine.py       # Motor lógico de mapeo en memoria virtual
├── tests/
│   ├── __init__.py
│   └── test_mmap_engine.py  # Pruebas unitarias con pytest
├── run_mmap_processor.py    # Script ejecutable principal con rich
├── mkdocs.yml               # Configuración del portal MkDocs
├── requirements.txt         # Dependencias del entorno
└── README.md                # Documentación técnica avanzada del hito