# D221 - Asyncio Event Loop Core (Concurrencia de Alta Densidad)

Diseño e implementación de un núcleo de procesamiento asíncrono basado en el bucle de eventos nativo de Python (`asyncio`) para la gestión optimizada de tareas concurrentes masivas de tipo I/O.

---

## 🏛️ Explicación Profunda de la Arquitectura Asíncrona

### El Problema: Bloqueo en Operaciones de I/O
En sistemas síncronos tradicionales, cada solicitud de red, lectura de disco o consulta a base de datos detiene la ejecución del hilo principal hasta recibir una respuesta. Esto degrada drásticamente la escalabilidad cuando se manejan miles de peticiones simultáneas.

### La Solución: El Bucle de Eventos y Corrutinas Cooperativas
El modelo asíncrono permite que, en lugar de bloquear el hilo, una tarea suspenda su ejecución (`await`) mientras espera el recurso externo, cediendo el control al bucle de eventos para procesar otras tareas activas. Esto maximiza el rendimiento utilizando un único hilo físico del procesador.

---

## 💼 Casos de Uso Reales en Producción
1. **Scrapers y Crawlers Web de Alto Rendimiento:** Descarga masiva concurrente de miles de páginas web sin agotar los descriptores de archivos ni saturar la memoria RAM.
2. **Microservicios y APIs Asíncronas (FastAPI / WebSockets):** Manejo simultáneo de miles de conexiones de clientes en tiempo real.
3. **Pipelines de Ingesta ETL Distribuidos:** Conexiones concurrentes a múltiples APIs externas para extracción de datos en paralelo.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias asíncronas (Garantizando el 100.00% de cobertura):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar validación mediante CLI:**
  `python main.py`

- **Levantar documentación local:**
  `mkdocs serve`