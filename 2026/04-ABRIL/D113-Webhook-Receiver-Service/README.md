# D113 - Webhook Receiver Service

Este hito implementa un **receptor seguro de notificaciones externas mediante la validación de firmas criptográficas HMAC (Hash-based Message Authentication Code)** utilizando **FastAPI**.

## Características Principales
- **Validación Criptográfica HMAC-SHA256:** Garantiza la autenticidad e integridad de los datos recibidos mediante claves compartidas.
- **Protección contra Timing Attacks:** Uso de `hmac.compare_digest` para evitar ataques de análisis de tiempo en las cadenas de firma.
- **API Moderna con FastAPI:** Recepción eficiente de solicitudes HTTP asíncronas con tipado estricto mediante Pydantic.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
Los webhooks permiten que sistemas externos (como pasarelas de pago, GitHub, Stripe o ERPs) notifiquen eventos en tiempo real a nuestras aplicaciones. Validar su firma evita que atacantes inyecten eventos falsos o suplanten identidades.

### Ejemplos de Uso:
1. **Integración con Pasarelas de Pago (Stripe / PayPal):**
   * *Caso:* Recibir notificaciones automáticas cuando un cargo se complete exitosamente.
   * *Uso:* Validar la firma criptográfica enviada en los headers antes de actualizar el estado de la orden en la base de datos.
2. **Webhooks de Repositorios de Código (GitHub / GitLab CI/CD):**
   * *Caso:* Disparar despliegues automatizados o pipelines de pruebas cuando se realice un `git push`.
   * *Uso:* Asegurar que únicamente eventos originados desde la plataforma oficial disparen acciones en los servidores internos.

## 📂 Estructura del Proyecto
```text
D113-Webhook-Receiver-Service/
│
├── src/
│   ├── __init__.py
│   └── receiver.py
├── tests/
│   └── test_receiver.py
├── run_webhook.py
├── requirements.txt
└── README.md