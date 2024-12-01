class Calculator:
    @staticmethod
    def calculate(expression):
        try:
            return eval(expression)
        except ZeroDivisionError:
            return "Ошибка: деление на ноль"
        except Exception:
            return "Ошибка: некорректное выражение"
