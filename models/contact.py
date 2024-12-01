import json

class Contact:
    def __init__(self, id, name, phone, email):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
        }

    @staticmethod
    def from_dict(data):
        return Contact(
            id=data["id"],
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
        )

    @staticmethod
    def load_contacts(file_path="data/contacts.json"):
        try:
            with open(file_path, "r") as file:
                return [Contact.from_dict(contact) for contact in json.load(file)]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_contacts(contacts, file_path="data/contacts.json"):
        with open(file_path, "w") as file:
            json.dump([contact.to_dict() for contact in contacts], file, ensure_ascii=False, indent=4)