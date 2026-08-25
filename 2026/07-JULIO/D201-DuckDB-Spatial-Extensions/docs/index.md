# D201 - DuckDB Spatial & Geospatial Extensions

Sistema avanzado de análisis y procesamiento geoespacial de ultra alto rendimiento utilizando la extensión **Spatial de DuckDB**, integrado con flujos de Python, pruebas unitarias estrictas y visualización interactiva.

---

## 🏛️ Descripción General del Hito

El hito **D201** aborda la integración de capacidades analíticas geoespaciales directamente dentro del motor analítico *in-process* de DuckDB. Tradicionalmente, el procesamiento de coordenadas, geometrías y operaciones espaciales requería la instalación de motores pesados (como PostGIS o librerías complejas). Este módulo demuestra cómo resolver consultas espaciales complejas de forma rápida, eficiente y embebida utilizando Python.

---

## 🚀 Arquitectura Técnica y Capacidades

El sistema está diseñado bajo una arquitectura modular y desacoplada:

1. **Gestor del Motor Espacial (`src/spatial_runner.py`):**
   - Conexión optimizada en memoria con DuckDB.
   - Carga e instalación dinámica de la extensión `spatial` mediante comandos nativos del motor.
   - Procesamiento de coordenadas geográficas (Latitud/Longitud) y transformación a formatos estándar de la industria como **WKT (Well-Known Text)** mediante funciones analíticas como `ST_Point` y `ST_AsText`.

2. **Interfaz Interactiva de Visualización (`app.py`):**
   - Dashboard analítico desplegado en **Streamlit** que permite a los tomadores de decisiones inspeccionar tablas de puntos de interés (POI).
   - Renderizado cartográfico integrado mediante mapas nativos de alta fluidez.

3. **Calidad de Software y Testing (`tests/test_spatial.py`):**
   - Cobertura estricta al 100% mediante `pytest` y `pytest-cov`, validando tanto la integridad de la extensión como el correcto formateo de las geometrías devueltas.

---

## 💼 Casos de Uso Empresariales

- **Logística y Cadena de Suministro:** Optimización de rutas de transporte y validación rápida de puntos de entrega geolocalizados sin latencia de red.
- **Geomarketing y Retail:** Agrupamiento masivo de sucursales y análisis de proximidad de clientes utilizando funciones espaciales integradas en consultas SQL analíticas.
- **Telemetría e IoT:** Ingesta y validación en tiempo real de flujos de coordenadas emitidos por dispositivos móviles o sensores vehiculares sobre grandes volúmenes de datos.

---

## ⚙️ Guía de Ejecución Rápida

Para poner en marcha el entorno y validar el funcionamiento del sistema, ejecuta los siguientes comandos en tu terminal de PowerShell:

### 1. Instalación de dependencias
```powershell
pip install -r requirements.txt