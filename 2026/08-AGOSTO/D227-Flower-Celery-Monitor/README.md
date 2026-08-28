# D227 - Celery Flower Monitor (Monitoreo en Tiempo Real)

Implementación y panel de control web para la supervisión del estado, métricas de rendimiento y trazabilidad de tareas distribuidas en workers de Celery con Flower.

---

## 🏛️ Explicación Profunda de la Arquitectura

### El Problema: La Caja Negra en Procesamiento Distribuido
Cuando una aplicación escala a decenas o cientos de tareas concurrentes ejecutándose en workers remotos, diagnosticar fallos, cuellos de botella o tareas colgadas a través de registros (*logs*) de texto plano resulta ineficiente e insostenible.

### La Solución: Celery Flower
Flower se conecta al backend y al broker de Celery para escuchar eventos en tiempo real, ofreciendo un tablero web interactivo que permite visualizar el estado de cada tarea, reiniciar workers, inspeccionar argumentos y revocar ejecuciones bloqueadas de forma instantánea.

---

## 💼 Casos de Uso Reales en Producción
1. **Sistemas de Alerta Temprana (SRE):** Detección inmediata de picos de tareas fallidas (*FAILED*) por problemas de red o base de datos.
2. **Auditoría de Carga de Trabajo:** Análisis de tiempos de ejecución promedio para optimizar la asignación de recursos en clústeres de producción.
3. **Gestión Operativa de Cola:** Capacidad de purgar colas o cancelar tareas huérfanas con un solo clic.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar CLI de validación:**
  `python main.py`

- **Lanzar servidor Flower (requiere Redis activo en puerto 6379):**
  `flower -A src.celery_app.celery_app --port=5555` *(Luego visita `http://localhost:5555`)*

- **Lanzar panel web interactivo de simulación (Streamlit):**
  `streamlit run app.py`

- **Levantar documentación local (MkDocs Enterprise):**
  `mkdocs serve`