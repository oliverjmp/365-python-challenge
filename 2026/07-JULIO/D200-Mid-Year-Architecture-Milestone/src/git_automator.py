import git
import os

class GitMilestoneManager:
    """Gestor automatizado para etiquetado y auditoría de hitos de arquitectura en Git."""

    def __init__(self, repo_path: str = "."):
        self.repo_path = repo_path
        try:
            self.repo = git.Repo(repo_path, search_parent_directories=True)
        except git.exc.InvalidGitRepositoryError:
            raise ValueError(f"La ruta '{repo_path}' no es un repositorio Git válido.")

    def obtener_estado_actual(self) -> dict:
        """Devuelve un diccionario con el estado actual del repositorio (rama, commits, tags)."""
        return {
            "branch_activa": self.repo.active_branch.name,
            "commit_reciente": self.repo.head.commit.hexsha[:7],
            "mensaje_commit": self.repo.head.commit.message.strip(),
            "tags_existentes": [tag.name for tag in self.repo.tags]
        }

    def crear_tag_hito(self, nombre_tag: str, mensaje: str) -> str:
        """Crea un tag anotado para marcar un hito de arquitectura en el repositorio."""
        if nombre_tag in [tag.name for tag in self.repo.tags]:
            raise ValueError(f"El tag '{nombre_tag}' ya existe en el repositorio.")
        
        nuevo_tag = self.repo.create_tag(nombre_tag, message=mensaje)
        return f"Tag '{nuevo_tag.name}' creado exitosamente en el commit {self.repo.head.commit.hexsha[:7]}."