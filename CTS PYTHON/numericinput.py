def get_age():
    age = input("Enter your age: ")

    if not age.isdigit():
        print("Invalid age")
        return

    age = int(age)
    print(f"Next year you'll be {age + 1}")

get_age()