class Task:
    def __init__(self, id, title, description, status):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    def to_string(self) -> str:
        return f"Id: {self.id}, Title: {self.title}, Description: {self.description}, Status: {self.status}"
