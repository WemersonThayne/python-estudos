from tasks.repository.task_repository_impl import TaskRepositoryImpl
from tasks.service.task_service import TaskService


class TaskController:

    def __init__(self):
        self.task_service = TaskService(TaskRepositoryImpl())

    def get_task(self, task_id):
        return self.task_service.get_task(task_id).to_json()

    def get_tasks(self):
        return self.task_service.get_tasks()

    def create_task(self, task):
        return self.task_service.create_task(task)

    def update_task(self, task_id, task):
        return  self.task_service.update_task(task_id, task)


    def delete_task(self, task_id):
        return self.task_service.delete_task(task_id)