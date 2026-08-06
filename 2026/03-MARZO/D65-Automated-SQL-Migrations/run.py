from pathlib import Path
import logging
from alembic.config import Config
from alembic import command

# Configuración de logging estructurado
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
)
logger = logging.getLogger(__name__)

def run_migrations() -> None:
    """Ejecuta las migraciones de Alembic de forma automatizada."""
    try:
        logger.info("Iniciando la ejecución de migraciones con Alembic...")
        
        # 1. Definir la ruta base del día actual y la ubicación del alembic.ini
        base_dir = Path(__file__).resolve().parent
        alembic_ini_path = base_dir / "alembic.ini"
        
        if not alembic_ini_path.exists():
            raise FileNotFoundError(f"No se encontró el fichero de configuración en: {alembic_ini_path}")

        # 2. Cargar la configuración de Alembic apuntando al archivo ini
        alembic_cfg = Config(str(alembic_ini_path))
        
        # Opcional (por seguridad): Forzar la ruta del script_location si es relativa
        script_location = base_dir / "alembic"  # Asumiendo que tu carpeta se llama 'alembic'
        alembic_cfg.set_main_option("script_location", str(script_location))

        # 3. Ejecutar la actualización hacia la última revisión ("head")
        command.upgrade(alembic_cfg, "head")
        
        logger.info("Migraciones ejecutadas exitosamente.")

    except Exception as e:
        logger.error(f"Error crítico durante la ejecución de migraciones: {e}")
        raise

if __name__ == "__main__":
    run_migrations()