gitHub = "https://github.com/your_username/your_repository"

def get_number(prompt):
    """Функция безопасного ввода числа."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: Введите корректное число.")


def get_operation():
    """Функция выбора операции."""
    while True:
        operation = input("Выберите операцию (+, -, *, /): ").strip()
        if operation in ["+", "-", "*", "/"]:
            return operation
        print("Ошибка: Выберите одну из операций (+, -, *, /).")


def calculate(num1, num2, operation):
    """Выполнение вычисления."""
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        if num2 == 0:
            return None
        return num1 / num2


def main():
    history = []

    while True:
        num1 = get_number("Введите первое число: ")
        operation = get_operation()
        num2 = get_number("Введите второе число: ")

        result = calculate(num1, num2, operation)

        if result is None:
            print("Ошибка: Деление на ноль.")
        else:
            print(f"Результат: {result}")
            history.append(f"{num1} {operation} {num2} = {result}")

        while True:
            choice = input("Хотите продолжить? (да/нет): ").strip().lower()
            if choice in ["да", "нет"]:
                break
            print("Ошибка: Введите 'да' или 'нет'.")

        if choice == "нет":
            break

    print("\nИстория вычислений:")
    for record in history:
        print(record)


if __name__ == "__main__":
    main()