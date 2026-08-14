# D138 - Text Vectorization with TF-IDF

Este hito implementa un **motor robusto de vectorización de texto no estructurado** utilizando `TfidfVectorizer` de `Scikit-learn`, permitiendo transformar colecciones de documentos de texto en matrices numéricas ponderadas (Term Frequency-Inverse Document Frequency).

## Características Principales
- **Ponderación TF-IDF:** Evalúa la importancia relativa de una palabra en un documento en relación con todo el corpus, penalizando términos demasiado frecuentes e irrelevantes.
- **Soporte de N-gramas:** Permite extraer secuencias de palabras contiguas (unigramas, bigramas, etc.) para capturar mejor el contexto semántico.
- **Transformación de Nuevos Textos:** Capacidad de ajustar el vocabulario sobre un corpus de entrenamiento y proyectar nuevos documentos invisibles de forma consistente.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
La vectorización TF-IDF es el paso fundamental en el Procesamiento de Lenguaje Natural (PLN) para convertir texto plano en entradas compatibles con algoritmos de Machine Learning.

### Ejemplos de Uso:
1. **Clasificación Automática de Reseñas o Tickets de Soporte:**
   * *Caso:* Categorizar correos electrónicos entrantes como "Spam" o "Legítimos" basándose en el contenido de sus palabras.
   * *Uso:* Convertir los mensajes en matrices TF-IDF para alimentar modelos de clasificación supervisada (como Regresión Logística o SVM).
2. **Motores de Búsqueda y Recuperación de Información (Information Retrieval):**
   * *Caso:* Encontrar documentos o artículos de una base de datos que guarden mayor similitud semántica con una consulta de búsqueda de un usuario.

## 📂 Estructura del Proyecto
```text
D138-Text-Vectorization-TFIDF/
│
├── src/
│   ├── __init__.py
│   └── tfidf_transformer.py
├── tests/
│   └── test_tfidf_transformer.py
├── run_tfidf.py
├── requirements.txt
└── README.md