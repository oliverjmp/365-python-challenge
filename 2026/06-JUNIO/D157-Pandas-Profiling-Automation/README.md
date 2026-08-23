# D157 - Pandas Profiling Automation

Este hito implementa un **script automatizado de auditoría exploratoria de datos (EDA)** utilizando `YData Profiling` (`pandas-profiling`), permitiendo generar diagnósticos completos de calidad de datos, estadísticas descriptivas y correlaciones con exportación a un reporte HTML interactivo.

## Características Principales
- **Automatización Completa de EDA:** Resúmenes profundos de datasets con una única ejecución orientada a objetos (`DataAuditorEngine`).
- **Control de Calidad de Datos:** Detección automática de valores nulos, duplicados, tipos de datos anómalos y alertas estadísticas.
- **Exportación Interactiva HTML:** Generación de informes listos para compartir con stakeholders y perfiles de negocio sin necesidad de escribir código visual manual.

## 📂 Estructura del Proyecto
```text
D157-Pandas-Profiling-Automation/
│
├── src/
│   ├── __init__.py
│   └── data_auditor.py
├── tests/
│   └── test_data_auditor.py
├── run_audit.py
├── requirements.txt
└── README.md