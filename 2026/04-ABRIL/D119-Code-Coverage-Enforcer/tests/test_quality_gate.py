import pytest
from src.quality_gate import QualityGateEnforcer

def test_quality_gate_success(monkeypatch):
    """Simula una ejecución de coverage exitosa que cumple con el umbral."""
    enforcer = QualityGateEnforcer(min_coverage_percentage=80.0)

    class MockCompletedProcess:
        returncode = 0
        stdout = "TOTAL 50 0 100%"
        stderr = ""

    def mock_run(cmd, capture_output, text):
        return MockCompletedProcess()

    monkeypatch.setattr("subprocess.run", mock_run)

    passed, message = enforcer.check_coverage()
    assert passed is True
    assert "100%" in message

def test_quality_gate_failure(monkeypatch):
    """Simula una ejecución donde la cobertura cae por debajo del umbral."""
    enforcer = QualityGateEnforcer(min_coverage_percentage=100.0)

    class MockCompletedProcess:
        returncode = 1
        stdout = ""
        stderr = "FAIL: Required coverage of 100% not reached: 85%"

    def mock_run(cmd, capture_output, text):
        return MockCompletedProcess()

    monkeypatch.setattr("subprocess.run", mock_run)

    passed, message = enforcer.check_coverage()
    assert passed is False
    assert "FAIL" in message