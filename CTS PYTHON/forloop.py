def print_numbers(count):
    if count <= 0:
        print("Invalid loop count")
        return

    for i in range(5):
        print(i + 1)

count = 5

print_numbers(count)