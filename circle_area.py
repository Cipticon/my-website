import random


def generate_random_number(start, end):
    """Функция для генерации случайного числа"""
    return random.randint(start, end)


def main():
    try:
        start = int(input("Введите начальное значение диапазона: "))
        end = int(input("Введите конечное значение диапазона: "))

        if start >= end:
            print("Начальное число должно быть меньше конечного!")
        else:
            random_number = generate_random_number(start, end)
            print(f"Случайное число между {start} и {end}: {random_number}")
    except ValueError:
        print("Пожалуйста, введите числовые значения для диапазона.")


if __name__ == "__main__":
    main()