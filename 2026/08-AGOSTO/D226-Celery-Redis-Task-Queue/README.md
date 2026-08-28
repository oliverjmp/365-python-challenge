# D226 - Celery & Redis Task Queue (Tareas en Segundo Plano)

Implementación robusta de una cola de tareas distribuidas utilizando Celery y Redis para el procesamiento asíncrono y desacoplado de cargas de trabajo pesadas en entornos empresariales.

---

## 🏛️ Explicación Profunda de la Arquitectura

### El Problema: Bloqueo de Hilos en Aplicaciones Web
Cuando una aplicación web recibe una petición que requiere procesamiento intensivo, mantener la conexión HTTP abierta provoca bloqueos de recursos, tiempos de espera elevados (*timeouts*) y una experiencia de usuario deficiente.

### La Solución: Arquitectura de Broker y Workers
Celery actúa como el enrutador de tareas, empaquetando argumentos y metadatos en un mensaje JSON que se deposita instantáneamente en Redis (Broker). Los workers independientes recogen los mensajes, ejecutan las funciones en segundo plano y registran los resultados en el backend.

---

## 💼 Casos de Uso Reales en Producción
1. **Generación de Reportes y Exportación Masiva:** Procesamiento de archivos PDF o Excel pesados fuera del ciclo web.
2. **Plataformas de Comercio Electrónico:** Procesamiento asíncrono de pasarelas de pago y confirmaciones de inventario.
3. **Notificaciones y Mailing Masivo:** Envío masivo de correos electrónicos transaccionales y notificaciones push.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar CLI de validación:**
  `python main.py`

- **Lanzar worker de Celery (requiere servidor Redis activo en puerto 6379):**
  `celery -A src.celery_app.celery_app worker --loglevel=info`

- **Lanzar aplicación web interactiva (Streamlit):**
  `streamlit run app.py`

- **Levantar documentación local (MkDocs Enterprise):**
  `mkdocs serve`