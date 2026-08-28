# D228 - FastAPI Celery Trigger

Microservicio web en FastAPI equipado con colas de tareas asíncronas en segundo plano mediante Celery y Redis.

---

## 🏛️ Explicación Profunda

### El Problema: Bloqueo de Hilos en APIs Web
Cuando una petición HTTP requiere procesar cargas pesadas (como generar un reporte masivo, enviar lotes de correos o realizar cálculos complejos), mantener la conexión abierta bloquea el servidor web, agotando las conexiones disponibles y provocando caídas de servicio.

### La Solución: Patrón Trigger-Asíncrono con Celery
FastAPI actúa como una puerta de enlace rápida que acepta la orden, encola la tarea en Redis y devuelve un identificador instantáneamente. Un worker independiente consume la tarea de forma paralela sin afectar la disponibilidad de la API.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Lanzar servidor FastAPI:**
  `uvicorn src.main:app --reload --port=8000` *(Visita `http://localhost:8000/docs` para probar los endpoints interactivos)*

- **Levantar documentación local (MkDocs Enterprise):**
  `mkdocs serve`