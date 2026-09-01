import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from mlflow.tracking import MlflowClient

class ModelRegistryManager:
    def __init__(self, tracking_uri: str = "sqlite:///mlflow.db"):
        self.tracking_uri = tracking_uri
        mlflow.set_tracking_uri(self.tracking_uri)
        self.client = MlflowClient()

    def train_and_register_model(self, model_name: str, experiment_name: str = "Registry-Experiment") -> dict:
        """Entrena un modelo base, lo registra en MLflow y retorna los datos de la versión."""
        if not model_name:
            raise ValueError("El nombre del modelo no puede estar vacío.")
            
        mlflow.set_experiment(experiment_name)
        X, y = make_classification(n_samples=100, n_features=10, random_state=42)
        
        model = RandomForestClassifier(n_estimators=10, random_state=42)
        model.fit(X, y)

        with mlflow.start_run() as run:
            mlflow.log_param("n_estimators", 10)
            
            # Registrar modelo con Model Registry integrado
            model_info = mlflow.sklearn.log_model(
                sk_model=model,
                artifact_path="model",
                registered_model_name=model_name
            )

        # Obtener la última versión creada para este modelo
        latest_versions = self.client.get_latest_versions(model_name)
        version = latest_versions[-1].version if latest_versions else "1"

        return {
            "model_name": model_name,
            "version": version,
            "run_id": run.info.run_id,
            "status": "REGISTERED"
        }

    def transition_model_stage(self, model_name: str, version: str, stage: str) -> dict:
        """Transiciona una versión de modelo específica a una etapa operativa (Staging / Production / Archived)."""
        valid_stages = ["Staging", "Production", "Archived"]
        if stage not in valid_stages:
            raise ValueError(f"Etapa inválida. Debe ser una de: {valid_stages}")

        self.client.transition_model_version_stage(
            name=model_name,
            version=version,
            stage=stage
        )

        return {
            "model_name": model_name,
            "version": version,
            "current_stage": stage,
            "status": "TRANSITIONED"
        }