# FastAPI DuckDB Microservice (D188)

Microservicio web ultrarrápido para consulta de analíticas corporativas concurrentes basado en **FastAPI** y conexiones **DuckDB en modo Read-Only**.

## 🏛️ Arquitectura de Concurrencia Read-Only
1. **Aislamiento de Lectura Concurrente:** Al abrir DuckDB con `read_only=True`, múltiples hilos de ejecución atienden peticiones HTTP concurrentes de manera totalmente segura sin bloqueos de escritura.
2. **Baja Latencia In-Process:** Consultas analíticas vectoriales ejecutadas en milisegundos directamente expuestas mediante contratos API tipados con Pydantic.
3. **Ciclo de Vida Gestionado (`lifespan`):** Control robusto de inicialización y recursos de la base de datos subyacente.

---

## 📈 Endpoints Principales Disponibles

| Método | Endpoint | Descripción |
|:-------|:---------|:------------|
| `GET` | `/health` | Verificación del estado de salud del microservicio. |
| `GET` | `/api/ventas` | Listado paginado de transacciones analíticas. |
| `GET` | `/api/resumen/departamento` | Agregación de montos y conteo por área corporativa. |