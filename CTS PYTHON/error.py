def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

divide_numbers(10, 2)