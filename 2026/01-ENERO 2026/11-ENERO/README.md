🧠 Día 11 — Analizador de Sentimientos con Modelo Entrenado (Dataset Ampliado)
Este módulo implementa un analizador de sentimientos en español entrenado con un dataset ampliado de más de 400 frases clasificadas en cinco categorías:

positivo

negativo

neutro

sarcasmo

ambiguo

El objetivo del Día 11 es construir un modelo propio, entrenado desde cero, utilizando técnicas clásicas de Machine Learning y desplegado en una interfaz web con Streamlit.

🎯 Objetivos del Día 11
Construir un dataset ampliado y balanceado.

Entrenar un modelo de clasificación de texto usando:

TF‑IDF para vectorización

Logistic Regression como clasificador

Evaluar el modelo con métricas reales:

classification report

matriz de confusión

Integrar todo en una aplicación Streamlit interactiva.

Permitir al usuario escribir texto libre y obtener:

la clase predicha

las probabilidades por categoría

📦 Estructura del proyecto
Código
11-ENERO/
│── app.py
│── README.md
El archivo app.py contiene:

Dataset ampliado (positivo, negativo, neutro, sarcasmo, ambiguo)

Mezcla y construcción del DataFrame

Entrenamiento del modelo

Métricas

Interfaz Streamlit completa

🚀 Cómo ejecutar la aplicación
1. Instalar dependencias
En tu entorno local:

Código
pip install streamlit scikit-learn pandas
2. Ejecutar la app
Desde la carpeta 11-ENERO:

Código
streamlit run app.py
3. Abrir en el navegador
Streamlit abrirá automáticamente:

Código
http://localhost:8501/
Si no se abre, puedes copiar la URL manualmente.

📊 Dataset ampliado
El modelo se entrena con:

100 frases positivas

100 frases negativas

100 frases neutras

50 frases sarcásticas

50 frases ambiguas

Este dataset permite que el modelo:

Reconozca sentimientos claros

Maneje textos ambiguos

Identifique sarcasmo básico

Sea más robusto ante variaciones de lenguaje

🧪 Evaluación del modelo
La app muestra:

classification_report

matriz de confusión

predicción + probabilidades

Esto permite analizar:

qué clases están mejor aprendidas

dónde se confunde el modelo

cómo responde ante textos trampa

🖥 Interfaz Streamlit
La interfaz incluye:

Vista previa del dataset

Métricas del modelo

Matriz de confusión

Área de texto para ingresar frases

Botón para analizar

Probabilidades por clase

🧩 Limitaciones conocidas
El modelo no entiende sarcasmo complejo (ningún modelo clásico lo hace).

No captura contexto profundo ni ironía avanzada.

Depende fuertemente de palabras clave.

No usa embeddings ni modelos preentrenados (eso vendrá en días posteriores).