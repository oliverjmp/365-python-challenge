🤖 Día 17: Extracción de Entidades con NLP (NER)

🎯 Objetivo del Reto

Desarrollar un motor de Reconocimiento de Entidades Nombradas (NER) utilizando Inteligencia Artificial para transformar texto no

 estructurado en datos organizados. Esta herramienta permite automatizar la identificación de elementos clave en grandes

 volúmenes de texto, una habilidad esencial para la analítica avanzada en Business Intelligence.


🚀 Implementación Técnica

Motor de IA: spaCy.

Modelo Utilizado: es_core_news_md (español).

Capacidades de Extracción:

PER: Nombres de personas.

ORG: Organizaciones y empresas.

LOC: Localizaciones geográficas y ciudades.

Procesamiento Lingüístico: Lematización para normalizar palabras a su raíz léxica.

🔒 Seguridad y Portabilidad

Rutas Relativas: El script utiliza pathlib para gestionar archivos de forma dinámica.

Seguridad: No contiene rutas absolutas (C:\Users\...), lo que lo hace seguro para repositorios públicos de GitHub.

📂 Estructura de Datos (JSON)

El script procesa el texto y genera automáticamente un archivo estructurado:

JSON
{
    "entidades": [

        {"texto": "Oliver Morales Pérez", "tipo": "PER"},

        {"texto": "Microsoft", "tipo": "ORG"},

        {"texto": "Madrid", "tipo": "LOC"}
    ]
}
⌨️ Instrucciones de Ejecución

Asegúrate de tener instalado el modelo de español:

PowerShell

python -m spacy download es_core_news_md

Para ejecutarlo, simplemente usa el botón Play de VS Code sobre el archivo nlp_entidades.py.