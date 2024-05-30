from abc import ABC, abstractmethod


class TaskRepository(ABC):

    @abstractmethod
    def find_by_id(self):
        pass

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass

    @abstractmethod
    def find_by_name(self, name):
        pass

    @abstractmethod
    def find_by_category(self, category):
        pass

    @abstractmethod
    def find_by_user(self, user):
        pass

    @abstractmethod
    def find_by_args(self, args):
        pass