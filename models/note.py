import json
import csv
from datetime import datetime

class Note:
    def __init__(self, id, title, content, timestamp=None):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = timestamp or datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "timestamp": self.timestamp,
        }

    @staticmethod
    def from_dict(data):
        return Note(
            id=data["id"],
            title=data["title"],
            content=data["content"],
            timestamp=data["timestamp"],
        )

    @staticmethod
    def load_notes(file_path="data/notes.json"):
        try:
            with open(file_path, "r") as file:
                return [Note.from_dict(note) for note in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_notes(notes, file_path="data/notes.json"):
        with open(file_path, "w") as file:
            json.dump([note.to_dict() for note in notes], file, ensure_ascii=False, indent=4)

    @staticmethod
    def export_to_csv(notes, file_path="data/notes.csv"):
        with open(file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Content", "Timestamp"])
            for note in notes:
                writer.writerow([note.id, note.title, note.content, note.timestamp])
        print(f"Заметки экспортированы в {file_path}")

    @staticmethod
    def import_from_csv(file_path="data/notes.csv"):
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [
                    Note(
                        id=int(row["ID"]),
                        title=row["Title"],
                        content=row["Content"],
                        timestamp=row["Timestamp"],
                    )
                    for row in reader
                ]
        except FileNotFoundError:
            print("Файл для импорта не найден.")
            return []
