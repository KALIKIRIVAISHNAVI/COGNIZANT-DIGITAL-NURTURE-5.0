def string_length(text):
    if text.strip() == "":
        print("Invalid string")
        return

    print(f"Length: {len(text)}")

text = "Hello World"

string_length(text)