from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy import create_engine
from alembic import context

# Importamos o Base e os modelos para que Alembic conheça os metadados
from models.base import Base
from models import user, task  # Importando os modelos

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(context.config.config_file_name)

# Este objeto é usado para configurações de migração 'offline'
config = context.config

# Adicione aqui os modelos das tabelas
# Para que o Alembic reconheça e gere as migrações adequadas
target_metadata = Base.metadata

# Configurações adicionais que podem ser necessárias
config.set_main_option('sqlalchemy.url', 'postgresql://postgres:postgres@localhost:5432/task_manager')

def run_migrations_offline():
    """
    Run migrations in 'offline' mode.

    Neste modo, a configuração do contexto é feita apenas com uma URL.
    Sem necessidade de criar um 'Engine' ou conexão com o banco de dados.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"}
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """
    Run migrations in 'online' mode.

    Neste modo, criamos um 'Engine' e associamos uma conexão com o contexto.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
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

# Verifica se estamos em modo offline ou online e executa a função correspondente
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

