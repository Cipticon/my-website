import math

def calculate_circle_area(radius):
    """Функция для расчета площади круга"""
    return math.pi * radius ** 2

def main():
    print("Добро пожаловать в программу для расчета площади круга!")
    try:
        radius = float(input("Введите радиус круга: "))
        if radius < 0:
            print("Радиус не может быть отрицательным!")
        else:
            area = calculate_circle_area(radius)
            print(f"Площадь круга с радиусом {radius} равна: {area:.2f}")
    except ValueError:
        print("Пожалуйста, введите числовое значение для радиуса.")

if __name__ == "__main__":
    main()