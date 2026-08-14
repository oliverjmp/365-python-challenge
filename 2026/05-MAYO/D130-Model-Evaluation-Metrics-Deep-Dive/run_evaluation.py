import logging
import numpy as np
from src.evaluator import ModelEvaluator

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    logging.info("=== Iniciando Evaluación Profunda de Modelos (D130) ===")
    
    # Simulación de etiquetas reales y probabilidades arrojadas por un clasificador
    np.random.seed(42)
    y_true = np.array([0, 0, 0, 1, 1, 1, 0, 1, 0, 1])
    y_scores = np.array([0.12, 0.35, 0.22, 0.85, 0.78, 0.92, 0.45, 0.68, 0.29, 0.95])
    
    logging.info("Inicializando ModelEvaluator...")
    evaluator = ModelEvaluator(y_true, y_scores)
    
    # 1. Matriz de Confusión detallada
    cm = evaluator.confusion_matrix_detailed()
    logging.info(f"Matriz de Confusión Desglosada: {cm}")
    
    # 2. Curva ROC-AUC
    roc_auc, fpr, tpr = evaluator.roc_auc_metrics()
    logging.info(f"Puntaje ROC-AUC calculado: {roc_auc:.4f}")
    
    # 3. Curva Precision-Recall
    pr_auc, precision, recall = evaluator.precision_recall_metrics()
    logging.info(f"Puntaje PR-AUC calculado: {pr_auc:.4f}")
    
    # 4. Reporte de Clasificación
    report = evaluator.full_classification_report()
    print("\n--- Reporte de Clasificación ---")
    print(report)
    print("--------------------------------")
    
    logging.info("=== Hito D130 Ejecutado Exitosamente ===")

if __name__ == "__main__":
    main()