import sys
from pathlib import Path
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# 1. Configurar la ruta raíz del proyecto de forma dinámica (Sube 2 niveles hasta la raíz de D65)
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# 2. Importar la URL de conexión y los modelos del núcleo de datos
from database import DATABASE_URL  # Asegura la importación limpia de la URL de conexión
from models import Base            # Importa la Base declarativa para registrar la metadata

# Objeto de configuración de Alembic
config = context.config

# 3. Inyección explícitamente programática de la URL para evitar el KeyError en alembic.ini
# NOTA: Este override tiene prioridad sobre el valor de alembic.ini.
# database.py (DATABASE_URL) es la única fuente de verdad de la conexión;
# el valor en alembic.ini se mantiene sincronizado solo por legibilidad.
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configuración de logs corporativos
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata objetivo para autogeneración de migraciones de esquemas
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    config_section = config.get_section(config.config_ini_section, {})
    
    connectable = engine_from_config(
        config_section,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, 
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()