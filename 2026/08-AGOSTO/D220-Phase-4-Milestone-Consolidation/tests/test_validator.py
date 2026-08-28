import pytest
from src.pipeline_validator import MilestonePipelineValidator

def test_verify_consolidation_success():
    result = MilestonePipelineValidator.verify_consolidation_status("Fase-4-Milestone")
    assert result["status"] == "CONSOLIDATED"
    assert result["ci_cd_automated"] is True
    assert result["coverage_target"] == 100.0

def test_verify_consolidation_error():
    with pytest.raises(ValueError, match="ID de fase inválido"):
        MilestonePipelineValidator.verify_consolidation_status("Fase-Invalida")