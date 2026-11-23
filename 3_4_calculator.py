a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
operation = input("Enter +, -, * or /: ")

if operation == "+":
    print("Answer:", a + b)
elif operation == "-":
    print("Answer:", a - b)
elif operation == "*":
    print("Answer:", a * b)
elif operation == "/":
    print("Answer:", a / b)
else:
    print("Wrong operation")