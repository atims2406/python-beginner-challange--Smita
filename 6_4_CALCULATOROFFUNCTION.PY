def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
operation = input("Enter +, -, * or /: ")

if operation == "+":
    print("Answer:", add(a, b))
elif operation == "-":
    print("Answer:", subtract(a, b))
elif operation == "*":
    print("Answer:", multiply(a, b))
elif operation == "/":
    print("Answer:", divide(a, b))
else:
    print("Wrong operation")