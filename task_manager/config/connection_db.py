import psycopg2
import config.load_env as env
import utils.db_util as db_util
import logging as log


def singleton(cls):
    instances = {}

    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return get_instance


@singleton
class ConnectionDb:

    def __init__(self):
        self.connection = None
        self.cursor = None
        self._initialize_connection()


    def _initialize_connection(self):
        environment = env.get_db_config()
        if self.connection is None:
            try:
                self.connection = psycopg2.connect(
                    host=environment['db_host'],
                    user=environment['db_user'],
                    password=environment['db_password'],
                    database=environment['db_name'],
                    port=environment['db_port'],
                )
                self.cursor = self.connection.cursor()

            except Exception as error:
                log.error("Error: Connection not established {}".format(error))
            else:
                log.info("Connection established")

            self._init_creating_tables()
    def get_cursor(self):
        return self.cursor

    def get_connection(self):
        return self.connection


    def close(self):
        if self.connection is not None:
            self.connection.close()
            log.info("Connection closed")

    #FIXME temporario
    def _init_creating_tables(self):

        sql_create_task_table = """
                CREATE TABLE IF NOT EXISTS task (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(255),
                    description TEXT,
                    status VARCHAR(50),
                    date_end DATE,
                    priority INT,
                    category_id INT,
                    user_id INT,
                    created_at TIMESTAMP,
                    updated_at TIMESTAMP
                    )"""

        db_util.create_table(sql_create_task_table, self.connection, self.cursor)
        log.info("Created Task Table")

# if __name__ == "__main__":
#     connection_db = ConnectionDb()
#     connection = connection_db.connection
#     cursor = connection_db.get_cursor()
#
#     sql = """CREATE TABLE IF NOT EXISTS test_table
#                       (id SERIAL PRIMARY KEY, name VARCHAR(255), age INT)"""
#
#     db_util.create_table(sql, connection, cursor)
#
#     # db_util.insert_table("INSERT INTO test_table (name, age) VALUES (%s, %s)",('Alice teste', 35), connection, cursor)
#
#     id = 1
#     query_by_id = "SELECT id,name FROM test_table where id = %s"
#     rows = db_util.select_datas(query_by_id,(id,),  cursor)
#     print(rows)
#
#     rows = db_util.select_datas("SELECT * FROM test_table",None, cursor)
#
#     # Iterar sobre os resultados
#     for row in rows:
#         # Cada linha é uma tupla onde cada elemento corresponde a uma coluna
#         id, name, age = row
#         print(f"ID: {id}, Nome: {name}, Idade: {age}")
#
#     id = 5
#     name = "Wemerson"
#     age = 28
#
#     update_sql = "UPDATE test_table SET name = %s, age = %s WHERE id = %s"
#     db_util.update_data(update_sql, (name, age, id), connection, cursor)
#
#     query_by_id = "SELECT id,name FROM test_table where id = %s"
#     rows = db_util.select_datas(query_by_id, (id,), cursor)
#     print(rows)
#
#     # Fechar a conexão
#     connection_db.close()

  #FIXME: validar em outro momento
  # def _initialize_db(self):
  #       environment = env.get_db_config()
  #       try:
  #           with psycopg2.connect(
  #                   host=environment['db_host'],
  #                   user=environment['db_user'],
  #                   password=environment['db_password'],
  #                   port=environment['db_port'],
  #           ) as conn:
  #               conn.autocommit = True
  #               conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
  #
  #               with conn.cursor() as cur:
  #                   sql_query_exist_db = f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{environment['db_name']}'"
  #                   cur.execute(sql_query_exist_db)
  #                   exists = cur.fetchone()
  #                   if not exists:
  #                       cur.execute(f'CREATE DATABASE "{environment["db_name"]}"')
  #       except Exception as error:
  #           print("Error: Could not create database: {}".format(error))
  #           return
  #
  #       self._initialize_connection()
