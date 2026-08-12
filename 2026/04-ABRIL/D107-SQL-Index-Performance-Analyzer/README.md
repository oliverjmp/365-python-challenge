# D107 - SQL Index Performance Analyzer

Este hito implementa un **analizador de rendimiento de consultas mediante la evaluación de planes de ejecución (`EXPLAIN`) y estrategias de optimización de índices** en bases de datos relacionales (SQLite / PostgreSQL).

## Características Principales
- **Inspección de Planes de Ejecución:** Análisis detallado de cómo el motor de base de datos procesa una consulta (`SCAN` vs `SEARCH`).
- **Optimización con Índices:** Creación dinámica de índices para reducir el costo de lectura en grandes volúmenes de datos.
- **Pruebas Unitarias Automatizadas:** Cobertura de código validada mediante `pytest`.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En sistemas de producción con bases de datos relacionales, una consulta mal escrita o sin los índices adecuados puede provocar bloqueos, lentitud extrema y uso excesivo de CPU. El uso de un analizador de planes de ejecución permite:

### Ejemplos de Uso:
1. **Auditoría de Consultas Lentas (Slow Query Monitoring):**
   * *Caso:* Una API experimenta retrasos al buscar usuarios por campos no indexados (como correo electrónico o estado).
   * *Uso:* Permite identificar si el motor está realizando un recorrido completo de la tabla (*Full Table Scan*) en lugar de una búsqueda indexada (*Index Search*).
2. **Optimización de Reportes Masivos (Business Intelligence):**
   * *Caso:* Consultas analíticas complejas que cruzan múltiples tablas con millones de filas.
   * *Uso:* Evaluar el impacto de crear índices compuestos para acelerar los filtros y uniones (`JOIN`).
3. **Desarrollo y CI/CD de Bases de Datos:**
   * *Caso:* Validar migraciones de esquemas y asegurar que las consultas críticas de los nuevos servicios mantengan un rendimiento óptimo antes de desplegar a producción.

## 📂 Estructura del Proyecto
```text
D107-SQL-Index-Performance-Analyzer/
│
├── src/
│   ├── __init__.py
│   └── analyzer.py
├── tests/
│   └── test_analyzer.py
├── requirements.txt
└── README.md