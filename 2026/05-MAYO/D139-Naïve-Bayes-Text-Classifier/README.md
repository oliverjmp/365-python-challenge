# D139 - Naïve Bayes Text Classifier

Este hito implementa un **clasificador automático de documentos de texto** utilizando el algoritmo estadístico `Multinomial Naive Bayes` combinado con vectorización `TF-IDF` a través de un `Pipeline` robusto de `Scikit-learn`.

## Características Principales
- **Pipeline Integrado:** Automatiza la transformación de texto plano a matrices numéricas TF-IDF y su posterior clasificación probabilística sin fugas de datos.
- **Optimización de Laplace (Alpha):** Soporta el parámetro de suavizado alpha para prevenir probabilidades nulas ante palabras no vistas en el entrenamiento.
- **Estimación de Probabilidades:** Capacidad de retornar distribuciones de probabilidad asociadas a cada clase para evaluar la confianza de la predicción.

## 💡 ¿Para qué se usa y Casos de Uso Prácticos?
El clasificador Multinomial Naive Bayes es el estándar de la industria para tareas de PLN por su alta velocidad de procesamiento y efectividad en corpus de alta dimensionalidad.

### Ejemplos de Uso:
1. **Detección Automática de Correo Spam o Phishing:**
   * *Caso:* Clasificar correos electrónicos entrantes como "Spam" o "Seguro" según la frecuencia de términos sospechosos.
   * *Uso:* Alimentar el modelo con miles de correos etiquetados para bloquear amenazas automáticamente.
2. **Análisis de Sentimientos en Reseñas de Productos:**
   * *Caso:* Categorizar opiniones de usuarios en tiendas en línea como "Positivo", "Neutral" o "Negativo".
   * *Uso:* Automatizar el monitoreo de satisfacción del cliente a escala masiva.

## 📂 Estructura del Proyecto
```text
D139-Naïve-Bayes-Text-Classifier/
│
├── src/
│   ├── __init__.py
│   └── nb_text_classifier.py
├── tests/
│   └── test_nb_text_classifier.py
├── run_classifier.py
├── requirements.txt
└── README.md