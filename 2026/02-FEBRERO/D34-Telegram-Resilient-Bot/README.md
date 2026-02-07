### 🤖 Proyecto Día 34: Bot de Volatilidad con Notificaciones Telegram 📱
En este hito, el pipeline de datos sale de la consola local y se conecta con el usuario a través de la mensajería instantánea. El sistema ahora es capaz de vigilar el mercado y "avisar" de forma proactiva mediante la API de Telegram.

#### **Hitos Técnicos Alcanzados:**
1.  **Integración de Webhooks/APIs:** Conexión con `api.telegram.org` utilizando peticiones `POST` para el envío de alertas push.
2.  **Blindaje de Datos (Error Handling):** * Implementación de detección de **Rate Limiting (HTTP 429)** para evitar baneos de IP.
    * Validación de existencia de llaves en el JSON (`if 'bitcoin' in datos`) para prevenir cierres inesperados del programa.
3.  **Lógica de Umbral Sensible:** Configuración de un disparador de volatilidad al **0.01%**, permitiendo un filtrado inteligente entre variaciones irrelevantes ("Estable") y movimientos críticos ("Alerta").
4.  **Resiliencia del Sistema:** Capacidad de recuperación automática ante errores inesperados mediante bloques `try-except` globales.



#### **Tecnologías Utilizadas:**
* **Requests:** Para la comunicación bidireccional con servidores externos.
* **Telegram Bot API:** Interfaz de salida para notificaciones al móvil.
* **JSON:** Formato de intercambio de datos entre la nube y el script local.

---

### 📊 Ejemplo de Flujo de Trabajo:
1. **Consulta:** El bot pide el precio a CoinGecko cada 30 segundos.
2. **Análisis:** Compara `precio_actual` vs `precio_anterior`.
3. **Decisión:** - Si $\Delta\% > 0.01$: Envía mensaje a Telegram + Log en consola.
   - Si $\Delta\% \le 0.01$: Solo registra el estado en consola como "Estable".

---

### 🧠 Lección del Día:
La importancia de la **estabilidad del servicio**. Un bot que se apaga ante el primer error de red no es útil; un bot resiliente que sabe esperar (wait-and-retry) es una herramienta de grado profesional.