def display_coordinates(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid coordinates")
        return

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

# Multiple assignment
x, y = 10, 20

display_coordinates(x, y)