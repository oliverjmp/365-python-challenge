import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, precision_score

class ModelPipelineTrainer:
    def __init__(self, tracking_uri: str = "sqlite:///mlflow.db"):
        self.tracking_uri = tracking_uri
        mlflow.set_tracking_uri(self.tracking_uri)

    def generate_synthetic_data(self, n_samples: int = 1000, random_state: int = 42):
        """Genera un dataset sintético de clasificación para el pipeline."""
        X, y = make_classification(n_samples=n_samples, n_features=20, random_state=random_state)
        return train_test_split(X, y, test_size=0.2, random_state=random_state)

    def train_and_log(self, experiment_name: str, n_estimators: int = 100, max_depth: int = 5) -> dict:
        """Entrena un modelo Random Forest y registra métricas, parámetros y artefactos en MLflow."""
        if not experiment_name:
            raise ValueError("El nombre del experimento no puede estar vacío.")
            
        mlflow.set_experiment(experiment_name)
        X_train, X_test, y_train, y_test = self.generate_synthetic_data()

        with mlflow.start_run() as run:
            # Hiperparámetros
            params = {"n_estimators": n_estimators, "max_depth": max_depth}
            for key, value in params.items():
                mlflow.log_param(key, value)

            # Entrenamiento del modelo Scikit-learn
            model = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth, random_state=42)
            model.fit(X_train, y_train)

            # Predicciones y Métricas
            preds = model.predict(X_test)
            acc = accuracy_score(y_test, preds)
            prec = precision_score(y_test, preds, zero_division=0)

            metrics = {"accuracy": float(acc), "precision": float(prec)}
            for key, value in metrics.items():
                mlflow.log_metric(key, value)

            # Registro del artefacto del modelo
            mlflow.sklearn.log_model(model, "random_forest_model")

            return {
                "run_id": run.info.run_id,
                "status": "SUCCESS",
                "params": params,
                "metrics": metrics
            }