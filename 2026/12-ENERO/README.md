🧠 Día 12 — Detección de Idioma y Normalización Inteligente del Texto
Este módulo amplía el proyecto del Día 11 incorporando un pipeline profesional de preprocesamiento de texto, similar al que se utiliza en sistemas reales de NLP.
El objetivo es asegurar que el modelo reciba texto limpio, uniforme y en español, mejorando la calidad de las predicciones y evitando errores cuando el usuario introduce texto en otros idiomas.

🎯 Objetivos del Día 12
Detectar automáticamente el idioma del texto ingresado.

Normalizar el texto antes de enviarlo al modelo del Día 11.

Integrar el preprocesamiento en la app Streamlit.

Mostrar al usuario:

idioma detectado

texto original

texto normalizado

predicción final

probabilidades por clase

🧩 Funcionalidades implementadas
✔ Detección de idioma
Se utiliza langdetect para identificar si el texto está en español.
Si no lo está, la app muestra una advertencia antes de clasificar.

✔ Normalización avanzada del texto
El módulo preprocesamiento.py limpia el texto aplicando:

conversión a minúsculas

eliminación de tildes

eliminación de URLs

eliminación de emojis

reducción de caracteres repetidos

limpieza de signos y símbolos

normalización de espacios

Esto garantiza que el modelo reciba un texto uniforme y libre de ruido.

✔ Integración con el modelo del Día 11
El texto normalizado se envía al clasificador entrenado con el dataset ampliado de más de 400 frases.

📦 Archivos del Día 12
Código
12-ENERO/
│── app.py
│── preprocesamiento.py
│── README.md
🚀 Ejecución
Desde la carpeta 12-ENERO:

Código
streamlit run app.py
La aplicación se abrirá en:

Código
http://localhost:8501/
🧪 Ejemplo de funcionamiento
Entrada del usuario:

Código
Qué maravilla 😒… el sistema volvió a fallar justo cuando más lo necesitaba.
Pero bueno, “excelente servicio”, como siempre 🙃.
Salida del sistema:

Idioma detectado: es

Texto normalizado:
que maravilla el sistema volvio a fallar justo cuando mas lo necesitaba pero bueno excelente servicio como siempre

Sentimiento detectado: sarcasmo

Probabilidad dominante: 0.57