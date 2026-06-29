import csv

# Read CSV file
with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

# Convert salary to int
for emp in employees:
    emp["salary"] = int(emp["salary"])

# Filter employees with salary > 50000
high_salary = [emp for emp in employees if emp["salary"] > 50000]

# Calculate average salary
total_salary = sum(emp["salary"] for emp in employees)
avg_salary = total_salary / len(employees)

print("Employees with salary > 50000:")
for emp in high_salary:
    print(emp)

print("\nAverage Salary:", avg_salary)