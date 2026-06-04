import csv
from datetime import datetime

# Read CSV file
with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)
    expenses = list(reader)

# Convert data types
for exp in expenses:
    exp["amount"] = float(exp["amount"])

# Get current month and year
now = datetime.now()
current_month = now.month
current_year = now.year

# Filter current month expenses
current_expenses = [
    exp for exp in expenses
    if datetime.strptime(exp["date"], "%Y-%m-%d").month == current_month
    and datetime.strptime(exp["date"], "%Y-%m-%d").year == current_year
]

# Group by category
category_totals = {}

for exp in current_expenses:
    cat = exp["category"]
    category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]

# Print summary
print("Expense Summary (Current Month):")
for cat, total in category_totals.items():
    print(cat, ":", total)