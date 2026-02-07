### 🤖 Proyecto Día 47: Web Scraping Foundations 🌐🕷️

Hoy iniciamos la extracción automatizada de datos externos. El objetivo es aprender a realizar peticiones HTTP seguras y parsear el código fuente de una web para convertir texto desordenado en datos estructurados.

#### **Hitos Técnicos Alcanzados:**
1.  **Protocolo HTTP con `requests`:** Gestión de peticiones GET y manejo de códigos de estado (200 OK, 404 Not Found).
2.  **Parsing de HTML con `BeautifulSoup`:** Navegación por el DOM (Document Object Model) para localizar etiquetas específicas (`h1`, `p`, `a`).
3.  **User-Agent Spoofing:** Configuración de cabeceras para que nuestra petición parezca provenir de un navegador real, evitando bloqueos básicos.
4.  **Extracción Selectiva:** Filtrado de elementos por ID y Clase para obtener información precisa sin ruido.

#### **Tecnologías Utilizadas:**
* **Requests:** La librería estándar de facto para peticiones HTTP.
* **BeautifulSoup4:** Para navegar y buscar dentro del árbol HTML.
* **LXML:** Parser de alto rendimiento para procesar el HTML.