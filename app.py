from flask import Flask, render_template, request
import math

app = Flask(__name__)


def calculate_circle_area(radius):
    """Функция для расчета площади круга"""
    return math.pi * radius ** 2


@app.route("/", methods=["GET", "POST"])
def index():
    area = None
    if request.method == "POST":
        try:
            radius = float(request.form["radius"])
            if radius < 0:
                area = "Радиус не может быть отрицательным!"
            else:
                area = f"Площадь круга с радиусом {radius} равна: {calculate_circle_area(radius):.2f}"
        except ValueError:
            area = "Пожалуйста, введите числовое значение для радиуса."

    return render_template("index.html", area=area)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)