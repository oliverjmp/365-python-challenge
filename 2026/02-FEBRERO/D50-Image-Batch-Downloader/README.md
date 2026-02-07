### 🤖 Proyecto Día 50: Automated Image Batch Downloader 🖼️⚡

¡Medio centenar de días! Para este hito, hemos desarrollado una herramienta de extracción de activos multimedia. El script analiza el DOM de una página web, identifica recursos visuales y los descarga localmente gestionando flujos de datos binarios.

#### **Hitos Técnicos Alcanzados:**
1.  **Extracción de Atributos Multimedia:** Localización dinámica de etiquetas `<img>` y resolución de rutas mediante `urljoin`.
2.  **Gestión de Streams Binarios:** Uso de `requests` con `stream=True` para descargar archivos grandes de forma eficiente sin saturar la memoria RAM.
3.  **Persistencia en Disco (Modo 'wb'):** Escritura de datos en formato binario para preservar la integridad de archivos JPG, PNG y WebP.
4.  **Sanitización de Nombres:** Limpieza de extensiones y parámetros de URL para asegurar archivos válidos en Windows.

#### **Tecnologías Utilizadas:**
* **Requests:** Para la descarga de contenido binario.
* **BeautifulSoup4:** Para el mapeo de recursos en el HTML.
* **Pathlib:** Para la organización automática de la carpeta de descargas.