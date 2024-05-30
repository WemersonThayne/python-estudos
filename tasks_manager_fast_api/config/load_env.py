from dotenv import load_dotenv
import os

load_dotenv()

_db_config = {
    'db_name': os.getenv('DATABASE_NAME'),
    'db_user': os.getenv('DATABASE_USER'),
    'db_password': os.getenv('DATABASE_PASSWORD'),
    'db_host': os.getenv('DATABASE_HOST'),
    'db_port': os.getenv('DATABASE_PORT'),
    'db_drive_name': os.getenv('DATABASE_DRIVE_NAME'),
}


def get_db_config(): return _db_config
