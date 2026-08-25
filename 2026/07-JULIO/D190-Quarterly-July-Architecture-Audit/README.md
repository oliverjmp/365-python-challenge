# D190 - Quarterly Architecture Audit

Sistema automatizado de auditoría integral de rendimiento, validación de esquemas JSON mediante Pydantic v2 y visualización mediante tablero ejecutivo en Streamlit para el inicio de la Fase 4 del portafolio analítico.

## 🏛️ Arquitectura de Procesamiento Implementada
1. **Persistencia Estructurada en Data Lake:** Lectura de contratos de arquitectura almacenados en formato JSON (`data_lake/architecture_state.json`).
2. **Validación de Contratos con Pydantic v2:** Control estricto de tipos, patrones permitidos de estado (`CONFORME`, `ADVERTENCIA`, `CRITICO`) y rangos numéricos de rendimiento.
3. **Consolidación de Métricas y Visualización Ejecutiva:** Generación automatizada de índices de cumplimiento expuestos mediante un tablero dinámico web.

## 💡 Casos de Uso del Mundo Real
- **Gobierno de Datos y Auditoría de Microservicios:** Monitorear el estado de salud de múltiples dependencias técnicas en tiempo real mediante contratos tipados.
- **Reportes Ejecutivos para Comités Directivos:** Transformar logs y estados JSON complejos en dashboards visuales de alto impacto para la toma de decisiones.

## 📂 Estructura del Proyecto
```text
D190-Quarterly-July-Architecture-Audit/
├── data_lake/             # Contrato de estado en formato JSON
├── docs/
│   └── index.md           # Documentación técnica en MkDocs
├── src/
│   ├── __init__.py
│   └── audit_engine.py    # Motor de validación y métricas de arquitectura
├── tests/
│   ├── __init__.py
│   └── test_audit_engine.py # Pruebas unitarias con pytest
├── dashboard.py           # Aplicación ejecutiva interactiva con Streamlit
├── run_audit.py           # Script ejecutable principal en consola
├── mkdocs.yml             # Configuración de MkDocs
├── requirements.txt       # Dependencias del proyecto
└── README.md              # Documentación técnica del hito