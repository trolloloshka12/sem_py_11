import json
from datetime import datetime

class Task:
    def __init__(self, id, title, description, done=False, priority="Средний", due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date or datetime.now().strftime('%d-%m-%Y')

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "priority": self.priority,
            "due_date": self.due_date,
        }

    @staticmethod
    def from_dict(data):
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            done=data["done"],
            priority=data["priority"],
            due_date=data["due_date"],
        )

    @staticmethod
    def load_tasks(file_path="data/tasks.json"):
        try:
            with open(file_path, "r") as file:
                return [Task.from_dict(task) for task in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_tasks(tasks, file_path="data/tasks.json"):
        with open(file_path, "w") as file:
            json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
