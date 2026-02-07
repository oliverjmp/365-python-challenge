📊 Día 03 — Automatización de Excel a partir de CSV
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge

🚀 Descripción del proyecto
Este proyecto toma un archivo CSV con información de criptomonedas (por ejemplo, generado en el Día 02) y crea un informe Excel profesional, aplicando:

Formato de encabezados

Colores corporativos

Negritas y alineación

Formato de moneda

Formato de porcentaje

Autoajuste de columnas

El objetivo es simular un flujo real de automatización de reportes, como los que se utilizan en:

Finanzas

Business Intelligence

Data Engineering

Reporting corporativo

🧠 Tecnologías utilizadas
Python 3

pandas — lectura y exportación de datos

openpyxl — formateo avanzado de Excel

📦 Estructura del proyecto
Código
dia_03_Excel_Automatizado/
│── main.py
│── README.md
└── recursos/
▶️ Cómo ejecutar


1. Instala las dependencias:
bash
pip install pandas openpyxl
2. Asegúrate de tener el archivo:
Código
precios_crypto.csv
en la misma carpeta que main.py.

3. Ejecuta el script:
bash
python main.py
4. Se generará automáticamente:
Código
informe_cripto.xlsx

📊 Resultado

El archivo Excel generado incluye:

Encabezados con fondo azul y texto blanco

Datos formateados como moneda y porcentaje

Columnas ajustadas automáticamente

Un informe limpio, profesional y listo para enviar

Ejemplo de salida en consola:

Archivo 'informe_cripto.xlsx' generado y formateado correctamente.