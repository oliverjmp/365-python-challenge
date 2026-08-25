# Arquitectura del Hito D201

## 🗺️ Pipeline Geoespacial
El sistema opera mediante los siguientes flujos técnicos:
1. **Carga Dinámica:** Instalación en memoria de la librería `spatial` provista por la API oficial de DuckDB.
2. **Ingesta de Coordenadas:** Conversión de pares tradicionales de latitud y longitud a objetos geométricos tipados mediante funciones como `ST_Point` y `ST_AsText`.