def get_salary(data, department, employee):
    if department not in data:
        print("Department not found")
        return

    if employee not in data[department]:
        print("Employee not found")
        return

    print(f"Salary: {data[department][employee]}")

employees = {
    "IT": {
        "Anki": 50000,
        "Rahul": 60000
    },
    "HR": {
        "Priya": 45000,
        "Kumar": 55000
    }
}

get_salary(employees, "IT", "Anki")