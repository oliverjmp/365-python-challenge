# Módulo D89: Data Lineage Tracker (`Custom Python Engine`)

## Descripción General
Este módulo implementa un **motor personalizado de linaje de datos** en Python. Su propósito es auditar y rastrear las dependencias y transformaciones aplicadas a los conjuntos de datos a lo largo de un flujo ETL.

---

## Características Principales
* **Registro de Trazabilidad**: Vincula datasets de origen y destino mediante operaciones específicas.
* **Consulta de Linaje**: Permite inspeccionar el historial completo de transformaciones de cualquier conjunto de datos.
* **Diseño Extensible**: Estructura basada en clases para integrarse fácilmente en pipelines de datos complejos.

---

## Estructura del Proyecto
```text
D89-Data-Lineage-Tracker/
├── src/
│   ├── __init__.py
│   └── lineage_tracker.py # Implementación del motor de linaje de datos
├── tests/
│   ├── __init__.py
│   └── test_lineage.py # Pruebas unitarias del sistema de auditoría
├── requirements.txt # Dependencias del proyecto
└── README.md        # Documentación técnica del módulo