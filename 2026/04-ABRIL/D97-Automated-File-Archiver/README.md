# D97 - Automated File Archiver

## Descripción
D97 es un pipeline automatizado diseñado para escanear directorios de trabajo, clasificar dinámicamente cualquier tipo de archivo según su extensión y empaquetar respaldos comprimidos de manera limpia utilizando únicamente la librería estándar de Python (`pathlib` y `shutil`).

## Estructura del Proyecto
* `data/entrada/`: Ficheros pendientes de clasificar.
* `data/clasificados/`: Ficheros organizados automáticamente por carpetas de extensión (`pdf/`, `xlsx/`, `png/`, etc.).
* `data/respaldos/`: Archivos `.zip` históricos generados tras cada ejecución.
* `src/archiver.py`: Lógica central del pipeline.
* `tests/test_archiver.py`: Pruebas unitarias de validación.

## Instrucciones de Uso
1. Coloca tus archivos en `data/entrada/`.
2. Ejecuta el pipeline desde la terminal:
   ```powershell
   $env:PYTHONPATH="."; python run_archiver.py