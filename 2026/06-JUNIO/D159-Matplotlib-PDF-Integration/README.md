# D159 - Matplotlib + ReportLab PDF Integration

Este hito implementa un **pipeline de exportación automatizada** que combina la potencia visual de `Matplotlib` para la generación de gráficos estadísticos en memoria con el motor de estructuración de documentos de `ReportLab`, permitiendo incrustar gráficos rasterizados de alta calidad directamente en informes PDF gerenciales.

## Características Principales
- **Generación en Memoria (`io.BytesIO`):** Renderiza y convierte gráficos estadísticos a búferes de bytes sin necesidad de saturar el disco con imágenes temporales físicas.
- **Diseño Corporativo Optimizado:** Gráficos limpios con etiquetas dinámicas, paletas de colores institucionales y tablas de resumen estructuradas mediante Flowables.
- **Pruebas Unitarias Rigurosas:** Validación integral de parámetros de entrada, extensiones de archivo y compilación exitosa de documentos en entornos headless.

## 📂 Estructura del Proyecto
```text
D159-Matplotlib-PDF-Integration/
│
├── src/
│   ├── __init__.py
│   └── chart_pdf_pipeline.py
├── tests/
│   └── test_chart_pdf_pipeline.py
├── run_pipeline.py
├── requirements.txt
└── README.md