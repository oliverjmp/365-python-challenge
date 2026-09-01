import pytest
from src.registry_manager import ModelRegistryManager

def test_model_registration_and_transition(tmp_path):
    db_path = tmp_path / "test_mlflow.db"
    tracking_uri = f"sqlite:///{db_path}"
    
    manager = ModelRegistryManager(tracking_uri=tracking_uri)
    model_name = "TestClassifierModel"
    
    # Registrar modelo
    reg_result = manager.train_and_register_model(model_name=model_name)
    assert reg_result["status"] == "REGISTERED"
    assert reg_result["model_name"] == model_name
    
    version = reg_result["version"]
    
    # Transicionar etapa a Production
    trans_result = manager.transition_model_stage(
        model_name=model_name,
        version=version,
        stage="Production"
    )
    assert trans_result["status"] == "TRANSITIONED"
    assert trans_result["current_stage"] == "Production"

def test_empty_model_name():
    manager = ModelRegistryManager()
    with pytest.raises(ValueError, match="El nombre del modelo no puede estar vacío."):
        manager.train_and_register_model(model_name="")

def test_invalid_stage():
    manager = ModelRegistryManager()
    with pytest.raises(ValueError, match="Etapa inválida"):
        manager.transition_model_stage(model_name="Model", version="1", stage="InvalidStage")