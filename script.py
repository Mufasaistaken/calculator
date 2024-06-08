from flask import Flask, render_template, request # type: ignore

app = Flask(__name__)

class Calculator:
    def add(self, a, b):
        return a + b
    
    def sub(self, a, b):
        return a - b
    
    def mult(self, a, b):
        return a * b
    
    def div(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Can't devide by zero IDIOT"
        

calc = Calculator()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']


    if operation == 'add':
        result = calc.add(num1, num2)
    elif operation == 'sub':
        result = calc.sub(num1, num2)
    elif operation == 'mult':
        result = calc.mult(num1, num2)
    elif operation == 'div':
        result = calc.div(num1, num2)
    else:
        result = "Invalid Operation"
    
    return render_template('index.html', result=result)

if __name__ == "__main__":
    app.run(debug = True)


