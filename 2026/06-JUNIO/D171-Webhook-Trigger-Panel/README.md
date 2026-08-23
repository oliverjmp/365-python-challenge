# D171 - Webhook Trigger Panel

Panel de control operativo desarrollado con Streamlit y la librería Requests para el lanzamiento manual y monitoreo de webhooks y notificaciones de alerta en tiempo real.

## Características Principales
- **Lanzamiento Manual:** Envío personalizable de peticiones HTTP POST a endpoints externos o de prueba con payloads JSON.
- **Monitoreo de Respuestas:** Visualización instantánea del código de estado HTTP (`Status Code`), latencia y el cuerpo de la respuesta.
- **Auditoría de Eventos:** Registro de historial de ejecuciones dentro de la sesión interactiva.

## Estructura del Proyecto
```text
D171-Webhook-Trigger-Panel/
├── src/
│   ├── __init__.py
│   └── webhook_client.py
├── tests/
│   ├── __init__.py
│   └── test_webhook.py
├── app_webhook.py
├── requirements.txt
└── README.md