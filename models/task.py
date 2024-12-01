import json
import csv

class Task:
    def __init__(self, id, title, description, done=False, priority="Средний", due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

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

    @staticmethod
    def export_to_csv(tasks, file_path="data/tasks.csv"):
        with open(file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Description", "Done", "Priority", "DueDate"])
            for task in tasks:
                writer.writerow([task.id, task.title, task.description, task.done, task.priority, task.due_date])
        print(f"Задачи экспортированы в {file_path}")

    @staticmethod
    def import_from_csv(file_path="data/tasks.csv"):
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [
                    Task(
                        id=int(row["ID"]),
                        title=row["Title"],
                        description=row["Description"],
                        done=row["Done"].lower() == "true",
                        priority=row["Priority"],
                        due_date=row["DueDate"],
                    )
                    for row in reader
                ]
        except FileNotFoundError:
            print("Файл для импорта не найден.")
            return []
