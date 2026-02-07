### 🤖 Proyecto Día 45: Automated Snapshot & Zip Backup 📦🛡️

Este proyecto implementa la red de seguridad definitiva para cualquier sistema de automatización: el **Backup Preventivo**. Antes de realizar operaciones de escritura, movimiento o borrado, el sistema genera un "Snapshot" comprimido del estado actual del directorio, permitiendo una recuperación instantánea ante fallos lógicos o errores de script.

#### **Hitos Técnicos Alcanzados:**
1.  **Algoritmos de Compresión:** Implementación de `ZIP_DEFLATED` para reducir el consumo de almacenamiento mientras se empaquetan los activos.
2.  **Recursividad Inteligente:** Uso de `rglob("*")` para capturar archivos en subcarpetas, manteniendo la integridad de la estructura original dentro del archivo comprimido.
3.  **Snapshot Timestamping:** Generación de nombres de archivo únicos basados en segundos (`YYYYMMDD_HHMMSS`) para evitar colisiones de backups.
4.  **Aislamiento de Flujo:** Lógica de exclusión para evitar "backups infinitos" (impedir que el script intente meter la carpeta de Backups dentro del propio ZIP).

#### **Tecnologías Utilizadas:**
* **Zipfile Module:** Librería estándar de Python para manipulación de archivos comprimidos.
* **Pathlib:** Gestión de rutas relativas (`arcname`) para asegurar que el ZIP sea portable entre diferentes PCs.
* **Datetime:** Precisión temporal para el versionamiento de snapshots.