🚀 Día 19: Pipeline de BI - Procesamiento Batch (Masivo)

🎯 Objetivo del Reto

Evolucionar de análisis individuales a un sistema de Procesamiento en Lote (Batch). El objetivo es automatizar la lectura de 

archivos externos (CSV/Excel) y aplicar modelos de NLP a gran escala para generar reportes de inteligencia de negocio.

🛠️ Stack Tecnológico

Pandas: Utilizado para la manipulación y análisis de estructuras de datos (DataFrames).

TextBlob: Motor de análisis de sentimiento aplicado en bloque.

Pathlib: Gestión de rutas dinámicas para asegurar la portabilidad del pipeline.

🔄 Flujo de Trabajo (ETL)

Extract (Extracción): Lectura automatizada de comentarios_clientes.csv.

Transform (Transformación): * Limpieza de datos.

Aplicación de lógica de sentimientos en toda la columna mediante funciones lambda.

Clasificación categórica (POSITIVO, NEGATIVO, NEUTRO).

Load (Carga): Generación de un nuevo archivo reporte_sentimientos_final.csv con los resultados enriquecidos.


Shutterstock

Explorar

📊 Capacidades de Análisis

El script genera un resumen estadístico automático en consola que permite visualizar la distribución de sentimientos del conjunto 

de datos procesado:

Conteo por categoría: (Ej. POSITIVO: 2, NEGATIVO: 2, NEUTRO: 1).

Exportación de Score: Permite filtrado numérico avanzado en herramientas de visualización.

🔒 Seguridad
Al igual que en días anteriores, el código es 100% portable. No utiliza rutas locales fijas, permitiendo su ejecución en 

cualquier entorno de producción sin revelar información del sistema local.