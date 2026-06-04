def area(length, width):
    if length <= 0 or width <= 0:
        print("Invalid dimensions")
        return None

    return length * width

result = area(5, 3)

if result is not None:
    print(f"Area: {result}")