# D166 - Excel Export Engine con Openpyxl y Pandas

Motor automatizado de exportación de tablas analíticas y DataFrames a ficheros de Microsoft Excel (`.xlsx`), aplicando estilos corporativos profesionales (encabezados personalizados, fuentes, anchos de columna dinámicos y formatos numéricos).

## Características Principales
- **Formato Profesional:** Inyección de estilos con `openpyxl` (colores institucionales, bordes y alineaciones).
- **Ajuste Dinámico:** Cálculo automático del ancho de las columnas basado en el contenido para evitar recortes visuales.
- **Pruebas Automatizadas:** Validación lógica de la creación de ficheros y hojas de cálculo exportadas.

## 📂 Estructura del Proyecto
```text
D166-Excel-Export-Engine-Openpyxl/
├── src/
│   ├── __init__.py
│   └── exporter.py
├── tests/
│   ├── __init__.py
│   └── test_exporter.py
├── app_excel.py
├── requirements.txt
└── README.md