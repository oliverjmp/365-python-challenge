# D186 - JSON SemiStructured Parsing

Plataforma analítica corporativa para la extracción, aplanamiento y consulta estructurada de datos semi-estructurados (JSON anidado) utilizando DuckDB sobre almacenamiento columnar Parquet.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Operadores JSON Nativos (`->>`):** Recuperación eficiente de atributos anidados en profundidad sin penalización de rendimiento.
2. **Analítica In-Process de Cero Copia:** Procesamiento de grandes volúmenes de eventos con uso mínimo de memoria RAM.
3. **Presentación Híbrida:** Documentación técnica estática (MkDocs) combinada con aplicaciones analíticas interactivas en tiempo real (Streamlit).

## 💼 Casos Prácticos en el Mundo Real
- **Análisis de Logs de Aplicaciones y Telemetría:** Extracción y auditoría en tiempo real de cargas útiles JSON complejas provenientes de microservicios o pasarelas de pago, filtrando errores críticos y latencias de red sin requerir ETLs pesadas previas.
- **Consultoría de Eventos de Usuario (Clickstream):** Procesamiento dinámico de interacciones de clientes almacenadas en esquemas flexibles, permitiendo a los equipos de producto consultar métricas de uso multiplataforma de forma instantánea.

## 📂 Estructura del Proyecto
```text
D186-JSON-Semi-Structured-Parsing/
├── data_lake/             # Almacenamiento columnar temporal de ficheros Parquet
├── docs/
│   └── index.md           # Documentación técnica corporativa (MkDocs)
├── src/
│   ├── __init__.py
│   ├── json_parsing_engine.py  # Motor analítico de procesamiento JSON
│   ├── dashboard.py       # Aplicación ejecutiva interactiva (Streamlit + Plotly)
│   └── main_demo.py       # Script ejecutable principal de terminal
├── tests/
│   ├── __init__.py
│   └── test_json_engine.py   # Pruebas unitarias de cobertura con pytest
├── mkdocs.yml             # Configuración del portal MkDocs
├── requirements.txt       # Dependencias del entorno
└── README.md              # Documentación técnica avanzada del hito