class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

# Create multiple objects
emp1 = Employee("Anki", 101)
emp2 = Employee("Rahul", 102)
emp3 = Employee("Priya", 103)

# Display employee information
emp1.display_info()
emp2.display_info()
emp3.display_info()

# Print employee names
print("\nEmployee Names:")
print(emp1.name)
print(emp2.name)
print(emp3.name)