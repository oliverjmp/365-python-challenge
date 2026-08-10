# Módulo D82: Webhook Dispatcher System (`Requests + HMAC`)

## Descripción General
Este proyecto implementa un sistema emisor y receptor de **Webhooks seguros**, firmados criptográficamente mediante **HMAC-SHA256**, garantizando la integridad y autenticidad de los eventos transmitidos en tiempo real.

---

## Características Principales
* **Firma Criptográfica**: Uso de HMAC y SHA-256 para estampar un sello único en cada petición saliente.
* **Validación Segura en Destino**: FastAPI procesa los encabezados y utiliza `hmac.compare_digest` para prevenir ataques de temporización (*timing attacks*).
* **Pruebas Automatizadas**: Cobertura integral de escenarios válidos, firmas ausentes y firmas manipuladas.

---

## Estructura del Proyecto
```text
D82-Webhook-Dispatcher-System/
├── src/
│   ├── __init__.py
│   ├── dispatcher.py    # Lógica del emisor y generación de HMAC
│   └── receiver.py      # Servidor FastAPI receptor y validador de seguridad
├── tests/
│   ├── __init__.py
│   └── test_webhook.py  # Pruebas unitarias de integración de seguridad
├── requirements.txt     # Dependencias del proyecto
└── README.md            # Documentación técnica del módulo