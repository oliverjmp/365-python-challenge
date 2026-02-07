### 🤖 Proyecto Día 49: Recursive Web Crawler 🕷️🪜

Hoy implementamos un motor de navegación secuencial. El script ya no es estático; ahora es capaz de descubrir enlaces, "saltar" a nuevas URLs, extraer datos profundos y mantener un estado de recolección persistente.

#### **Hitos Técnicos Alcanzados:**
1.  **Lógica de Crawling:** Implementación de un flujo de "Landing -> Discovery -> Extraction".
2.  **Manejo de Cortesía (Polite Scraping):** Introducción de `time.sleep()` para evitar sobrecargar servidores y prevenir bloqueos de IP.
3.  **Normalización de URLs:** Uso de `urljoin` para convertir rutas relativas (`/wiki/Python`) en rutas absolutas funcionales.
4.  **Recolección Selectiva:** Filtrado de enlaces relevantes para evitar que el bot se pierda en secciones innecesarias (como menús laterales o pies de página).

#### **Tecnologías Utilizadas:**
* **Requests & BeautifulSoup:** El núcleo de conexión y parseo.
* **Time:** Para la gestión de intervalos entre peticiones.
* **Urllib.parse:** Para la reconstrucción inteligente de URLs.