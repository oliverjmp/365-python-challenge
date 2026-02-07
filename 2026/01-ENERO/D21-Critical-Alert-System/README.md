# ⚠️ Día 21: Sistema de Alertas de Sentimiento Crítico

## 🎯 Objetivo del Reto
Implementar una capa de **Analítica de Respuesta** que identifique automáticamente valores atípicos (outliers) negativos dentro de un conjunto de datos procesado.

## 🛠️ Lógica de Negocio
* **Umbral Crítico:** Se define un Score de **-0.7** como punto de alerta roja.
* **Filtrado Dinámico:** Uso de Pandas para aislar únicamente las filas que requieren atención inmediata.
* **Logging:** Generación de un archivo `LOG_ALERTAS_CRITICAS.txt` para trazabilidad de errores.

## 🚀 Impacto en BI
Este script permite pasar de una "BI Pasiva" (mirar reportes) a una "BI Activa" (reaccionar a eventos en tiempo real), reduciendo drásticamente el tiempo de respuesta ante crisis de reputación o fallos de sistema.