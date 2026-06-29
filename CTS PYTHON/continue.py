def sum_odd_numbers(limit):
    if limit <= 0:
        print("Invalid range")
        return

    total = 0

    for i in range(10):
        if i % 2 == 0:
            continue

        total += i

    print(f"Sum of odd numbers: {total}")

sum_odd_numbers(10)