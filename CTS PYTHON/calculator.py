def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError
        return a / b
    else:
        return "Invalid operator"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Error: Invalid number input")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")