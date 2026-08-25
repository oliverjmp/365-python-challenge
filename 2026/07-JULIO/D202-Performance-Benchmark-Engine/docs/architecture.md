# Arquitectura del Hito D202

## 📊 Flujo de Benchmarking
El sistema opera bajo una secuencia optimizada:
1. **Generación de Datos:** Creación de un DataFrame base con un volumen configurable de registros.
2. **Registro en Motor Analítico:** Inyección del dataset en la instancia en memoria de DuckDB.
3. **Ejecución Cronometrada:** Evaluación de consultas de agregación (`GROUP BY` y `SUM`) bajo condiciones controladas con `timeit`.