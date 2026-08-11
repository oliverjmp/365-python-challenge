# D96 - File System Watcher Daemon

## Descripción
D96 es un demonio de monitoreo de archivos diseñado para automatizar el procesamiento de datos. El sistema vigila un directorio específico en tiempo real y, al detectar la creación o modificación de archivos de Excel (`.xlsx`, `.xls`), procesa y muestra automáticamente un resumen de su contenido en consola.

## Características
* **Monitoreo en tiempo real:** Utiliza la librería `watchdog` para reaccionar instantáneamente a cambios en el sistema de archivos.
* **Procesamiento automático de Excel:** Emplea `pandas` para extraer y analizar tablas de datos sin intervención manual.
* **Manejo de bloqueos:** Implementa una estrategia de copia temporal mediante `shutil` y `os` para gestionar el bloqueo exclusivo de archivos impuesto por Microsoft Excel en Windows.
* **Cobertura 100%:** Proyecto validado con pruebas unitarias (`pytest`) para garantizar estabilidad.

## Requisitos Previos
* Python 3.11 o superior.
* Librerías necesarias (listadas en `requirements.txt`):
  * `watchdog`
  * `pandas`
  * `openpyxl`

## Instalación
1. Clona este repositorio en tu equipo.
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt