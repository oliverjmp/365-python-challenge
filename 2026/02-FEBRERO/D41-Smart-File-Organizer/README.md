### 🤖 Proyecto Día 41: Smart File Organizer & OS Automation 📂⚡

Iniciamos la Fase 3 enfocándonos en la automatización de flujos de trabajo locales. Este script actúa como un "Robot de Limpieza" para el sistema operativo, clasificando archivos huérfanos en carpetas estructuradas según su extensión. Es el primer paso para construir sistemas de procesamiento de datos por lotes (Batch Processing).

#### **Hitos Técnicos Alcanzados:**
1.  **Manipulación de File System:** Uso profundo de la librería `os` para escanear directorios y `shutil` para operaciones de movimiento de archivos de alto nivel.
2.  **Mapeo Dinámico de Extensiones:** Implementación de un diccionario de categorías (Documentos, Imágenes, Ejecutables) para la clasificación automática.
3.  **Gestión de Colisiones:** Lógica básica para evitar errores si una carpeta de destino ya existe o si el archivo está en uso.
4.  **Automatización de Rutas:** Uso de rutas relativas y absolutas para garantizar que el script funcione en cualquier entorno (Windows/Mac/Linux).

#### **Tecnologías Utilizadas:**
* **os Module:** Interfaz con el Sistema Operativo para manejo de directorios.
* **shutil Module:** Utilidades de copia y movimiento de archivos.
* **Pathlib:** Gestión moderna de rutas de archivos.