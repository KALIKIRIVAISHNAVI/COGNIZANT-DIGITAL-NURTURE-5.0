def read_file():
    try:
        with open("greeting.txt", "r") as file:
            content = file.read()
            print("File Content:")
            print(content)

    except FileNotFoundError:
        print("File not found")

read_file()