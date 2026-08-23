# D163 - File Uploader & Data Sanitizer

Interfaz robusta de carga de ficheros externos con validación de esquemas en caliente mediante `Pydantic` y visualización en tiempo real con `Streamlit`.

## Características Principales
- **Carga Segura de Ficheros:** Componente interactivo para la ingesta de archivos CSV o JSON directamente desde el navegador.
- **Validación Estricta con Pydantic:** Verificación fila por fila de los esquemas, tipos de datos y restricciones de negocio en caliente.
- **Reporte de Errores Detallado:** Interfaz amigable que detalla exactamente qué filas o campos fallaron la validación.

## 📂 Estructura del Proyecto
```text
D163-File-Uploader-Data-Sanitizer/
├── src/
│   ├── __init__.py
│   ├── validator.py
│   └── sanitizer.py
├── tests/
│   ├── __init__.py
│   └── test_sanitizer.py
├── app_uploader.py
├── requirements.txt
└── README.md