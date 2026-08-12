from src.cli import status, deploy

def test_status_command():
    status()
    assert True

def test_deploy_command():
    deploy(environment="staging")
    assert True