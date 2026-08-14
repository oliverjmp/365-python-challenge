import logging
from src.nb_text_classifier import NaiveBayesTextClassifier

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Demostración del Clasificador Naive Bayes de Textos (D139) ===")

    # Dataset de entrenamiento simulado con categorías claras
    training_corpus = [
        "Desarrollo de software con python y frameworks modernos",
        "Inteligencia artificial aprendizaje automático y redes neuronales",
        "Bases de datos relacionales y optimización de consultas sql",
        "Resultado del partido de futbol y resumen de la jornada deportiva",
        "Campeonato mundial de baloncesto y estadísticas de jugadores",
        "Medalla de oro en atletismo en los juegos olímpicos"
    ]
    
    training_labels = [
        "Tecnología", "Tecnología", "Tecnología",
        "Deportes", "Deportes", "Deportes"
    ]

    logging.info(f"Entrenando clasificador con {len(training_corpus)} documentos distribuidos en dos clases.")

    # Inicializar y ajustar el clasificador
    nb_classifier = NaiveBayesTextClassifier(alpha=1.0, ngram_range=(1, 2))
    nb_classifier.fit(training_corpus, training_labels)
    logging.info("Modelo ajustado exitosamente.")

    # Textos nuevos para clasificación
    new_documents = [
        "Nuevo algoritmo de machine learning programado en python",
        "Gran actuación en el partido de futbol de la liga deportiva"
    ]

    logging.info("Realizando predicciones sobre nuevos documentos...")
    predictions = nb_classifier.predict(new_documents)
    probabilities = nb_classifier.predict_proba(new_documents)

    for doc, pred, prob in zip(new_documents, predictions, probabilities):
        logging.info(f"Texto: '{doc}'")
        logging.info(f" -> Predicción: {pred} (Probabilidades por clase: {prob})")

    logging.info("=== Hito D139 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()