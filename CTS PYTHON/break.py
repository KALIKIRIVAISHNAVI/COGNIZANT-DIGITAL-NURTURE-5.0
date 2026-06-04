def find_first_even(range_size):
    if range_size <= 0:
        print("Invalid range size")
        return

    for i in range(1, range_size + 1):
        if i % 2 == 0:
            print(f"First even number: {i}")
            break

range_size = 10

find_first_even(range_size)