## 📅 MES 2: Conectividad y Escalabilidad (Febrero ❄️)
> **Enfoque:** APIs, JSON, Web Scraping y Arquitecturas Distribuidas.

| Día | Fecha | Proyecto / Hito | Estado |
| :---: | :--- | :--- | :---: |
| 32 | 01-FEB | 🌐 Tracker de Cripto: Consumo de APIs y JSON | ✅ |

---

### 🛠️ Proyecto Destacado: Día 32 - Tracker de Criptomonedas 📈
He desarrollado un monitor de activos digitales que se conecta en tiempo real con la API de **CoinGecko**. Este proyecto marca el inicio de la integración de mi código con servicios en la nube.

#### **Hitos Técnicos Alcanzados:**
1.  **Protocolo HTTP:** Implementación de peticiones `GET` mediante la librería `requests`.
2.  **Manejo de JSON:** Serialización y deserialización de datos estructurados entre el servidor remoto y Python.
3.  **Status Codes & Handling:** Validación de conexión y manejo de excepciones en peticiones de red.
4.  **Persistencia Local:** Almacenamiento de snapshots de datos en archivos `.json` para trazabilidad histórica.

#### **Tecnologías Utilizadas:**
* **Requests:** Interacción con el endpoint de la API.
* **JSON Library:** Procesamiento de la respuesta del servidor.
* **Datetimes:** Estampado de tiempo para auditoría de precios.

---

### 🧠 Conceptos Clave de Hoy:
* **Endpoint:** La URL específica a la que apuntamos (`api.coingecko.com`).
* **Payload:** Los parámetros enviados (`ids`, `vs_currencies`) para filtrar la respuesta.
* **Serialization:** Proceso de convertir el JSON recibido en un diccionario de Python accesible.