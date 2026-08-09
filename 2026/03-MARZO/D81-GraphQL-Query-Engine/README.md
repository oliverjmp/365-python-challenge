# Módulo D81: GraphQL Query Engine (`Strawberry + Python`)

## Descripción General
Este proyecto implementa un motor y servidor de consultas **GraphQL** utilizando la librería moderna **Strawberry** en Python. Su propósito es ofrecer una alternativa flexible a las APIs REST tradicionales para la consulta estructurada de registros de logs.

---

## Características Principales
* **Tipado Estricto**: Definición de esquemas basados en clases de Python y decoradores de Strawberry (`@strawberry.type`, `@strawberry.field`).
* **Consultas Flexibles**: Capacidad de solicitar únicamente los campos necesarios y aplicar filtros avanzados en una sola petición.
* **Pruebas Asíncronas**: Validación del esquema y resolución de consultas mediante ejecuciones asíncronas con `pytest`.

---

## Estructura del Proyecto
```text
D81-GraphQL-Query-Engine/
├── src/
│   ├── __init__.py
│   └── schema.py      # Definición de tipos, base de datos simulada y esquema GraphQL
├── tests/
│   ├── __init__.py
│   └── test_schema.py # Pruebas unitarias asíncronas del motor de consultas
├── requirements.txt   # Dependencias del proyecto
└── README.md          # Documentación técnica del módulo