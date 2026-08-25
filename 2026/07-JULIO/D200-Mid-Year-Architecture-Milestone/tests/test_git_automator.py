import pytest
import git
from src.git_automator import GitMilestoneManager

def test_repositorio_invalido(tmp_path):
    """Verifica que se lance un error si la ruta no es un repositorio Git."""
    with pytest.raises(ValueError, match="no es un repositorio Git válido"):
        GitMilestoneManager(str(tmp_path))

def test_gestor_git_real(tmp_path):
    """Prueba el flujo completo sobre un repositorio Git temporal real."""
    # Inicializamos un repo temporal de prueba
    repo = git.Repo.init(str(tmp_path))
    
    # Creamos un archivo dummy y hacemos un commit inicial
    dummy_file = tmp_path / "README.md"
    dummy_file.write_text("# Test Repo")
    repo.index.add(["README.md"])
    repo.index.commit("Commit inicial de prueba")

    manager = GitMilestoneManager(str(tmp_path))
    estado = manager.obtener_estado_actual()
    
    assert estado["commit_reciente"] is not None
    assert isinstance(estado["tags_existentes"], list)

    # Probamos la creación de un tag de hito
    resultado = manager.crear_tag_hito("v200-milestone", "Hito de mitad de año alcanzado")
    assert "creado exitosamente" in resultado

    # Intentamos crear el mismo tag duplicado para validar la excepción
    with pytest.raises(ValueError, match="ya existe"):
        manager.crear_tag_hito("v200-milestone", "Intento duplicado")