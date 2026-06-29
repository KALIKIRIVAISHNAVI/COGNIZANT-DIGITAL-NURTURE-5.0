import math

def calculate_area(radius):
    if radius <= 0:
        print("Invalid radius")
        return

    area = math.pi * radius ** 2
    print(f"Area of Circle: {area:.2f}")

radius = 5

calculate_area(radius)