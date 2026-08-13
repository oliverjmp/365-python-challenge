# D111 - Email Attachment Dispatcher

Este hito implementa un **sistema automatizado de envío de correos corporativos con reportes adjuntos cifrados**, combinando la librería estándar `smtplib` y `email.mime` con cifrado simétrico robusto mediante `cryptography`.

## Características Principales
- **Cifrado de Adjuntos:** Protección de datos sensibles mediante claves simétricas Fernet antes de la transferencia.
- **Estructura MIME Completa:** Soporte nativo para cuerpos de correo en HTML y múltiples partes adjuntas codificadas en Base64.
- **Automatización de Alertas:** Diseñado para integrarse en pipelines de generación de reportes financieros o de auditoría.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En la automatización de procesos empresariales (RPA y analítica), el envío desatendido de información es un pilar crítico. Permite:

### Ejemplos de Uso:
1. **Envío Automatizado de Estados Financieros Confidenciales:**
   * *Caso:* Enviar reportes generados automáticamente (como los del D110) a directivos de la empresa con cifrado de archivo por motivos de cumplimiento normativo (GDPR / privacidad).
2. **Alertas de Monitoreo de Seguridad:**
   * *Caso:* Enviar registros de logs o dumps de bases de datos cifrados a equipos de ciberseguridad ante incidentes críticos.
3. **Distribución Masiva de Facturas o Recibos de Nómina:**
   * *Caso:* Despachar correos personalizados a empleados con sus comprobantes protegidos con claves individuales.

## 📂 Estructura del Proyecto
```text
D111-Email-Attachment-Dispatcher/
│
├── src/
│   ├── __init__.py
│   └── dispatcher.py
├── tests/
│   └── test_dispatcher.py
├── run_dispatch.py
├── requirements.txt
└── README.md