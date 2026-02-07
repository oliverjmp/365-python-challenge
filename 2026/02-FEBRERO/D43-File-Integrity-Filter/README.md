### 🤖 Proyecto Día 43: File Integrity & Quality Filter 🗑️🔍

En este hito, transformamos el automatizador en un sistema de **Mantenimiento Preventivo**. El script ahora inspecciona los metadatos del archivo (tamaño en disco) antes de renombrarlo o moverlo. Si un archivo no cumple con el estándar de integridad (archivos vacíos de 0 bytes), es segregado automáticamente a una carpeta de desecho.

#### **Hitos Técnicos Alcanzados:**
1.  **Inspección de Metadatos:** Uso de `os.path.getsize` para evaluar el peso del archivo antes de la ingesta.
2.  **Lógica de Segregación (Quarantine):** Implementación de una ruta de "Papelera" para aislar archivos sospechosos o corruptos.
3.  **Cómputo de Carga Procesada:** Cálculo en tiempo real de la cantidad de datos (en KB/MB) que el script ha movido exitosamente.
4.  **Optimización de I/O:** Evitamos procesar archivos innecesarios, ahorrando ciclos de escritura en disco.

#### **Tecnologías Utilizadas:**
* **os.path:** Para la lectura de propiedades físicas de los archivos.
* **Pathlib:** Para la gestión de rutas y creación de la zona de cuarentena.
* **Shutil:** Para la ejecución del movimiento de segregación.