### 🤖 Proyecto Día 52: Session Persistence & POST Login 🔐

Hoy implementamos la persistencia de estado. Hemos dejado de realizar peticiones aisladas para gestionar un flujo de navegación completo. El bot ahora es capaz de recibir, almacenar y reenviar cookies de sesión automáticamente.

#### **Hitos Técnicos Alcanzados:**
1.  **Requests Session Object:** Creación de una instancia persistente que mantiene cookies y headers durante toda la ejecución.
2.  **Protocolo POST:** Envío de datos sensibles (credenciales) en el cuerpo de la petición, emulando un formulario de inicio de sesión.
3.  **Cookie Management:** Análisis de cómo el servidor identifica al bot mediante tokens de sesión tras una autenticación exitosa.
4.  **Acceso Condicional:** Verificación de acceso a rutas protegidas que requieren una sesión activa.

#### **Tecnologías Utilizadas:**
* **Requests (Session):** Para el mantenimiento automático del estado.
* **HTTP Methods (GET/POST):** Para la interacción completa con el servidor.