def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Invalid input")
        return None

    return a + b

result = add(5, 3)

if result is not None:
    print(f"Sum: {result}")