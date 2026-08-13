# D117 - Design Pattern Observer

Este hito implementa el **patrón de comportamiento Observer (Observador) para la gestión desacoplada de eventos en arquitecturas de pipelines de datos**.

## Características Principales
- **Desacoplamiento de Componentes:** Permite que un objeto (Sujeto/Publisher) notifique cambios a múltiples dependencias (Observadores) sin conocer sus detalles internos.
- **Suscripción Dinámica:** Capacidad de adjuntar (`attach`) o desvincular (`detach`) observadores en tiempo de ejecución.
- **Gestión Centralizada de Eventos:** Ideal para disparar registros de auditoría, métricas de rendimiento o alertas automáticas al cambiar el estado de un flujo.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
En arquitectura de software y flujos de datos modernos, los componentes no deben estar fuertemente acoplados entre sí.

### Ejemplos de Uso:
1. **Sistemas de Notificación y Alertas en Pipelines ETL:**
   * *Caso:* Cuando un pipeline inicia, finaliza con éxito o falla, múltiples subsistemas (como dashboards de métricas, bots de Telegram del D112 y sistemas de logs) necesitan enterarse simultáneamente sin que el pipeline principal maneje la lógica de cada uno.
2. **Arquitecturas Basadas en Eventos (Event-Driven):**
   * *Caso:* Disparar disparadores automáticos ante modificaciones de estado en modelos de negocio u objetos de dominio.

## 📂 Estructura del Proyecto
```text
D117-Design-Pattern-Observer/
│
├── src/
│   ├── __init__.py
│   └── pipeline_observer.py
├── tests/
│   └── test_observer.py
├── run_observer.py
├── requirements.txt
└── README.md