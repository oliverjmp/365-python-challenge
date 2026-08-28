# D226 - Celery & Redis Task Queue

## 🏢 Resumen Ejecutivo y Alcance del Hito
El hito **D226** implementa una arquitectura estándar de la industria para el procesamiento asíncrono de tareas en segundo plano mediante la combinación de **Celery** y **Redis**. En aplicaciones empresariales de alta disponibilidad, las operaciones pesadas (como generación de reportes masivos, procesamiento de pagos, envíos de correos o ingesta de datos) no deben bloquear los hilos de respuesta de la API web. Este núcleo desacopla el ciclo de solicitud del usuario de la ejecución de la carga de trabajo.

---

## 📐 Pilares de Ingeniería
1. **Desacoplamiento de Solicitudes (Request/Response Cycle):** Las peticiones devuelven respuestas inmediatas al usuario mientras delegan el cómputo pesado a workers distribuidos.
2. **Redis como Message Broker:** Utilización de estructuras en memoria de ultra baja latencia para enrutar mensajes y almacenar estados de tareas.
3. **Escalabilidad Horizontal de Workers:** Capacidad de desplegar múltiples nodos de procesamiento en paralelo consumiendo de la misma cola centralizada.