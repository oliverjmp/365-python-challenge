# Día 67: Proxy Rotation Scraper (`Requests + Proxy Pool`)

## 📋 Descripción General
Motor de extracción web resiliente desarrollado en Python utilizando la librería `requests` en conjunto con un **Pool de Proxies rotativos**. Su objetivo principal es prevenir bloqueos, limitaciones de tasa (*rate limiting*) y baneos de IP (*IP bans*) durante la ejecución de pipelines de datos a gran escala[cite: 1].

## 🛠️ Enfoque Técnico y Arquitectura
- **Rotación Round-Robin Dinámica**: Distribución equitativa de las peticiones HTTP entre los nodos intermediarios disponibles.
- **Tolerancia a Fallos y Auto-Purga**: Detección automática de códigos de error por bloqueo (HTTP 403, 429, 503) o fallos de red para eliminar de manera inmediata el proxy defectuoso del pool activo.
- **Reintentos Exponenciales**: Integración del adaptador HTTP de `urllib3` con backoff exponencial para mitigar intermitencias de red.
- **Tipado Estricto y Validación**: Uso de esquemas robustos mediante `Pydantic v2` para la configuración de parámetros de red y listas de proxies cargadas desde variables de entorno.

## 🚀 Instalación y Configuración

1. **Clonar la estructura o situarse en el directorio del módulo**:
   ```bash
   cd 03-MARZO/D67-Proxy-Rotation-Scraper