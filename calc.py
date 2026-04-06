gitHub = "https://github.com/fleay1337/calculator"

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


def calculate(x, y, operation):
    """Выполнение вычисления."""
    if operation == "+":
        return x + y
    if operation == "-":
        return x - y
    if operation == "*":
        return x * y
    if operation == "/":
        if y == 0:
            return None
        return x / y


def main():
    history = []

    while True:
        x = get_number("Введите первое число: ")
        operation = get_operation()
        y = get_number("Введите второе число: ")

        result = calculate(x, y, operation)

        if result is None:
            print("Ошибка: Деление на ноль.")
        else:
            print(f"Результат: {result}")
            history.append(f"{x} {operation} {y} = {result}")

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