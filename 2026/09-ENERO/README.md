🧠 Día 09 — Analizador Universal de Textos
Un sistema inteligente capaz de analizar cualquier tipo de texto y adaptar su interpretación según el género detectado.

Este módulo no depende de días anteriores y funciona como una herramienta autónoma, moderna y poderosa para análisis lingüístico, narrativo, técnico o estratégico.

🚀 Descripción general
El Analizador Universal de Textos identifica automáticamente el tipo de contenido que recibe y genera un informe ejecutivo adaptado.
Es capaz de procesar textos:

📘 Religiosos

📙 Narrativos

📗 Técnicos

📕 Empresariales

💛 Emocionales

🔬 Científicos

⚪ Desconocidos (si no encaja en ninguna categoría)

El sistema utiliza heurísticas inteligentes basadas en vocabulario clave, patrones lingüísticos y estructuras comunes para clasificar el texto y aplicar un análisis especializado.

🧩 Características principales
🔍 1. Detección automática del tipo de texto
El sistema identifica el género del contenido mediante intersección de palabras clave:

Religioso

Empresarial

Técnico

Emocional

Narrativo

Científico

Desconocido

🧠 2. Análisis especializado según el tipo
Cada categoría activa un módulo de análisis distinto:

Religioso: temas teológicos, símbolos, estructura literaria

Narrativo: trama, conflicto, arquetipos

Técnico: conceptos, procesos, terminología

Empresarial: riesgos, oportunidades, estrategia

Emocional: tono, emociones dominantes

Científico: evidencia, método, conclusiones

📊 3. Métricas lingüísticas
Palabras más frecuentes

Bigramas más comunes

Limpieza de stopwords

Conteo total de palabras

📝 4. Informe ejecutivo adaptado
El reporte final incluye:

Tipo de texto detectado

Análisis especializado

Frecuencias

Bigramas

Resumen ejecutivo contextual

📁 Estructura del proyecto
Código
09-ENERO/
│
├── main.py
│
├── textos/
│   └── entrada.txt
│
└── reportes/
    └── informe_tendencias.txt
▶️ Cómo usarlo
1. Crear la carpeta de entrada
Dentro de 09-ENERO/:

Código
textos/
2. Crear el archivo de texto
Dentro de textos/:

Código
entrada.txt
Pega cualquier contenido:

Un capítulo bíblico

Un artículo de negocios

Un poema

Un manual técnico

Un texto emocional

Un paper científico

3. Ejecutar el programa
bash
python main.py
4. Revisar el informe generado
Se creará automáticamente en:

Código
reportes/informe_tendencias.txt
🧪 Ejemplos de uso
📘 Si analizas Génesis 1–2:
Detecta: Religioso

Temas: creación, origen, relación Dios-humanidad

Bigramas: “la tierra”, “los cielos”, etc.

Resumen adaptado al género

📕 Si analizas un artículo empresarial:
Detecta: Empresarial

Riesgos, oportunidades, estrategia

Recomendaciones ejecutivas

💛 Si analizas un poema:
Detecta: Emocional

Emociones dominantes

Tono y motivos

🛠️ Tecnologías utilizadas
Python 3

Expresiones regulares

Heurísticas lingüísticas

Contadores de frecuencia

Procesamiento básico de texto

Sin dependencias externas.
Sin APIs.
100% local.