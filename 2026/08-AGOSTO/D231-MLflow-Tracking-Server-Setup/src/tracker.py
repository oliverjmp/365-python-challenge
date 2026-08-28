import mlflow
import os

class MLflowTracker:
    def __init__(self, tracking_uri: str = "sqlite:///mlflow.db"):
        self.tracking_uri = tracking_uri
        mlflow.set_tracking_uri(self.tracking_uri)

    def create_or_set_experiment(self, experiment_name: str) -> str:
        """Configura o crea un experimento activo en el servidor de MLflow."""
        if not experiment_name:
            raise ValueError("El nombre del experimento no puede estar vacío.")
        mlflow.set_experiment(experiment_name)
        return experiment_name

    def log_run(self, experiment_name: str, run_name: str, params: dict, metrics: dict) -> dict:
        """Registra una ejecución de entrenamiento con hiperparámetros y métricas."""
        self.create_or_set_experiment(experiment_name)
        
        with mlflow.start_run(run_name=run_name) as run:
            for key, value in params.items():
                mlflow.log_param(key, value)
            for key, value in metrics.items():
                mlflow.log_metric(key, value)
                
            return {
                "run_id": run.info.run_id,
                "experiment_id": run.info.experiment_id,
                "status": "LOGGED",
                "params": params,
                "metrics": metrics
            }