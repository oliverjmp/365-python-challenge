import logging
import numpy as np
from src.tfidf_transformer import TextTfidfVectorizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración de Vectorización TF-IDF (D138) ===")

    # Corpus de ejemplo simulando descripciones de artículos tecnológicos
    corpus = [
        "Inteligencia artificial y aprendizaje automático en python",
        "Procesamiento de lenguaje natural y análisis de texto avanzado",
        "Modelos de clasificación supervisada con scikit learn",
        "Redes neuronales profundas para visión artificial y texto"
    ]

    logging.info(f"Corpus cargado con {len(corpus)} documentos de texto.")

    # Inicializar el vectorizador TF-IDF con n-gramas (1 a 2)
    vectorizer = TextTfidfVectorizer(ngram_range=(1, 2), max_features=15)
    
    # Ajustar y transformar
    dense_matrix = vectorizer.fit_transform(corpus)
    logging.info(f"Matriz TF-IDF generada con forma (Documentos x Características): {dense_matrix.shape}")

    # Obtener vocabulario extraído
    features = vectorizer.get_feature_names()
    logging.info(f"Vocabulario de características (Términos / N-gramas): {features}")

    # Transformar un nuevo documento de prueba
    new_document = ["Aplicaciones de inteligencia artificial en procesamiento de texto"]
    logging.info(f"Transformando nuevo documento: '{new_document[0]}'")
    new_matrix = vectorizer.transform(new_document)
    
    logging.info(f"Forma de la matriz resultante para el nuevo documento: {new_matrix.shape}")
    logging.info("=== Hito D138 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()