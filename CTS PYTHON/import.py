from math import *

def math_operations(number):
    if number < 0:
        print("Invalid input")
        return

    print(f"Square Root: {sqrt(number):.2f}")
    print(f"Power (number²): {pow(number, 2):.2f}")
    print(f"Value of Pi: {pi:.2f}")

number = 16

math_operations(number)