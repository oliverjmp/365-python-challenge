🗂️ Día 14 — Sistema de Monitoreo de Archivos (File Watcher) + Alertas Básicas
📌 Descripción general

En este día desarrollé un sistema de monitoreo de archivos (File Watcher) capaz de detectar cambios en una carpeta en tiempo real.
El objetivo es identificar eventos como creación, modificación o eliminación de archivos, y generar alertas básicas junto con un registro detallado en logs.

Este tipo de herramienta es fundamental en procesos automatizados, pipelines de datos y sistemas de vigilancia de carpetas.

🎯 Objetivos del día

Monitorear una carpeta en tiempo real.

Detectar:

nuevos archivos

archivos modificados

archivos eliminados

Registrar todos los eventos en un archivo de log.

Mostrar alertas básicas por consola.

Preparar la base para futuras integraciones (alertas por email, pipelines, validadores, etc.).

🛠️ Tecnologías utilizadas

Python

Módulo os

Módulo time

Logging

Estructuras de monitoreo basadas en timestamps

🧩 Funcionalidades principales

✔ Detección de nuevos archivos
Identifica cuando un archivo aparece en la carpeta monitoreada.

✔ Detección de archivos modificados
Compara timestamps para detectar cambios en el contenido.

✔ Detección de archivos eliminados
Registra cuando un archivo desaparece de la carpeta.

✔ Logging estructurado
Genera un archivo:

Código

logs/file_watcher.log

con todos los eventos detectados.

✔ Alertas básicas por consola
Cada evento se imprime en tiempo real con iconos visuales:

🟢 Nuevo archivo

🟡 Archivo modificado

🔴 Archivo eliminado

📂 Estructura del módulo
Código
14-ENERO/

│── file_watcher.py

│── watch_folder/

│── logs/
│     └── file_watcher.log

│── README.md

🚀 Ejecución

Desde la carpeta:

Código

cd 2026/14-ENERO

python file_watcher.py

Salida esperada al realizar cambios en watch_folder:

Código
🔍 Monitoreando carpeta: watch_folder

🟢 Nuevo archivo detectado: test.txt

🟡 Archivo modificado: test.txt

🔴 Archivo eliminado: test.txt

🟢 Nuevo archivo detectado: texto.txt

📄 Ejemplo de archivo de prueba (test.txt)
Código

Este es un archivo de prueba para el sistema de monitoreo del Día 14.

Si este archivo aparece, modifica o se elimina, el watcher debe detectarlo.
Prueba 1: creación del archivo.

Prueba 2: modificación del contenido.

Prueba 3: eliminación del archivo.