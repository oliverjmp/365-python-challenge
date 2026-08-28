# D223 - Async Queue Producer-Consumer (Procesamiento Desacoplado)

Implementación robusta del patrón Productor-Consumidor asíncrono utilizando `asyncio.Queue` para la gestión eficiente y desacoplada de flujos de datos concurrentes con control de contrapresión.

---

## 🏛️ Explicación Profunda de la Arquitectura

### El Problema: Acoplamiento de Tiempos de Ejecución
Cuando un sistema genera datos a una velocidad diferente a la que puede procesarlos, los sistemas rígidos colapsan por falta de memoria o bloquean los hilos principales de ejecución.

### La Solución: Buffer Asíncrono y Contrapresión
`asyncio.Queue` actúa como un búfer intermedio seguro. Los productores depositan tareas sin importar quién las consuma, y los consumidores recogen elementos según su disponibilidad. El parámetro `maxsize` evita desbordamientos de memoria mediante el bloqueo inteligente del productor cuando el buffer está lleno.

---

## 💼 Casos de Uso Reales en Producción
1. **Sistemas de Mensajería y Event Streaming en Memoria:** Procesamiento asíncrono de webhooks entrantes en servidores API.
2. **Pipelines ETL con Múltiples Workers:** Extracción masiva de registros donde múltiples hilos de consumo insertan lotes en bases de datos.
3. **Encolado de Tareas en Background:** Gestión de notificaciones, envío de correos electrónicos o procesamiento de imágenes sin bloquear la respuesta al usuario.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar CLI de validación:**
  `python main.py`

- **Lanzar aplicación web interactiva (Streamlit):**
  `streamlit run app.py`

- **Levantar documentación local (MkDocs Enterprise):**
  `mkdocs serve`