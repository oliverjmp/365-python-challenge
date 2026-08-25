# Arquitectura de Contenerización D203

## 🐳 Flujo de Construcción Multi-etapa
El contenedor se construye bajo dos fases distinctas:
1. **Etapa `builder`:** Utiliza una imagen con herramientas de compilación (`build-essential`) para instalar las dependencias de Python de forma limpia.
2. **Etapa `runner`:** Parte de una imagen base limpia, copiando únicamente los paquetes compilados y el código fuente, reduciendo el tamaño final en disco y la superficie de vulnerabilidades.