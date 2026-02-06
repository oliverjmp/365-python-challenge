🗂️ Día 15 — Sistema de Backup Automático (Backup Manager)

📌 Descripción general

En este día desarrollé un sistema de backup automático capaz de crear copias versionadas de un archivo o carpeta, mantener un 

número máximo de versiones y eliminar las más antiguas.

El objetivo es garantizar la disponibilidad de información histórica y evitar la acumulación innecesaria de archivos.

Este módulo es ideal para pipelines de datos, reportes automatizados y cualquier flujo donde sea necesario conservar versiones previas.

🎯 Objetivos del día

Crear copias de seguridad con timestamp.

Mantener un número máximo de backups.

Eliminar versiones antiguas automáticamente.

Registrar todas las operaciones en logs.

Permitir configuración mediante archivo JSON.

🛠️ Tecnologías utilizadas

Python

Módulo shutil

Módulo os

JSON para configuración

Logging

🧩 Funcionalidades principales

✔ Creación de backups con timestamp

Cada ejecución genera una copia con formato:

Código

backup_YYYYMMDD_HHMMSS

✔ Soporte para archivos o carpetas

El sistema detecta si source_path es archivo o directorio.

✔ Eliminación automática de versiones antiguas

Si el número de backups supera el límite configurado, se eliminan los más antiguos.

✔ Logging estructurado

Se genera un archivo:


Código

logs/backup.log

con información detallada de:

backups creados

backups eliminados

errores

✔ Configuración flexible

El archivo config.json permite definir:

ruta a respaldar

número máximo de versiones

📂 Estructura del módulo
Código
15-ENERO/

│── backup_manager.py

│── config.json

│── backups/

│── logs/

│     └── backup.log
│── README.md

⚙️ Archivo de configuración (config.json)

Ejemplo:

json
{
    "source_path": "data",

    "max_backups": 5
}
Puedes cambiar:

"data" por cualquier archivo o carpeta

"max_backups" por el número de versiones que quieras conservar

🚀 Ejecución

Desde la carpeta:

Código

cd 2026/15-ENERO

python backup_manager.py

Salida esperada:

Código

🟢 Backup creado: backup_20260206_213916

🟡 Backup eliminado: backup_20260205_180000

📄 Ejemplo de archivo para respaldar

Puedes crear un archivo dentro de data/ como:

Código

Este es un archivo de prueba para el sistema de backup automático del Día 15.

Sirve para verificar la creación de copias, el versionado y la limpieza de backups antiguos.