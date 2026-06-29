def display_coordinates(coords):
    if len(coords) != 2:
        print("Invalid coordinates")
        return

    x, y = coords

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid coordinate values")
        return

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

coordinates = (10, 20)

display_coordinates(coordinates)