import logging

from tasks.domain.task import Task


class TaskService:

    def __init__(self, repository):
        self.repository = repository

    def get_task(self, task_id):
        logging.info("finding task with id: {}".format(task_id))
        task = Task.from_sql_result(self.repository.find_by_id(task_id))
        logging.info("found task with id: {} - Task: {}".format(task_id, task))
        return task

    def get_tasks(self):
        logging.info("finding all tasks")
        tasks = Task.from_sql_results(self.repository.find_all())
        logging.info("found tasks {}".format(len(tasks)))
        tasks = [task.to_json() for task in tasks]
        return tasks

    def create_task(self, task):
        try:
            logging.info("creating new task: `{}`".format(task))
            #task = Task.from_sql_result(task)
            self.repository.insert(task)
        except Exception as e:
            logging.error(e)
            return {"error": str(e)}
        return {"message": "Task created successfully"}

    def update_task(self, task_id, task):
        try:
            logging.info("updating task: id  {}, {}".format(task_id, task))
            self.repository.update(task_id,task)
        except Exception as e:
            logging.error(e)
            return {"error": str(e)}
        return {"message": "Task updating successfully"}


    def delete_task(self, task_id):
        try:
            logging.info("deleting task id  {}".format(task_id,))
            self.repository.delete(task_id)
        except Exception as e:
            logging.error(e)
            return {"error": str(e)}
        return {"message": "Task deleting successfully"}