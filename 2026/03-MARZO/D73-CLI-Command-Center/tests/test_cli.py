from typer.testing import CliRunner
from src.cli import app

runner = CliRunner()

def test_run_pipeline_command():
    """Valida la ejecución estándar del comando principal del CLI."""
    result = runner.invoke(app, ["--name", "test-pipe"])
    assert result.exit_code == 0
    assert "Iniciando pipeline: test-pipe" in result.stdout
    assert "Pipeline 'test-pipe' ejecutado exitosamente." in result.stdout

def test_run_pipeline_dry_run():
    """Valida la ejecución del pipeline con la opción de simulación (dry-run)."""
    result = runner.invoke(app, ["--name", "test-pipe", "--dry-run"])
    assert result.exit_code == 0
    assert "Modo simulación (dry-run) activado" in result.stdout