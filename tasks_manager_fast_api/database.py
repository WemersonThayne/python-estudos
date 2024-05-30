from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models import user, task

import config.load_env as env

environment = env.get_db_config()
#
# url = URL.create(
#     drivername=environment['db_drive_name'],
#     username=environment['db_user'],
#     password=environment['db_password'],
#     host=environment['db_host'],
#     database=environment['db_name'],
#     port=environment['db_port']
# )

SQLALCHEMY_DATABASE_URL = f"{environment['db_drive_name']}://{environment['db_user']}:{environment['db_password']}@{environment['db_host']}:{environment['db_port']}/{environment['db_name']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    Base.metadata.create_all(bind=engine)
