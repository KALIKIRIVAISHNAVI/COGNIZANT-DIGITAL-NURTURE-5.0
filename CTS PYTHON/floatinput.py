def convert_weight():
    weight = input("Enter weight in kilograms: ")

    try:
        kg = float(weight)

        if kg <= 0:
            print("Invalid weight")
            return

        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs:.2f}")

    except ValueError:
        print("Invalid input. Please enter a decimal number.")

convert_weight()