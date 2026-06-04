import json

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}"

employees = {
    "E101": Employee("E101", "Anki", 50000),
    "E102": Employee("E102", "Rahul", 60000)
}

# Save to JSON file
def save_employees():
    data = {}

    for emp_id, emp in employees.items():
        data[emp_id] = {
            "name": emp.name,
            "salary": emp.salary
        }

    with open("emps.json", "w") as file:
        json.dump(data, file, indent=4)

# Load from JSON file
def load_employees():
    with open("emps.json", "r") as file:
        data = json.load(file)

    loaded_employees = {}

    for emp_id, details in data.items():
        loaded_employees[emp_id] = Employee(
            emp_id,
            details["name"],
            details["salary"]
        )

    return loaded_employees

save_employees()

loaded = load_employees()

print("Employee Details:")
for emp in loaded.values():
    print(emp)