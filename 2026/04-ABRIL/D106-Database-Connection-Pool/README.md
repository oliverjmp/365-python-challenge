# D106 - Database Connection Pool

Este hito implementa una **gestión eficiente de grupos de conexiones concurrentes a bases de datos relacionales** utilizando el motor de **SQLAlchemy Pool**.

## Características Principales
- **Control de Concurrencia:** Configuración avanzada de `pool_size` y `max_overflow` para regular las conexiones simultáneas.
- **Monitoreo de Estado:** Métricas en tiempo real de conexiones activas, inactivas y disponibles en el pool.
- **Pruebas Unitarias:** Cobertura validada mediante `pytest`.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En aplicaciones profesionales, abrir y cerrar una conexión a la base de datos por cada petición de usuario consume demasiados recursos y satura el servidor. El uso de un *Connection Pool* resuelve esto manteniendo un grupo de conexiones abiertas y listas para ser reutilizadas.

### Ejemplos de Uso:
1. **APIs Web de Alta Concurrencia (FastAPI / Flask):**
   * *Caso:* Múltiples usuarios consultan datos simultáneamente en una tienda online.
   * *Uso:* El pool asigna una conexión disponible a cada petición HTTP de forma inmediata, evitando que la base de datos colapse por exceso de conexiones concurrentes (*Too many connections*).
2. **Procesamiento Masivo de Datos (ETL):**
   * *Caso:* Inserción de miles de registros leídos desde archivos CSV a una base de datos relacional.
   * *Uso:* El script solicita conexiones del pool por lotes, optimizando el tiempo de ejecución al evitar el costo de abrir una nueva conexión por cada fila insertada.
3. **Microservicios con Background Workers (Celery / Daemons):**
   * *Caso:* Tareas en segundo plano que ejecutan consultas periódicas de auditoría o limpieza de tablas.
   * *Uso:* Permite reutilizar la misma instancia del motor de base de datos durante todo el ciclo de vida del proceso en segundo plano de forma segura.
4. **Pruebas Automatizadas Rápidas (Testing):**
   * *Caso:* Ejecución de pruebas unitarias sobre bases de datos en memoria (`sqlite:///:memory:`).
   * *Uso:* Permite aislar entornos de prueba con ciclos de vida de conexión controlados y limpios.

## 📂 Estructura del Proyecto
```text
D106-Database-Connection-Pool/
│
├── src/
│   ├── __init__.py
│   └── db_pool.py
├── tests/
│   └── test_db_pool.py
├── requirements.txt
└── README.md