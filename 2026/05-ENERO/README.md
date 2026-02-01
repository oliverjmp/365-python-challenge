📄 Día 05 — Exportación Automática del Informe a PDF
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge

🚀 Descripción del proyecto
En este quinto día del reto, se completa el ciclo profesional de generación de reportes:

CSV → Excel formateado → Excel con gráficos → PDF listo para enviar

El script toma el archivo Excel generado en el Día 04:

Código
../04-ENERO/informe_cripto.xlsx
y lo convierte automáticamente en un PDF profesional, utilizando Microsoft Excel como motor de renderizado.
Este tipo de automatización es habitual en entornos como:

Reporting financiero

Business Intelligence

Automatización de informes ejecutivos

Sistemas de generación de reportes diarios

El objetivo es obtener un documento final limpio, coherente y listo para entregar, sin intervención manual.

🧠 Tecnologías utilizadas
Python 3

win32com.client (automatización de Excel en Windows)

Rutas automáticas basadas en la ubicación del script

📦 Estructura del proyecto
Código
dia_05_Exportar_PDF/
│── main.py
│── README.md
└── recursos/
▶️ Cómo ejecutar
1. Instalar la dependencia necesaria:
bash
pip install pywin32
2. Verificar que el archivo del Día 04 existe:
Código
../04-ENERO/informe_cripto.xlsx
3. Ejecutar el script:
bash
python main.py
4. Se generará automáticamente:
Código
informe_cripto.pdf
en la carpeta del Día 05.

📊 Resultado
El PDF generado incluye:

La tabla formateada del Día 03

Los gráficos premium creados en el Día 04

La portada ejecutiva

Todo en un documento profesional, ordenado y listo para enviar

Ejemplo de salida en consola:

Código
Convirtiendo a PDF...
Origen: ../04-ENERO/informe_cripto.xlsx
Destino: informe_cripto.pdf
PDF generado correctamente.
✨ Nota final
Este sistema de exportación es totalmente funcional, pero puede ampliarse tanto como sea necesario:
nuevos estilos, más hojas, portadas avanzadas, automatización por lotes, envío por email, integración con APIs… lo que haga falta.