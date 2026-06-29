def add_expense(expenses, amount):
    if amount <= 0:
        print("Invalid expense amount")
        return

    expenses.append(amount)
    print("Updated Expenses List:")
    print(expenses)

expenses = [100, 250, 75]

add_expense(expenses, 150)