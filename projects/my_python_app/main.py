from flask import Flask
from random import randint

from projects.calculator.calculator import Calculator


app = Flask(__name__)
calc = Calculator()

@app.route('/')
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    result = f"this is result of {num1} + {num2} = {calc.add(num1, num2)}"
    return result, 200

if __name__ == '__main__':
    app.run()
