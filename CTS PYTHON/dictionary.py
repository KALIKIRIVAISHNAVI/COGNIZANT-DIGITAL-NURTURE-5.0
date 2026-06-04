def merge_employee_data(emp1, emp2):
    if not isinstance(emp1, dict) or not isinstance(emp2, dict):
        print("Invalid dictionary input")
        return

    emp1.update(emp2)

    print("Updated Employee Data:")
    print(emp1)

employee1 = {
    "name": "Anki",
    "age": 20
}

employee2 = {
    "department": "IT",
    "salary": 50000
}

merge_employee_data(employee1, employee2)