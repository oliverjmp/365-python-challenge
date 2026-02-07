📄 README — Día 08 (Pipeline Maestro + Resumen Ejecutivo + Logging Avanzado)
Autor: Oliver Javier Morales Pérez
Proyecto: 365 Python Challenge
Fecha: 08 de Enero

🚀 Descripción General
El Día 08 introduce un componente clave en cualquier ecosistema profesional de reporting:
un Pipeline Maestro capaz de ejecutar, supervisar y documentar todas las etapas del flujo de trabajo construido en los días anteriores.

Este módulo no solo ejecuta los scripts del Día 03 al Día 07, sino que además:

Registra el estado de cada módulo

Mide tiempos de ejecución

Genera un log maestro con trazabilidad completa

Produce un resumen ejecutivo listo para auditoría o comunicación interna

Mantiene la arquitectura modular y escalable del proyecto

El resultado es un pipeline robusto, profesional y completamente automatizado.

🎯 Objetivos del Día 08
Ejecutar secuencialmente los módulos del Día 03 al Día 07

Registrar el estado de cada ejecución (OK / ERROR)

Medir la duración de cada etapa

Generar un archivo de log detallado

Crear un resumen ejecutivo en texto plano

Consolidar el ecosistema de reporting en un flujo único y trazable

🧩 Módulos ejecutados por el Pipeline Maestro
Día	Módulo	Descripción
03	Limpieza de datos	Carga, limpieza y exportación del Excel base
04	Dashboard Premium	Generación del dashboard ejecutivo
05	Exportación PDF	Creación del informe PDF final
06	Pipeline Automático	Ejecución integrada de los días 03–05
07	Envío Simulado	Simulación profesional del envío del informe
🛠 Tecnologías utilizadas
Python 3

os.system() para ejecución de módulos

Manejo de rutas dinámicas

Sistema de logs

Generación de reportes ejecutivos

No se utilizan APIs externas ni credenciales sensibles.

📦 Estructura del proyecto
Código
2026/
│── 03-ENERO/
│── 04-ENERO/
│── 05-ENERO/
│── 06-ENERO/
│── 07-ENERO/
│── 08-ENERO/
│     ├── main.py
│     ├── README.md
│     ├── logs/
│     │     └── pipeline_YYYY-MM-DD_HH-MM-SS.log
│     └── reportes/
│           └── resumen_ejecutivo.txt
▶️ Cómo ejecutar el pipeline maestro
Desde la carpeta raíz del proyecto:

Código
python 2026/08-ENERO/main.py
El sistema:

Ejecutará cada módulo del Día 03 al Día 07

Mostrará el estado en consola

Creará un log maestro en /logs/

Generará un resumen ejecutivo en /reportes/

📊 Ejemplo de salida en consola
Código
=== EJECUCIÓN DEL PIPELINE — DÍA 08 ===

Ejecutando: Día 03 — Limpieza de datos
[OK] Archivo 'informe_cripto.xlsx' generado y formateado correctamente.

Ejecutando: Día 04 — Dashboard
[OK] Dashboard premium generado.

Ejecutando: Día 05 — Exportación PDF
[OK] PDF generado correctamente.

Ejecutando: Día 06 — Pipeline Automático
[OK] Pipeline completado correctamente.

Ejecutando: Día 07 — Envío Simulado
[OK] Simulación de envío completada.

Log maestro generado: logs/pipeline_2026-02-02_20-56-26.log
Resumen ejecutivo generado: reportes/resumen_ejecutivo.txt

Pipeline completado.
📝 Resumen Ejecutivo generado
El archivo resumen_ejecutivo.txt incluye:

Fecha y hora

Estado de cada módulo

Duración de cada etapa

Conclusión del pipeline

Indicador de calidad final

Ejemplo:

Código
=== RESUMEN EJECUTIVO — DÍA 08 ===

Fecha de ejecución: 02/02/2026 20:56:26

Día 03 — Limpieza de datos
Estado: OK
Duración: 1.24 segundos

Día 04 — Dashboard
Estado: OK
Duración: 1.08 segundos

Día 05 — Exportación PDF
Estado: OK
Duración: 10.44 segundos

Día 06 — Pipeline Automático
Estado: OK
Duración: 12.76 segundos

Día 07 — Envío Simulado
Estado: OK
Duración: 0.52 segundos

Conclusión:
El pipeline se ejecutó correctamente y está listo para distribución.
🛡 Seguridad
Este módulo:

No usa credenciales

No envía correos reales

No expone datos sensibles

Es completamente seguro para repositorios públicos