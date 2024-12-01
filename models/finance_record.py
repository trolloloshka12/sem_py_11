import json
import csv

class FinanceRecord:
    def __init__(self, id, amount, category, date, description):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount,
            "category": self.category,
            "date": self.date,
            "description": self.description,
        }

    @staticmethod
    def from_dict(data):
        return FinanceRecord(
            id=data["id"],
            amount=data["amount"],
            category=data["category"],
            date=data["date"],
            description=data["description"],
        )

    @staticmethod
    def load_records(file_path="data/finance.json"):
        try:
            with open(file_path, "r") as file:
                return [FinanceRecord.from_dict(record) for record in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_records(records, file_path="data/finance.json"):
        with open(file_path, "w") as file:
            json.dump([record.to_dict() for record in records], file, ensure_ascii=False, indent=4)

    @staticmethod
    def export_to_csv(records, file_path="data/finance_records.csv"):
        with open(file_path, mode="w", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
            for record in records:
                writer.writerow([record.id, record.amount, record.category, record.date, record.description])
        print(f"Финансовые записи экспортированы в {file_path}")

    @staticmethod
    def import_from_csv(file_path="data/finance_records.csv"):
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                return [
                    FinanceRecord(
                        id=int(row["ID"]),
                        amount=float(row["Amount"]),
                        category=row["Category"],
                        date=row["Date"],
                        description=row["Description"],
                    )
                    for row in reader
                ]
        except FileNotFoundError:
            print("Файл для импорта не найден.")
            return []
