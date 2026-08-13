# D112 - Telegram Alert Bot

Este hito implementa un **sistema de alertas operativas en tiempo real ante fallos críticos en pipelines de datos** utilizando la API HTTP oficial de Telegram Bots mediante `requests`.

## Características Principales
- **Integración con Telegram Bot API:** Envío automatizado de mensajes instantáneos con soporte para formato Markdown.
- **Manejo de Errores de Red:** Control robusto de excepciones ante caídas de conexión o respuestas inválidas de la API.
- **Monitoreo de Infraestructura:** Diseñado para acoplarse directamente a flujos de datos y notificar incidencias críticas de forma inmediata.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En arquitectura de datos y operaciones (DataOps), la visibilidad inmediata de los fallos evita la propagación de errores analíticos:

### Ejemplos de Uso:
1. **Alertas de Fallos en Pipelines ETL:**
   * *Caso:* Notificar automáticamente al equipo de ingeniería de datos cuando una tarea de extracción o carga falle por timeouts o problemas de esquemas.
2. **Monitoreo de Cierres Financieros Automatizados:**
   * *Caso:* Enviar un reporte rápido vía chat cuando los modelos financieros generados en hitos anteriores (ej. D110) terminen su ejecución con éxito o error.
3. **Control de Disponibilidad de Servidores y APIs:**
   * *Caso:* Disparar notificaciones prioritarias al detectar códigos de estado HTTP erróneos en servicios web corporativos críticos.

## 📂 Estructura del Proyecto
```text
D112-Telegram-Alert-Bot/
│
├── src/
│   ├── __init__.py
│   └── bot.py
├── tests/
│   └── test_bot.py
├── run_alert.py
├── requirements.txt
└── README.md