import json

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
