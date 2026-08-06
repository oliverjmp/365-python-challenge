# Día 66 — Playwright Dynamic Scraper 🚀

## 📋 Descripción del Proyecto
El **Día 66** continúa la **Fase 3** del reto, abordando un problema clásico de ingeniería de datos: la extracción de contenido de páginas **renderizadas dinámicamente vía JavaScript (SPA)**, donde herramientas tradicionales como `requests` + `BeautifulSoup` fallan porque el HTML inicial no contiene los datos objetivo — estos llegan después, vía una llamada asíncrona a una API simulada por el propio frontend.

Este módulo implementa un scraper con **Playwright** (Chromium headless) capaz de:
1. Renderizar JavaScript real en un browser headless.
2. Esperar explícitamente a que el contenido dinámico termine de cargar (sin `time.sleep()` fijo).
3. Extraer datos estructurados del DOM ya poblado.

### Sobre el target de scraping
En vez de apuntar a un sitio público real (frágil ante cambios de HTML de terceros), el proyecto levanta un **mock server HTTP local** (`http.server`) que sirve una página de catálogo corporativo cuyo contenido se inyecta vía JS tras un delay de 1.5s — simulando fielmente el comportamiento de una SPA real (React/Vue) que hace `fetch()` a una API tras el render inicial.

Esto hace el proyecto **100% reproducible y determinista**, ideal para portfolio y para CI, sin depender de la disponibilidad o estructura de un sitio externo.

---

## 🛠️ Tecnologías y Librerías Utilizadas
* **Python 3.x** (Tipado estricto, dataclasses, context managers)
* **Playwright** (Automatización de browser headless con espera nativa por selectores)
* **http.server** (Mock server local en hilo daemon, sin dependencias externas)
* **Pytest** (Tests de integración end-to-end reales, no mockeados)

---

## 📂 Arquitectura de Archivos
```text
D66-Playwright-Dynamic-Scraper/
├── D66.py                  # Orquestador: mock server + scraper + export JSON
├── mock_site/
│   └── index.html           # Página SPA simulada (inyección de datos vía JS)
├── tests/
│   └── test_scraper.py      # Tests de integración (server + browser real)
├── scraped_products.json    # Artefacto de salida (generado al ejecutar)
├── requirements.txt
└── README.md
```

---

## ⚙️ Componentes Clave

### `MockCatalogServer`
Levanta un `ThreadingHTTPServer` en un puerto libre del sistema operativo (`socket.bind(("", 0))`), corriendo en un hilo `daemon` para no bloquear el proceso principal. Se apaga automáticamente en el `finally` del pipeline.

### `DynamicCatalogScraper`
- Navega con `page.goto(url, wait_until="domcontentloaded")` — **no** espera a `networkidle`, ya que el contenido dinámico llega después del propio `DOMContentLoaded`.
- Usa `page.wait_for_selector(".product-card", timeout=8000)` para esperar la aparición real del contenido inyectado por JS — este es el patrón correcto en scraping dinámico (vs. `sleep()` fijo, que es lento e impredecible).
- Verifica adicionalmente un atributo de estado (`body[data-catalog-ready="true"]`) inyectado por el propio JS del mock, como señal explícita de "carga completa" — patrón común en SPAs reales instrumentadas para testing (data-testid, flags de estado).

### Mock site (`mock_site/index.html`)
El HTML inicial se sirve vacío (`<div id="product-list"></div>`). Un script `setTimeout` de 1.5s simula la latencia de una llamada a API real y luego inyecta las tarjetas de producto vía `innerHTML`, replicando el patrón de cualquier frontend moderno con fetch asíncrono.

---

## ▶️ Cómo Ejecutarlo en VS Code

### 1. Crear y activar entorno virtual
```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2. Instalar dependencias
```powershell
pip install -r requirements.txt
playwright install chromium
```
> ⚠️ Este paso es obligatorio y específico de Playwright: descarga el binario del browser Chromium que Playwright controla. Sin él, el script falla con `Executable doesn't exist`.

### 3. Ejecutar el scraper
```powershell
python D66.py
```

### 4. Ejecutar los tests
```powershell
pytest tests/ -v
```

---

## 📤 Ejemplo de Salida

Consola:
```
2026-03-16 09:00:00 - INFO - === [D66] INICIANDO DYNAMIC SCRAPER CON PLAYWRIGHT ===
2026-03-16 09:00:00 - INFO - Mock catalog server activo en: http://127.0.0.1:54231
2026-03-16 09:00:00 - INFO - Navegando a: http://127.0.0.1:54231/index.html
2026-03-16 09:00:00 - INFO - Esperando renderizado asíncrono del catálogo...
2026-03-16 09:00:02 - INFO - Catálogo renderizado. 6 tarjetas de producto detectadas.
2026-03-16 09:00:02 - INFO - [SUCCESS] Artefacto exportado en: scraped_products.json

[ÉXITO] Scraping completado en 1.87s
Productos extraídos: 6
  - [ENT-1001] Servidor Rack ProLine X200 | €4899.00 | En stock
  - [ENT-1002] Switch Gestionable 48-Puertos | €1250.50 | En stock
  - [ENT-1003] Licencia SaaS Analytics Suite (Anual) | €3600.00 | Agotado
  - [ENT-1004] Firewall Perimetral NextGen FW-9000 | €7899.99 | En stock
  - [ENT-1005] Cabina de Almacenamiento NAS 32TB | €5420.75 | En stock
  - [ENT-1006] Estación de Trabajo GPU-Optimized | €3299.00 | Agotado
```

Artefacto `scraped_products.json`:
```json
{
    "execution_time_seconds": 1.8734,
    "total_products_scraped": 6,
    "in_stock_count": 4,
    "out_of_stock_count": 2,
    "products": [
        {
            "sku": "ENT-1001",
            "name": "Servidor Rack ProLine X200",
            "price": 4899.0,
            "in_stock": true
        }
    ]
}
```

---

## 🧠 Notas Técnicas

- **Puerto dinámico vs. puerto fijo**: se usa `socket.bind(("127.0.0.1", 0))` para que el SO asigne un puerto libre automáticamente, evitando colisiones si el puerto 8000 (típico) ya está en uso en la máquina del desarrollador.
- **`wait_for_selector` vs `sleep`**: usar un delay fijo (`time.sleep(3)`) es el anti-patrón más común en scraping dinámico — es lento en el caso feliz e insuficiente si la red está lenta. `wait_for_selector` con timeout es determinista y falla explícitamente (`PlaywrightTimeoutError`) si algo no carga, permitiendo manejo de errores real.
- **Migrar a un target real**: para apuntar a un sitio público, basta reemplazar `target_url` en `main()` por la URL real y eliminar el uso de `MockCatalogServer`. El resto del pipeline (`DynamicCatalogScraper`) es agnóstico del origen.
- **Producción**: en un entorno productivo, este scraper correría en un contenedor con Chromium preinstalado (imagen oficial `mcr.microsoft.com/playwright/python`), con reintentos exponenciales ante fallos de red y rotación de user-agents si el target tiene protección anti-bot — fuera de alcance de este mini-proyecto.
- **Próximo paso natural (D67)**: rotación de proxies con `requests` para escenarios de scraping a gran escala donde el rate-limiting por IP es un problema.