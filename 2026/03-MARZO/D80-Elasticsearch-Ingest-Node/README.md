# Módulo D80: Elasticsearch Ingest Node (`Elasticsearch + Python`)

## Descripción General
Este proyecto implementa un cliente en Python utilizando la librería oficial de **Elasticsearch** para la indexación y búsqueda de texto completo sobre registros masivos de logs estructurados.

---

## Características Principales
* **Gestión de Índices**: Creación automatizada y verificación de índices en Elasticsearch.
* **Ingesta de Logs**: Inserción estructurada de documentos de registro con metadatos asociados.
* **Búsqueda de Texto Completo**: Consultas avanzadas basadas en coincidencia de texto (`match queries`).
* **Pruebas Aisladas**: Uso de mocks para validar la lógica de negocio sin requerir un cluster físico en ejecución durante el testing.

---

## Estructura del Proyecto
```text
D80-Elasticsearch-Ingest-Node/
├── src/
│   ├── __init__.py
│   └── search_client.py   # Lógica de conexión, indexación y búsqueda con Elasticsearch
├── tests/
│   ├── __init__.py
│   └── test_search_client.py # Pruebas unitarias con mocks
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación técnica del módulo