from models.note import Note
from models.task import Task
from models.contact import Contact
from models.finance_record import FinanceRecord
from utils.calculator import Calculator

def main_menu():
    print("Добро пожаловать в Персональный помощник!")
    while True:
        print("\nВыберите действие:")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансовыми записями")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Введите номер действия: ")
        if choice == '1':
            manage_notes()
        elif choice == '2':
            manage_tasks()
        elif choice == '3':
            manage_contacts()
        elif choice == '4':
            manage_finances()
        elif choice == '5':
            use_calculator()
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Управление заметками
def manage_notes():
    notes = Note.load_notes()

    while True:
        print("\nУправление заметками:")
        print("1. Просмотреть все заметки")
        print("2. Прочитать заметку по ID")
        print("3. Создать заметку")
        print("4. Редактировать заметку")
        print("5. Удалить заметку")
        print("6. Экспорт заметок в CSV")
        print("7. Импорт заметок из CSV")
        print("8. Назад")

        choice = input("Введите номер действия: ")
        if choice == '1':
            if not notes:
                print("Заметок пока нет.")
            else:
                for note in notes:
                    print(f"ID: {note.id}, Заголовок: {note.title}, Дата: {note.timestamp}")
        elif choice == '2':
            try:
                note_id = int(input("Введите ID заметки: "))
                note = next((n for n in notes if n.id == note_id), None)
                if note:
                    print(f"\nЗаголовок: {note.title}")
                    print(f"Содержимое: {note.content}")
                    print(f"Дата: {note.timestamp}")
                else:
                    print("Заметка с таким ID не найдена.")
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '3':
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержимое заметки: ")
            new_note = Note(id=len(notes) + 1, title=title, content=content)
            notes.append(new_note)
            Note.save_notes(notes)
            print("Заметка успешно создана!")
        elif choice == '4':
            try:
                note_id = int(input("Введите ID заметки для редактирования: "))
                note = next((n for n in notes if n.id == note_id), None)
                if note:
                    note.title = input(f"Введите новый заголовок (текущий: {note.title}): ") or note.title
                    note.content = input(f"Введите новое содержимое (текущее: {note.content}): ") or note.content
                    Note.save_notes(notes)
                    print("Заметка успешно обновлена!")
                else:
                    print("Заметка с таким ID не найдена.")
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '5':
            try:
                note_id = int(input("Введите ID заметки для удаления: "))
                notes = [n for n in notes if n.id != note_id]
                Note.save_notes(notes)
                print("Заметка успешно удалена!")
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '6':
            Note.export_to_csv(notes)
        elif choice == '7':
            imported_notes = Note.import_from_csv()
            notes.extend(imported_notes)
            Note.save_notes(notes)
            print("Заметки успешно импортированы!")
        elif choice == '8':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Управление задачами
def manage_tasks():
    tasks = Task.load_tasks()

    while True:
        print("\nУправление задачами:")
        print("1. Просмотреть все задачи")
        print("2. Создать задачу")
        print("3. Отметить задачу как выполненную")
        print("4. Фильтровать задачи")
        print("5. Назад")

        choice = input("Введите номер действия: ")
        if choice == '1':
            if not tasks:
                print("Задач пока нет.")
            else:
                for task in tasks:
                    status = "Выполнено" if task.done else "Не выполнено"
                    print(f"ID: {task.id}, Заголовок: {task.title}, Статус: {status}, Приоритет: {task.priority}, Срок: {task.due_date}")
        elif choice == '2':
            title = input("Введите заголовок задачи: ")
            description = input("Введите описание задачи: ")
            priority = input("Введите приоритет (Высокий, Средний, Низкий): ")
            due_date = input("Введите срок выполнения (ДД-ММ-ГГГГ): ")
            new_task = Task(
                id=len(tasks) + 1,
                title=title,
                description=description,
                priority=priority,
                due_date=due_date
            )
            tasks.append(new_task)
            Task.save_tasks(tasks)
            print("Задача успешно создана!")
        elif choice == '3':
            try:
                task_id = int(input("Введите ID задачи для отметки как выполненной: "))
                task = next((t for t in tasks if t.id == task_id), None)
                if task:
                    task.done = True
                    Task.save_tasks(tasks)
                    print("Задача успешно отмечена как выполненная!")
                else:
                    print("Задача с таким ID не найдена.")
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '4':  # Фильтрация задач
            print("\nФильтрация задач:")
            print("1. По статусу")
            print("2. По приоритету")
            filter_choice = input("Выберите тип фильтрации: ")
            if filter_choice == '1':
                status = input("Введите статус (выполнено/не выполнено): ").lower()
                filtered_tasks = [
                    task for task in tasks if
                    (status == "выполнено" and task.done) or (status == "не выполнено" and not task.done)
                ]
                for task in filtered_tasks:
                    print(f"ID: {task.id}, Заголовок: {task.title}, Статус: {'Выполнено' if task.done else 'Не выполнено'}")
            elif filter_choice == '2':
                priority = input("Введите приоритет (Высокий, Средний, Низкий): ").capitalize()
                filtered_tasks = [task for task in tasks if task.priority == priority]
                for task in filtered_tasks:
                    print(f"ID: {task.id}, Заголовок: {task.title}, Приоритет: {task.priority}")
            else:
                print("Некорректный выбор.")
        elif choice == '5':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Управление контактами
def manage_contacts():
    contacts = Contact.load_contacts()

    while True:
        print("\nУправление контактами:")
        print("1. Просмотреть все контакты")
        print("2. Добавить новый контакт")
        print("3. Удалить контакт")
        print("4. Назад")

        choice = input("Введите номер действия: ")
        if choice == '1':
            if not contacts:
                print("Контактов пока нет.")
            else:
                for contact in contacts:
                    print(f"ID: {contact.id}, Имя: {contact.name}, Телефон: {contact.phone}, Email: {contact.email}")
        elif choice == '2':
            name = input("Введите имя контакта: ")
            phone = input("Введите номер телефона: ")
            email = input("Введите адрес электронной почты: ")
            new_contact = Contact(id=len(contacts) + 1, name=name, phone=phone, email=email)
            contacts.append(new_contact)
            Contact.save_contacts(contacts)
            print("Контакт успешно добавлен!")
        elif choice == '3':
            try:
                contact_id = int(input("Введите ID контакта для удаления: "))
                contacts = [c for c in contacts if c.id != contact_id]
                Contact.save_contacts(contacts)
                print("Контакт успешно удалён!")
            except ValueError:
                print("ID должен быть числом.")
        elif choice == '4':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Управление финансовыми записями
def manage_finances():
    finances = FinanceRecord.load_records()

    while True:
        print("\nУправление финансовыми записями:")
        print("1. Просмотреть записи")
        print("2. Добавить запись")
        print("3. Сгенерировать отчёт")
        print("4. Назад")

        choice = input("Введите номер действия: ")
        if choice == '1':
            if not finances:
                print("Записей пока нет.")
            else:
                for record in finances:
                    print(f"ID: {record.id}, Сумма: {record.amount}, Категория: {record.category}, Дата: {record.date}, Описание: {record.description}")
        elif choice == '2':
            amount = float(input("Введите сумму (положительная — доход, отрицательная — расход): "))
            category = input("Введите категорию: ")
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            description = input("Введите описание: ")
            new_record = FinanceRecord(id=len(finances) + 1, amount=amount, category=category, date=date, description=description)
            finances.append(new_record)
            FinanceRecord.save_records(finances)
            print("Запись успешно добавлена!")
        elif choice == '3':
            if not finances:
                print("Записей пока нет.")
            else:
                start_date = input("Введите начальную дату (ДД-ММ-ГГГГ) или оставьте пустым: ")
                end_date = input("Введите конечную дату (ДД-ММ-ГГГГ) или оставьте пустым: ")
                filtered_records = finances
                if start_date:
                    filtered_records = [rec for rec in filtered_records if rec.date >= start_date]
                if end_date:
                    filtered_records = [rec for rec in filtered_records if rec.date <= end_date]

                total_income = sum(rec.amount for rec in filtered_records if rec.amount > 0)
                total_expenses = sum(rec.amount for rec in filtered_records if rec.amount < 0)
                balance = total_income + total_expenses

                categories = {}
                for rec in filtered_records:
                    categories[rec.category] = categories.get(rec.category, 0) + rec.amount

                print("\n--- Финансовый отчёт ---")
                print(f"Общий доход: {total_income}")
                print(f"Общие расходы: {abs(total_expenses)}")
                print(f"Баланс: {balance}")
                print("\n--- Категории ---")
                for category, amount in categories.items():
                    print(f"{category}: {amount}")

                report_file = f"data/finance_report.csv"
                with open(report_file, "w", encoding="utf-8") as file:
                    file.write("Категория,Сумма\n")
                    for category, amount in categories.items():
                        file.write(f"{category},{amount}\n")
                print(f"Отчёт сохранён в файл {report_file}")
        elif choice == '4':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

# Калькулятор
def use_calculator():
    while True:
        print("\nКалькулятор:")
        expression = input("Введите выражение (или 'назад' для возврата): ")
        if expression.lower() == 'назад':
            break
        try:
            result = Calculator.calculate(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main_menu()
