# D63: Advanced SQL Analytics & Financial Trends

## Descripción del Proyecto
Este módulo forma parte del **Reto de los 365 Días de Ingeniería de Datos y Python** (`365-Python-Challenge`)[cite: 1]. Su objetivo principal es demostrar el dominio de **SQL Avanzado** (Common Table Expressions - CTEs y Funciones de Ventana / Window Functions) ejecutado directamente desde Python sobre una base de datos SQLite persistente, delegando los cálculos analíticos pesados al motor relacional para garantizar escalabilidad y alto rendimiento.

## Enfoque Técnico
- **Base de Datos:** SQLite persistente con gestión transaccional robusta.
- **SQL Analítico:** Uso de `WITH` (CTEs) para modularizar consultas complejas, `AVG() OVER (ROWS BETWEEN...)` para medias móviles temporales y `LAG()` para comparativas de series temporales.
- **Validación de Datos:** Tipado estricto y validación de esquemas con **Pydantic v2**.
- **Resiliencia y Monitoreo:** Bloque de manejo de excepciones con **logging estructurado**.
- **Arquitectura:** Diseño modular limpio separando la conexión, las consultas, los modelos de datos y la orquestación principal.

## Estructura de Ficheros
```text
D63-Advanced-SQL-Analytics/
├── main.py              # Script principal de ejecución y orquestación
├── database.py          # Inicialización, conexión persistente y carga de datos simulados
├── models.py            # Esquemas de validación estricta con Pydantic v2
├── queries.py           # Repositorio de consultas SQL analíticas avanzadas
└── README.md            # Documentación técnica y de portafolio del módulo