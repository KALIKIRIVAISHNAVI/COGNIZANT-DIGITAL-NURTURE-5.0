def greet_user():
    name = input("Enter your name: ")

    if name.strip() == "":
        print("Name cannot be empty")
        return

    print(f"Hello, {name}!")

greet_user()