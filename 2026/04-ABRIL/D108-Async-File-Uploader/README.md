# D108 - Async File Uploader

Este hito implementa un **servicio asíncrono para la transferencia concurrente de ficheros pesados a servidores remotos** utilizando `asyncio` y `httpx`.

## Características Principales
- **Concurrencia Nativa:** Uso de `asyncio.gather` para enviar múltiples ficheros en paralelo sin bloquear el hilo principal.
- **Cliente HTTP No Bloqueante:** Implementación robusta con `httpx.AsyncClient`.
- **Pruebas Unitarias Asíncronas:** Cobertura validada mediante `pytest-asyncio` y simulación de respuestas de red con `respx`.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En arquitecturas modernas orientadas a microservicios y procesamiento de datos, la transferencia síncrona y secuencial de archivos pesados genera graves cuellos de botella e ineficiencia de recursos. El uso de cargas asíncronas concurrentes permite:

### Ejemplos de Uso:
1. **Sincronización de Lotes de Imágenes o Documentos (Cloud Storage):**
   * *Caso:* Una aplicación empresarial necesita respaldar y subir cientos de documentos escaneados o imágenes de alta resolución a un servidor de almacenamiento remoto o S3.
   * *Uso:* Reduce drásticamente el tiempo total de transferencia al realizar las peticiones HTTP en paralelo mediante E/S asíncrona.
2. **Ingesta de Logs o Reportes Masivos:**
   * *Caso:* Enviar periódicamente ficheros de registros operativos (*logs*) comprimidos desde múltiples nodos de procesamiento hacia un servidor centralizado de auditoría.
   * *Uso:* Evita bloqueos en el hilo de ejecución principal del software, permitiendo que la aplicación siga respondiendo a otras tareas concurrentes.
3. **Integración con APIs de Terceros con Alta Latencia:**
   * *Caso:* Consumir endpoints remotos donde cada subida de archivo experimenta demoras de red.
   * *Uso:* Maximiza el aprovechamiento del ancho de banda y los tiempos de espera (*I/O bound*) ejecutando las peticiones de forma simultánea.

## 📂 Estructura del Proyecto
```text
D108-Async-File-Uploader/
│
├── src/
│   ├── __init__.py
│   └── uploader.py
├── tests/
│   └── test_uploader.py
├── requirements.txt
└── README.md