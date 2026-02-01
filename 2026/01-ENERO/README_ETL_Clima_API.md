🌦️ Día 01 — ETL Profesional: API del Clima → Transformación → SQLite
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge
🚀 Descripción del proyecto
Este proyecto implementa un pipeline ETL profesional que:

Extrae datos meteorológicos desde una API pública

Transforma los datos en un formato limpio y analítico

Carga la información en una base de datos SQLite

Genera logs y maneja errores de forma robusta

Este tipo de pipeline es común en:

Data Engineering

Business Intelligence

Automatización de reportes

Integración de datos en empresas

🧠 Tecnologías utilizadas
Python 3

requests

sqlite3

logging

API pública de Open‑Meteo

📦 Estructura del proyecto
Código
dia_01_ETL_Clima_API/
│── main.py
│── README.md
└── recursos/
▶️ Cómo ejecutar
1. Instala dependencias:
Código
pip install requests
2. Ejecuta el script:
Código
python main.py
3. Se generará automáticamente la base de datos:
Código
clima.db
📊 Resultado
El pipeline crea la tabla:

Código
weather_data
Con las columnas:

fecha

temperatura

velocidad_viento

humedad

ciudad

Además, el programa muestra en consola el pronóstico de los próximos 5 días, incluyendo temperaturas máximas y mínimas.