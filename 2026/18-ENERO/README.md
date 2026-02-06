📊 Día 18: Análisis de Sentimiento (Versión Segura y Visual)

🎯 Objetivo del Reto

Desarrollar un sistema de Procesamiento de Lenguaje Natural (NLP) capaz de clasificar el tono emocional de textos en español.

Este módulo permite automatizar el triaje de comentarios de clientes, identificando rápidamente alertas (negativos) y casos de 

éxito (positivos).

🔒 Seguridad y Buenas Prácticas (Senior Level)

Rutas Dinámicas (pathlib): Se eliminaron todas las rutas absolutas (C:\Users\...). El script ahora utiliza rutas relativas, lo 

que lo hace 100% seguro para subir a GitHub público sin exponer el nombre de usuario del sistema.

Privacidad en Logs: La consola no imprime rutas internas del disco duro, solo resultados directos del procesamiento.

🚀 Funcionalidades

Traducción en Tiempo Real: Utiliza un puente de traducción para aplicar el motor de polaridad de TextBlob sobre textos en español.

Indicadores Visuales (Dashboard en Terminal):

 🟢 POSITIVO: Para scores mayores a 0.1.

🔴 NEGATIVO: Para scores menores a -0.1.

🟡 NEUTRO: Para frases informativas o sin carga emocional clara.

Persistencia de Datos: Exportación automática a resultado_sentimiento_dia18.json.

📂 Estructura de Salida

JSON
{
    "texto": "Oliver está haciendo un trabajo increíble con Python.",

    "sentimiento": "POSITIVO",

    "score": 0.8
}
⌨️ Comandos de Uso
Gracias a la configuración del Intérprete de Python 3.13 en VS Code, solo debes presionar el botón Play. El script detectará su

 ubicación automáticamente:

PowerShell

# Ejecución manual segura

python analisis_sentimiento.py