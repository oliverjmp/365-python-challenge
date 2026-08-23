# D158 - ReportLab Dynamic PDF Canvas & Flowables

Este hito implementa un **generador avanzado de informes ejecutivos en PDF estructurados** utilizando `ReportLab` mediante la combinación de elementos fluidos (`Flowables`) para el contenido de texto y tablas, junto con un lienzo maestro personalizado (`Canvas`) para la numeración dinámica de páginas corporativas (Página X de Y) y pies de página institucionales.

## Características Principales
- **Plantilla Maestra con Canvas Dinámico (`NumberedCanvas`):** Calcula automáticamente el número total de páginas para renderizar un pie de página profesional ("Página X de Y") sin desalinear el contenido.
- **Flujos de Contenido Estructurados (`Flowables`):** Inserción limpia de títulos, subtítulos, párrafos espaciados y tablas con estilos estilizados.
- **Control de Calidad y Pruebas Unitarias:** Validación rigurosa de entradas vacías, extensiones de archivo correctas y verificación de creación física del documento.

## 📂 Estructura del Proyecto
```text
D158-ReportLab-Dynamic-PDF-Canvas/
│
├── src/
│   ├── __init__.py
│   └── pdf_generator.py
├── tests/
│   └── test_pdf_generator.py
├── run_pdf.py
├── requirements.txt
└── README.md