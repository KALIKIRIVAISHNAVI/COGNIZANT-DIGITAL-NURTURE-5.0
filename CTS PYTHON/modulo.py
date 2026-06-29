def check_even_odd(number):
    if not isinstance(number, int):
        print("Invalid number")
        return

    remainder = number % 2

    if remainder == 0:
        print("Even")
    else:
        print("Odd")

number = 17

check_even_odd(number)