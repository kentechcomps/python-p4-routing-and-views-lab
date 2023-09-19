#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:name>')
def print_string(name):
    print(name)
    return f'<h1>{name}</h1>'

@app.route('/count/<int:param>')
def count(param):

    numbers = '\n'.join(str(i)for i in range(1 , param +1))

    return f'<pre>{numbers}</pre>'

@app.route('/math/<float:num1><operation><float:num2>')
def math (num1 ,operation , num2):
    result = None
    if operation =='+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
           result = num1/num2
        else:
            return 'Error: Division by zero'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Error : INvalid operation'
    
    return f'<h1>{num1} {operation} {num2} = {result}</h1>'