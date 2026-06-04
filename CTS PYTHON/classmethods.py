class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @classmethod
    def from_string(cls, emp_data):
        name, salary = emp_data.split(",")
        salary = int(salary)
        return cls(name.strip(), salary)

    def display(self):
        print(f"Employee Name: {self.name}")
        print(f"Salary: {self.salary}")

emp = Employee.from_string("Shubh,75000")
emp.display()