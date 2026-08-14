import numpy as np
from sklearn.metrics import (
    confusion_matrix,
    roc_auc_score,
    roc_curve,
    precision_recall_curve,
    auc,
    classification_report
)
from typing import Dict, Tuple, Union

class ModelEvaluator:
    """Motor avanzado de evaluación de métricas de clasificación para modelos de Machine Learning."""
    
    def __init__(self, y_true: Union[np.ndarray, list], y_pred_proba: Union[np.ndarray, list], y_pred: Union[np.ndarray, list] = None):
        if len(y_true) == 0 or len(y_pred_proba) == 0:
            raise ValueError("Las etiquetas reales y las probabilidades no pueden estar vacías.")
            
        self.y_true = np.array(y_true)
        self.y_pred_proba = np.array(y_pred_proba)
            
        if y_pred is not None:
            self.y_pred = np.array(y_pred)
        else:
            self.y_pred = (self.y_pred_proba >= 0.5).astype(int)

    def confusion_matrix_detailed(self) -> Dict[str, int]:
        """Calcula la matriz de confusión y desglosa sus componentes principales (TP, TN, FP, FN)."""
        cm = confusion_matrix(self.y_true, self.y_pred)
        if cm.shape == (2, 2):
            tn, fp, fn, tp = cm.ravel()
        else:
            tn, fp, fn, tp = int(cm[0, 0]), 0, 0, int(cm[1, 1]) if cm.size > 1 else 0
            
        return {
            "true_negatives": int(tn),
            "false_positives": int(fp),
            "false_negatives": int(fn),
            "true_positives": int(tp)
        }

    def roc_auc_metrics(self) -> Tuple[float, np.ndarray, np.ndarray]:
        """Calcula el puntaje ROC-AUC y extrae los puntos de la curva (FPR, TPR)."""
        auc_score = roc_auc_score(self.y_true, self.y_pred_proba)
        fpr, tpr, thresholds = roc_curve(self.y_true, self.y_pred_proba)
        return float(auc_score), fpr, tpr

    def precision_recall_metrics(self) -> Tuple[float, np.ndarray, np.ndarray]:
        """Calcula el área bajo la curva Precision-Recall (PR-AUC) y sus componentes."""
        precision, recall, thresholds = precision_recall_curve(self.y_true, self.y_pred_proba)
        pr_auc = auc(recall, precision)
        return float(pr_auc), precision, recall

    def full_classification_report(self) -> str:
        """Genera un reporte detallado en texto con precision, recall y f1-score por clase."""
        return classification_report(self.y_true, self.y_pred, zero_division=0)