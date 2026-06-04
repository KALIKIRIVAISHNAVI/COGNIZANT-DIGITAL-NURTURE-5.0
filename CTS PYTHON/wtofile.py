def write_greeting():
    with open("greeting.txt", "w") as file:
        file.write("Hello World")

    print("Message written to file successfully")

write_greeting()