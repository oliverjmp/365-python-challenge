📘 Día 10 – Analizador Universal ULTRA
Análisis avanzado de textos con Streamlit
Este proyecto forma parte del reto 365 Python Challenge y consiste en una aplicación web desarrollada con Streamlit que analiza cualquier texto y genera un informe completo con múltiples dimensiones lingüísticas, estadísticas y semánticas.

La versión ULTRA incluye mejoras significativas en clasificación, análisis narrativo, estilo literario y extracción de patrones.

🚀 Características principales
🔍 1. Detección automática del tipo de texto
El sistema identifica el tipo de texto según palabras clave y patrones semánticos:

Narrativo

Fantasía

Cuento

Fábula

Técnico

Científico

Emocional

Religioso

Empresarial

📊 2. Estadísticas del texto
Incluye:

Palabras más frecuentes

Bigramas más comunes

Conteo total de palabras

🧠 3. Análisis TF‑IDF
Identifica los términos más relevantes del texto según su peso estadístico.

❤️ 4. Análisis de tono emocional
Detecta emociones predominantes:

Miedo

Tristeza

Ira

Alegría

Tensión

📝 5. Resumen narrativo automático
Genera un resumen estructurado en:

Inicio

Desarrollo

Final

🎨 6. Detección de estilo literario
Clasifica el estilo según patrones lingüísticos:

Poético

Descriptivo

Directo

Clásico

Moderno

🖥️ Interfaz
La aplicación permite:

Pegar texto manualmente

Subir archivos .txt

Activar o desactivar módulos de análisis

Visualizar resultados en tiempo real

🛠️ Tecnologías utilizadas
Python 3.10+

Streamlit

scikit-learn (TF‑IDF)

Regex

Collections.Counter

📂 Estructura del proyecto
Código
📁 proyecto-dia10
│── app.py
│── README.md
│── requirements.txt
▶️ Cómo ejecutar el proyecto
Instala dependencias:

Código
pip install -r requirements.txt
Ejecuta la app:

Código
streamlit run app.py
Abre en el navegador:

Código
http://localhost:8501
📦 requirements.txt recomendado
Código
streamlit
scikit-learn
(FPDF eliminado porque ya no se usa)

🧩 Mejoras futuras
Exportación a PDF (cuando se desee reactivar)

Detección de personajes

Análisis de diálogos

Gráficos de frecuencia

Exportación a Excel o JSON

👨‍💻 Autor
Oliver Javier Morales Pérez  
Reto: 365 Python Challenge  
Día 10 – Analizador Universal ULTRA