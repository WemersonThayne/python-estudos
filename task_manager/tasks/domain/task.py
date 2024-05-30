import datetime


class Task:
    def __init__(self):
        pass

    def __init__(self, id, title, description, status, date_end, priority, category, user, created_at, updated_at):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.date_end = date_end
        self.priority = priority
        self.category = category
        self.user = user
        self.created_at = created_at
        self.updated_at = updated_at

    def __str__(self):
        return (f'{self.id}: {self.title}, {self.description}, {self.status}, {self.date_end}, {self.priority},'
                f' {self.category}, {self.user}')


    @staticmethod
    def _to_dict(row):
        id = row[0]
        title = row[1]
        description = row[2]
        status = row[3]
        date_end = row[4]
        priority = row[5]
        category = row[6]
        user = row[7]
        created_at = row[8]
        updated_at = row[9]

        # TODO colocar esses método em uma classe utilitária
        if date_end is not None and isinstance(date_end, str):
            date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d").date()
        if created_at is not None and isinstance(created_at, str):
            created_at = datetime.datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        if updated_at is not None and isinstance(updated_at, str):
            updated_at = datetime.datetime.strptime(updated_at, "%Y-%m-%d %H:%M:%S")

        return Task(id, title, description, status, date_end, priority, category, user, created_at, updated_at)

    @staticmethod
    def from_sql_result(result):
        for row in result:
            return Task._to_dict(row)

    @staticmethod
    def from_sql_results(results):
        tasks = []
        for row in results:
            tasks.append(Task._to_dict(row))
        return tasks


    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'date_end': str(self.date_end),
            'priority': self.priority,
            'category': self.category,
            'user': self.user,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }

