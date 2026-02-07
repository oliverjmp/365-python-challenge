📄 README — Día 07 (Simulación Profesional de Envío de Email)
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge

🚀 Descripción del proyecto
En este séptimo día del reto, se implementa un módulo profesional de envío simulado, diseñado para integrarse con el pipeline automático del Día 06 sin comprometer la seguridad del repositorio.

El objetivo es reproducir el comportamiento de un sistema real de distribución de informes, pero sin enviar correos electrónicos reales, evitando así exponer credenciales, datos personales o configuraciones sensibles.

Este enfoque es ideal para:

Repositorios públicos

Proyectos educativos

Sistemas en desarrollo

Pipelines que requieren un “hook” de envío sin depender de servicios externos

🎯 Objetivos del Día 07
Detectar el PDF generado en el Día 05

Simular el envío del informe

Mostrar un mensaje profesional en consola

Generar un log detallado del envío simulado

Dejar el módulo preparado para integraciones futuras con:

Gmail API

Outlook

Servicios externos (SendGrid, Mailjet, etc.)

🧠 Tecnologías utilizadas
Python 3

Manejo de rutas dinámicas

Sistema de logs

Simulación de procesos corporativos

No se utilizan APIs externas ni credenciales reales.

📦 Estructura del proyecto
Código
dia_07_Envio_Simulado/
│── main.py
│── README.md
└── logs/
    └── envio_simulado_YYYY-MM-DD_HH-MM-SS.log
▶️ Cómo ejecutar
Asegúrate de haber completado los días anteriores, especialmente el Día 05 (PDF generado).

Ejecuta:

Código
python main.py
Verás en consola:

Estado del envío

Vista previa del email

Archivo adjunto detectado

Mensaje profesional de simulación

Se generará un archivo de log en la carpeta /logs/.

📧 Ejemplo de salida en consola
Código
=== ENVÍO SIMULADO — DÍA 07 ===

Fecha de ejecución: 02/02/2026 07:40:12
Estado: OK
Acción: Simulación de envío del informe ejecutivo
Destinatario simulado: destinatario@empresa.com
Asunto simulado: Informe Ejecutivo — Mercado Cripto
Archivo adjunto detectado: ../05-ENERO/informe_cripto.pdf

Vista previa del email que se enviaría:
----------------------------------------
Para: destinatario@empresa.com
Asunto: Informe Ejecutivo — Mercado Cripto

Cuerpo:
Estimado equipo,

Adjunto el informe ejecutivo del mercado cripto correspondiente al día de hoy.

Incluye:
• Datos limpios
• Dashboard premium
• Gráficos ejecutivos
• PDF final

Saludos,
Oliver Javier Morales Pérez
365 Python Challenge
----------------------------------------

Simulación completada correctamente.
Log generado: logs/envio_simulado_2026-02-02_07-40-12.log
🛡 Seguridad
Este módulo:

No envía correos reales

No requiere contraseñas

No usa APIs externas

No expone datos personales

Es completamente seguro para repositorios públicos

✨ Nota final
El Día 07 deja el sistema listo para que, en el futuro, puedas integrar un servicio real de envío de correos sin modificar la estructura del pipeline.

Este diseño modular y seguro es típico de proyectos profesionales donde la automatización debe coexistir con buenas prácticas de seguridad.