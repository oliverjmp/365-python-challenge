import pytest
from src.pipeline_trainer import ModelPipelineTrainer

def test_pipeline_trainer_success(tmp_path):
    db_path = tmp_path / "test_mlflow.db"
    tracking_uri = f"sqlite:///{db_path}"
    
    trainer = ModelPipelineTrainer(tracking_uri=tracking_uri)
    result = trainer.train_and_log(
        experiment_name="Test-Classification-Experiment",
        n_estimators=10,
        max_depth=3
    )
    
    assert result["status"] == "SUCCESS"
    assert result["run_id"] is not None
    assert "accuracy" in result["metrics"]
    assert "precision" in result["metrics"]
    assert result["params"]["n_estimators"] == 10

def test_pipeline_empty_experiment_name():
    trainer = ModelPipelineTrainer()
    with pytest.raises(ValueError, match="El nombre del experimento no puede estar vacío."):
        trainer.train_and_log(experiment_name="")