# D189 - Pydantic Query Validator

Micro-librería especializada en validación estricta de parámetros de entrada para APIs analíticas, construida con **Pydantic v2** y un **SQL Sanitizer** heurístico basado en expresiones regulares[cite: 1].

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Interceptación Temprana (`@field_validator` en modo `before`):** Permite inspeccionar y limpiar los datos crudos antes de que el motor de tipos comience su validación estructural[cite: 1].
2. **Prevención Proactiva de Inyecciones SQL:** Bloqueo automatizado de comentarios maliciosos, comandos destructivos (`DROP TABLE`) y tautologías lógicas (`OR 1=1`)[cite: 1].
3. **Contratos de Datos Confiables:** Garantía estricta de formatos de fecha mediante patrones Regex y control estricto de rangos numéricos.

## 💼 Casos Prácticos en el Mundo Real
- **Seguridad en Endpoints de Microservicios Backend:** Blindar peticiones HTTP entrantes en APIs desarrolladas con FastAPI para evitar manipulaciones de consultas hacia motores de bases de datos analíticas (DuckDB, Snowflake, PostgreSQL).
- **Garantía de Integridad en Sistemas de Business Intelligence:** Asegurar que los filtros y métricas enviados desde tableros interactivos o clientes externos cumplan rígidamente con las reglas de negocio antes de consumir recursos de cómputo pesados.

## 📂 Estructura del Proyecto
```text
D189-Pydantic-Query-Validator/
├── data_lake/
├── docs/
│   └── index.md
├── src/
│   ├── __init__.py
│   └── query_validator.py
├── tests/
│   ├── __init__.py
│   └── test_validator.py
├── mkdocs.yml
├── requirements.txt
└── README.md