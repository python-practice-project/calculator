#calculator
from art import calculator_logo
import os
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
print(calculator_logo)
def calculator():
    #print(calculator_logo)
    num1 = float(input("What's the first number: "))
    for symbol in operations:
        print(symbol)

    calculation_stop = True
    while calculation_stop:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's next number: "))
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        another_cal = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
        if another_cal == 'y':
            num1 = answer
        else:
            calculation_stop = False
            os.system('cls')
            calculator()
calculator()