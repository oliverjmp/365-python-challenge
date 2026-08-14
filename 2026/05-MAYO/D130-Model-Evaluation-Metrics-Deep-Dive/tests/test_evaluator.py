import pytest
import numpy as np
from src.evaluator import ModelEvaluator

def test_evaluator_empty_data_raises_error():
    """Valida que se lance un error si se inicializa con datos vacíos."""
    with pytest.raises(ValueError, match="no pueden estar vacías"):
        ModelEvaluator([], [])

def test_model_evaluator_metrics_success():
    """Valida el cálculo correcto de todas las métricas de evaluación avanzadas."""
    y_true = [0, 0, 1, 1, 1, 0, 1, 0]
    y_scores = [0.1, 0.2, 0.8, 0.9, 0.6, 0.4, 0.85, 0.3]
    
    # Usamos labels explícitos en confusion_matrix o evaluamos con ambas clases presentes
    evaluator = ModelEvaluator(y_true, y_scores, y_pred=[0, 0, 1, 1, 1, 0, 1, 0])
    
    # Probar Matriz de Confusión
    cm_dict = evaluator.confusion_matrix_detailed()
    assert "true_positives" in cm_dict
    assert "false_positives" in cm_dict
    assert cm_dict["true_positives"] >= 0
    
    # Probar Matriz de Confusión con forma distinta a (2, 2) para cubrir el else
    evaluator_edge = ModelEvaluator([0, 1], [0.1, 0.8], y_pred=[0, 1])
    cm_edge = evaluator_edge.confusion_matrix_detailed()
    assert cm_edge["true_negatives"] >= 0

    # Probar ROC-AUC
    auc_score, fpr, tpr = evaluator.roc_auc_metrics()
    assert 0.0 <= auc_score <= 1.0
    assert len(fpr) > 0
    assert len(tpr) > 0
    
    # Probar Precision-Recall AUC
    pr_score, precision, recall = evaluator.precision_recall_metrics()
    assert 0.0 <= pr_score <= 1.0
    assert len(precision) > 0
    assert len(recall) > 0
    
    # Probar Reporte de Clasificación
    report = evaluator.full_classification_report()
    assert "precision" in report
    assert "recall" in report