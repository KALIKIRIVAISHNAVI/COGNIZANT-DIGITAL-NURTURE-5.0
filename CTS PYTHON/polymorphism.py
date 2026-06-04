class Employee:
    def work(self):
        print("Employee is working")

class Developer(Employee):
    def work(self):
        print("Developer is writing code")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team")

class Tester(Employee):
    def work(self):
        print("Tester is testing the application")

employees = [Developer(), Manager(), Tester()]

for employee in employees:
    employee.work()