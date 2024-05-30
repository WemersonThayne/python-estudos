from config.connection_db import ConnectionDb as connectionDb
from tasks.repository.task_repository import TaskRepository
from utils import db_util as db_util


class TaskRepositoryImpl(TaskRepository):

    def __init__(self):
        db = connectionDb()
        self.cursor = db.get_cursor()
        self.connection = db.get_connection()

    def find_by_id(self, id):
        sql = "SELECT * FROM task WHERE id = %s"
        return db_util.select_datas(sql, (id,), self.cursor)

    def find_all(self):
        sql = "SELECT * FROM task"
        return db_util.select_datas(sql, None, self.cursor)

    def insert(self, task):
        sql = ("INSERT INTO task (id, title, description, status, date_end, priority, created_at, updated_at) "
               "VALUES (DEFAULT, %s,%s,%s,%s,%s,%s,%s)")
        return db_util.insert_table(sql,
                                    (task['title'], task['description'], task['status'], task['date_end'],
                                     task['priority'], task['created_at'], task['updated_at']),
                                    self.connection, self.cursor)

    def update(self, id, task):
        sql = "UPDATE task SET title = %s, description = %s WHERE id = %s"
        return  db_util.update_data(sql, (task['title'], task['description'], id), self.connection, self.cursor)


    def delete(self, id):
        sql =  "DELETE FROM task WHERE id = %s"
        return db_util.update_data(sql, (id,), self.connection, self.cursor)

    def find_by_name(self, name):
        pass

    def find_by_category(self, category):
        pass

    def find_by_user(self, user):
        pass

    def find_by_args(self, args):
        pass
