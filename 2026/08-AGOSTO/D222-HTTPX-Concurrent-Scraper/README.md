# D222 - HTTPX Concurrent Scraper (Ingesta Masiva Keep-Alive)

Diseño e implementación de un motor de scraping e ingesta web asíncrona de alta densidad optimizado mediante conexiones persistentes Keep-Alive y HTTP/2 con `httpx`.

---

## 🏛️ Explicación Profunda de la Arquitectura

### El Problema: Latencia por Apertura de Sockets
En la ingesta masiva tradicional, abrir una conexión HTTP independiente para cada URL requiere un proceso costoso de resolución DNS, enlace TCP y negociación criptográfica TLS. Multiplicado por miles de peticiones, esto genera cuellos de botella severos en la red.

### La Solución: HTTPX AsyncClient y Keep-Alive
El uso de `httpx.AsyncClient` con límites de conexiones configurados permite **reutilizar un pool de conexiones TCP abiertas**, reduciendo el tiempo total de ingesta exponencialmente y protegiendo los recursos del sistema operativo.

---

## 💼 Casos de Uso Reales en Producción
1. **Monitoreo Financiero y de Precios en Tiempo Real:** Extracción concurrente masiva de catálogos de e-commerce o tickers bursátiles.
2. **Threat Intelligence y Ciberseguridad:** Escaneo y validación simultánea de miles de URLs o dominios sospechosos.
3. **ETL de APIs Externas:** Sincronización masiva de datos distribuidos en múltiples microservicios de terceros.

---

## 🚀 Comandos de Ejecución y Validación

- **Instalar dependencias:**
  `pip install -r requirements.txt`

- **Ejecutar pruebas unitarias (Cobertura estricta al 100%):**
  `python -m pytest --cov=src --cov-fail-under=100 --cov-report=term-missing --cache-clear`

- **Ejecutar CLI de validación:**
  `python main.py`

- **Lanzar aplicación web interactiva (Streamlit):**
  `streamlit run app.py`

- **Levantar documentación local (MkDocs Enterprise):**
  `mkdocs serve`