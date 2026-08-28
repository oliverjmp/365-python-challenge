import pytest
from src.tracker import MLflowTracker

def test_mlflow_tracker_logging(tmp_path):
    db_path = tmp_path / "test_mlflow.db"
    tracking_uri = f"sqlite:///{db_path}"
    
    tracker = MLflowTracker(tracking_uri=tracking_uri)
    
    params = {"alpha": 0.5, "solver": "adam"}
    metrics = {"loss": 0.04, "accuracy": 0.98}
    
    result = tracker.log_run(
        experiment_name="Unit-Test-Experiment",
        run_name="test-run-1",
        params=params,
        metrics=metrics
    )
    
    assert result["status"] == "LOGGED"
    assert result["run_id"] is not None
    assert result["params"] == params
    assert result["metrics"] == metrics

def test_mlflow_empty_experiment_name():
    tracker = MLflowTracker()
    with pytest.raises(ValueError, match="El nombre del experimento no puede estar vacío."):
        tracker.create_or_set_experiment("")