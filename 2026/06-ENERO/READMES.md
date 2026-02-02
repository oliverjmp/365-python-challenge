📄 README — Día 06 (Pipeline Maestro de Automatización Completa)
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge

🚀 Descripción del proyecto
En este sexto día del reto, se construye un pipeline maestro capaz de ejecutar automáticamente todo el flujo de generación del informe:

Día 03 → Limpieza de datos

Día 04 → Dashboard Premium en Excel

Día 05 → Exportación del PDF profesional

Logs automáticos

Indicadores de progreso en consola

Con un solo comando:

Código
python main.py
obtienes el PDF final listo para enviar, junto con un registro de ejecución.

Este tipo de automatización es habitual en:

Reporting financiero

Procesos ETL

Automatización de informes ejecutivos

Pipelines de Business Intelligence

Sistemas batch diarios

🧠 Tecnologías utilizadas
Python 3

Subprocess (ejecución de scripts)

Manejo de rutas dinámicas

Sistema de logs automático

📦 Estructura del proyecto
Código
dia_06_Pipeline/
│── main.py
│── README.md
└── logs/
    └── pipeline_2026-02-02.log
▶️ Cómo ejecutar
Asegúrate de que los días 03, 04 y 05 están completos.

Ejecuta:

bash
python main.py
El pipeline generará:

El Excel premium

El PDF final

Un archivo de log

Todo de forma automática.

📊 Resultado
El pipeline muestra en consola:

Código
[1/3] Ejecutando Día 03...
[2/3] Ejecutando Día 04...
[3/3] Exportando PDF (Día 05)...
Pipeline completado con éxito.
Y genera un log como:

Código
2026-02-02 07:12 — Pipeline completado correctamente en 12.4 segundos.
✨ Nota final
Este pipeline es totalmente funcional, pero puede ampliarse tanto como necesites:
envío automático por email, ejecución programada, integración con APIs, dashboards web… lo que haga falta para llevar tu sistema de reporting al siguiente nivel.