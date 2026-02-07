### 🤖 Proyecto Día 42: Bulk Rename & Dynamic Timestamping 🕒🏷️

En este hito, evolucionamos el organizador del Día 41 para añadir una capa de **Control de Versiones Automático**. El sistema ahora renombra cada archivo antes de moverlo, garantizando que nunca se pierda información por duplicidad de nombres y facilitando la búsqueda cronológica de documentos.

#### **Hitos Técnicos Alcanzados:**
1.  **Manipulación de Strings y Rutas:** Uso avanzado de `pathlib` para separar el nombre del archivo (stem) de su extensión (suffix) de forma segura.
2.  **Inyección de Metadatos Cronológicos:** Integración del módulo `datetime` para generar sellos de tiempo precisos (YYYY-MM-DD) integrados en el nombre del archivo.
3.  **Lógica Anti-Duplicados:** Implementación de un prefijo temporal que actúa como identificador único, permitiendo procesar múltiples versiones de un mismo archivo en el mismo día.
4.  **Flujo de Trabajo Atomizado:** Refactorización del proceso de movimiento: Clasificar -> Renombrar -> Desplazar.

#### **Tecnologías Utilizadas:**
* **Pathlib:** Para un manejo de rutas orientado a objetos mucho más robusto que `os.path`.
* **Datetime:** Para el formateo de sellos de tiempo dinámicos.
* **Shutil:** Para la ejecución física del traslado de archivos.