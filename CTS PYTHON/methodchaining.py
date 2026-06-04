class Employee:
    def __init__(self):
        self.salary = 0

    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        else:
            print("Invalid salary")
        return self

    def apply_raise(self, raise_amount):
        if raise_amount > 0:
            self.salary += raise_amount
        else:
            print("Invalid raise amount")
        return self

    def display_salary(self):
        print(f"Final Salary: {self.salary}")
        return self

employee = Employee()

employee.set_salary(50000).apply_raise(5000).display_salary()