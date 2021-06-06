# 100 Days of Code
# DAY 010
# Created by eduardorabe
# Calculator

from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number? "))
    continue_calculating = "y"
    while continue_calculating.lower() == "y":
        for symbol in operations:
            print(symbol)
        operation_symbol = str(input("Pick an operation from above: "))
        num2 = float(input("What's the next number? "))
        calculation_function = operations[operation_symbol]
        res = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {res}")
        continue_calculating = input(
            f"Type 'y' to continue calculating with {res}, or type 'n' to start a new calculation: ")
        if continue_calculating == "y":
            num1 = res
        elif continue_calculating == "n":
            calculator()


calculator()
