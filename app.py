import random
from flask import Flask, render_template, request

app = Flask(__name__)

def generate_random_number(start, end):
    """Функция для генерации случайного числа"""
    return random.randint(start, end)

@app.route("/", methods=["GET", "POST"])
def index():
    random_number = None
    if request.method == "POST":
        try:
            start = int(request.form["start"])
            end = int(request.form["end"])
            if start >= end:
                random_number = "Начальное число должно быть меньше конечного!"
            else:
                random_number = generate_random_number(start, end)
        except ValueError:
            random_number = "Пожалуйста, введите числовые значения для диапазона."

    return render_template("index.html", random_number=random_number)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)