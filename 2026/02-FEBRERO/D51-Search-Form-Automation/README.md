### 🤖 Proyecto Día 51: Search Form Automation & Query Injection 🔍💉

Hoy elevamos el nivel de interacción. Pasamos del scraping pasivo a la manipulación activa de motores de búsqueda. El objetivo es automatizar el envío de formularios de consulta mediante parámetros HTTP para obtener resultados específicos de forma dinámica.

#### **Hitos Técnicos Alcanzados:**
1.  **Payload Construction:** Uso del diccionario `params` en `requests` para codificar automáticamente términos de búsqueda (manejando espacios y caracteres especiales).
2.  **Protocolo GET vs Query Strings:** Análisis de cómo las URLs cambian al realizar una búsqueda y cómo replicar ese comportamiento desde Python.
3.  **Selector Strategy:** Implementación de selectores CSS específicos (`.mw-search-result-heading`) para aislar resultados relevantes entre el ruido visual de la web.
4.  **URL Reconstruction:** Generación de enlaces absolutos a partir de rutas relativas obtenidas del motor de búsqueda.

#### **Tecnologías Utilizadas:**
* **Requests (Parameter Mapping):** Para la inyección limpia de consultas.
* **BeautifulSoup (CSS Selection):** Para el mapeo de los nodos de resultados.