

from tabulate import tabulate

class Converter:
    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15


conv = Converter()

while True:
    print("\n1. C to F")
    print("2. F to C")
    print("3. C to K")
    print("4. K to C")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    value = float(input("Enter temperature: "))

    if choice == 1:
        result = conv.c_to_f(value)
        unit = "F"
    elif choice == 2:
        result = conv.f_to_c(value)
        unit = "C"
    elif choice == 3:
        result = conv.c_to_k(value)
        unit = "K"
    elif choice == 4:
        result = conv.k_to_c(value)
        unit = "C"
    else:
        print("Invalid choice")
        continue

    table = [["Input", "Result"], [value, round(result, 2)]]

    print(tabulate(table, headers="firstrow", tablefmt="grid"))