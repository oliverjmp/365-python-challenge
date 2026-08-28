# D229 - Redis Pub/Sub Event Broker | Enterprise Core

## 📋 Visión General del Proyecto
El hito **D229** implementa un sistema de mensajería asíncrono y desacoplado basado en eventos utilizando el patrón **Publish/Subscribe (Pub/Sub) de Redis**. Este componente está diseñado para resolver los desafíos de comunicación en arquitecturas orientadas a eventos (EDA) y microservicios, permitiendo la difusión de mensajes en tiempo real sin acoplamiento temporal ni espacial entre emisores y receptores.

---

## 🎯 Casos de Uso Empresariales

### Caso de Uso 1: Notificaciones Transaccionales en Tiempo Real
* **Contexto:** Cuando un usuario realiza una compra o transacción crítica en la plataforma principal, múltiples sistemas periféricos (pasarela de pagos, servicio de inventario y alertas por correo) deben reaccionar de forma inmediata.
* **Implementación con D229:** El microservicio de transacciones publica un evento de tipo `ORDER_CREATED` en el canal `orders`. Los suscriptores independientes capturan el evento al instante y ejecutan sus respectivas lógicas de negocio sin bloquear el hilo principal de la compra.

### Caso de Uso 2: Sincronización de Sesiones y Telemetría Distribuida
* **Contexto:** Monitorear eventos de inicio de sesión de usuarios o telemetría de sistemas distribuidos para auditoría de seguridad y análisis de rendimiento.
* **Implementación con D229:** Se utilizan canales específicos (`telemetry`, `notifications`) donde los nodos emisores difunden métricas que un servicio central de auditoría consume mediante escucha activa.

---

## 🏛️ Arquitectura y Patrones de Diseño

El sistema opera bajo un modelo de **Difusión (Broadcasting)** desacoplado:
* **Productores (`EventPublisher`):** Encapsulan la lógica de serialización de mensajes a formato JSON y emiten cargas útiles a canales lógicos en Redis mediante el comando `PUBLISH`.
* **Consumidores (`EventSubscriber`):** Mantienen conexiones persistentes a los canales suscritos mediante sockets de Redis (`PUBSUB`), procesando los eventos entrantes a través de funciones de retrollamada (*callbacks*) seguras con control de tiempo de espera (*timeouts*).

---

## 🚀 Guía de Instalación y Ejecución

### 1. Requisitos Previos
* Python 3.11+
* Servidor Redis activo (local en `localhost:6379` o mediante Docker).

### 2. Instalación de Dependencias
```bash
pip install -r requirements.txt