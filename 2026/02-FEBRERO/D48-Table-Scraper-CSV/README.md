### 🤖 Proyecto Día 48: HTML Table Scraper to CSV 📊💾

El objetivo de hoy es la extracción masiva de datos estructurados. Hemos pasado de leer etiquetas sueltas a procesar estructuras complejas (`<table>`), iterando sobre sus filas (`<tr>`) y celdas (`<td>`) para generar un dataset exportable.

#### **Hitos Técnicos Alcanzados:**
1.  **Iteración de Estructuras Anidadas:** Uso de `find_all` para recorrer dinámicamente el cuerpo de una tabla sin conocer su tamaño previo.
2.  **Data Cleaning:** Implementación de limpieza de strings para eliminar ruidos de formato HTML (espacios extras, caracteres especiales).
3.  **Serialización a CSV:** Uso de la librería `csv` de Python para garantizar que los datos extraídos sean compatibles con Excel o Pandas.
4.  **Manejo de Cabeceras Dinámicas:** Extracción automática de los nombres de las columnas desde la etiqueta `<thead>`.

#### **Tecnologías Utilizadas:**
* **BeautifulSoup4:** Para la segmentación de filas y columnas.
* **CSV Module:** Para la persistencia de datos en formato tabular.
* **Requests:** Para la captura del código fuente.