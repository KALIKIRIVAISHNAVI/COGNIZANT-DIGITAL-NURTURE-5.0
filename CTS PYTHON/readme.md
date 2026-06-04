## Name : KALIKIRI VAISHNAVI
## Register Number: 212223040081
# Installing Python & Running Programs
<img width="548" height="238" alt="image" src="https://github.com/user-attachments/assets/878aee53-74e7-4a6d-ba61-4a6d3e5948c4" />

<img width="1492" height="747" alt="ss1" src="https://github.com/user-attachments/assets/4a273f8a-c91b-4a8f-9361-fbd7e08bfc8d" />

<img width="615" height="237" alt="image" src="https://github.com/user-attachments/assets/dbf761f4-86ef-4607-8cfa-efcc10d7e9dd" />

<img width="1919" height="959" alt="image" src="https://github.com/user-attachments/assets/73ca3be6-095a-44c6-b916-891d6b0079f8" />

<img width="478" height="207" alt="image" src="https://github.com/user-attachments/assets/e72d5eee-034c-43af-8346-f7ad41dea461" />


### verified intellisense
<img width="997" height="547" alt="image" src="https://github.com/user-attachments/assets/5c14e4c5-569d-4190-97c4-a06c7df22b62" />

### program output
<img width="1919" height="1025" alt="image" src="https://github.com/user-attachments/assets/c3b77ede-8f5e-4265-86fe-51f9a3662d3e" />

## Data types
<img width="883" height="353" alt="image" src="https://github.com/user-attachments/assets/a4a1f6dc-9d57-4da0-b16f-f838f525dd96" />

```
def calculate_net_salary(salary, tax_rate):
    if salary < 0 or tax_rate < 0 or tax_rate > 1:
        return "Invalid salary or tax rate"

    tax = salary * tax_rate
    net_salary = salary - tax
    return net_salary

salary = 75000.5
tax_rate = 0.18

result = calculate_net_salary(salary, tax_rate)

if isinstance(result, str):
    print(result)
else:
    print(f"Net Salary: {result:.2f}")
```
<img width="1919" height="1079" alt="salary" src="https://github.com/user-attachments/assets/59fa8e2a-3f51-4152-b31a-f05324071ed2" />

## 5.variables
<img width="914" height="238" alt="image" src="https://github.com/user-attachments/assets/b9f85189-d0fb-4e13-818a-67a7493eacec" />

```
def display_coordinates(x, y):
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid coordinates")
        return

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

# Multiple assignment
x, y = 10, 20

display_coordinates(x, y)
```
<img width="1919" height="1073" alt="variables" src="https://github.com/user-attachments/assets/98851d61-74cb-4aac-863f-683b10372bc0" />

## Mathematical Operations
<img width="815" height="250" alt="image" src="https://github.com/user-attachments/assets/f9394e4a-2b4a-4c5c-8932-092c89135b35" />

```
def check_even_odd(number):
    if not isinstance(number, int):
        print("Invalid number")
        return

    remainder = number % 2

    if remainder == 0:
        print("Even")
    else:
        print("Odd")

number = 17

check_even_odd(number)
```
<img width="1919" height="1079" alt="modulo" src="https://github.com/user-attachments/assets/39de7181-a104-423a-8878-4ca10c7cc613" />

## 7.Floor Division
<img width="973" height="273" alt="image" src="https://github.com/user-attachments/assets/2e2c9385-fbd2-4906-a14b-99950b348e23" />

```
def calculate_share(total_bill, people):
    if total_bill < 0 or people <= 0:
        print("Invalid bill amount or number of people")
        return

    share = total_bill // people
    print(f"Individual Share: {share}")

total_bill = 1250
people = 4

calculate_share(total_bill, people)
```
<img width="1919" height="1079" alt="floor" src="https://github.com/user-attachments/assets/a6044b8d-8811-412f-8d10-26549b5ed289" />


<img width="1075" height="278" alt="image" src="https://github.com/user-attachments/assets/8af20165-15b2-4e24-8215-f1042b5cb9bb" />


```
def find_salary_range(salaries):
    if not salaries:
        print("Salary list is empty")
        return

    lowest_salary = min(salaries)
    highest_salary = max(salaries)

    print(f"Lowest Salary : {lowest_salary}")
    print(f"Highest Salary: {highest_salary}")

salaries = [50000, 75000, 62000, 95000]

find_salary_range(salaries)
```
<img width="1919" height="1079" alt="minmax" src="https://github.com/user-attachments/assets/2c2c4dfe-154f-473b-9642-39745aac6c83" />

## User Input

<img width="832" height="527" alt="image" src="https://github.com/user-attachments/assets/e694926d-c8a7-495f-a72c-df178209c65c" />

```
def greet_user():
    name = input("Enter your name: ")

    if name.strip() == "":
        print("Name cannot be empty")
        return

    print(f"Hello, {name}!")

greet_user()
```
<img width="1919" height="1079" alt="basicinput" src="https://github.com/user-attachments/assets/09f0e07d-5e90-42f3-81af-540cb0ec7d7c" />


<img width="828" height="276" alt="image" src="https://github.com/user-attachments/assets/e7be9f84-f352-44da-88c6-09d8a6e61557" />

```
def get_age():
    age = input("Enter your age: ")

    if not age.isdigit():
        print("Invalid age")
        return

    age = int(age)
    print(f"Next year you'll be {age + 1}")

get_age()
```
<img width="1919" height="1075" alt="numericinput" src="https://github.com/user-attachments/assets/4af82e43-8f84-409e-a600-0e01a5786445" />

<img width="827" height="236" alt="image" src="https://github.com/user-attachments/assets/447287d8-6899-4326-a4e3-2e9265eaf0f9" />

```
def convert_weight():
    weight = input("Enter weight in kilograms: ")

    try:
        kg = float(weight)

        if kg <= 0:
            print("Invalid weight")
            return

        lbs = kg * 2.20462
        print(f"Weight in pounds: {lbs:.2f}")

    except ValueError:
        print("Invalid input. Please enter a decimal number.")

convert_weight()
```
<img width="1919" height="1075" alt="floatinput" src="https://github.com/user-attachments/assets/2f0768ba-8386-4c5e-8611-7433426211d2" />

## Control flow
<img width="771" height="230" alt="image" src="https://github.com/user-attachments/assets/036314bf-9870-4062-a298-5645cdc0e77f" />

```
def check_pass_fail(marks):
    if marks < 0 or marks > 100:
        print("Invalid marks")
        return

    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

marks = 75

check_pass_fail(marks)
```

<img width="1919" height="1077" alt="simpleif" src="https://github.com/user-attachments/assets/7e1b8b1f-2097-425d-bb80-f4d6e35fce5b" />



<img width="849" height="232" alt="image" src="https://github.com/user-attachments/assets/639af407-624f-4e1c-9c23-dc34a2b6638a" />

```
def check_even_odd(num):
    if not isinstance(num, int):
        print("Invalid input")
        return

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = 8

check_even_odd(num)
```

<img width="1919" height="1078" alt="ifelse py" src="https://github.com/user-attachments/assets/9faa5955-533a-414e-99da-ecfe7870ab2f" />


<img width="969" height="570" alt="image" src="https://github.com/user-attachments/assets/f1811e76-a2f3-41b4-8028-4be8e4c65957" />

```
def assign_grade(score):
    if score < 0 or score > 100:
        print("Invalid score")
        return

    if score >= 80:
        grade = "A"
    elif score >= 60:
        grade = "B"
    else:
        grade = "C"

    print(f"Score : {score}")
    print(f"Grade : {grade}")

score = 88

assign_grade(score)
```

<img width="1919" height="1079" alt="ifelifelse" src="https://github.com/user-attachments/assets/56c7a7e0-94c7-44db-8776-86be8efe27d5" />


<img width="882" height="284" alt="image" src="https://github.com/user-attachments/assets/9abbdb4d-a531-4016-8903-600fc5884827" />

```
def validate_login(user, pwd):
    if user == "" or pwd == "":
        print("Username or password cannot be blank")
        return

    if user == "admin":
        if pwd == "pass123":
            print("Login Successful")
        else:
            print("Incorrect Password")
    else:
        print("Invalid Username")

user = "admin"
pwd = "pass123"

validate_login(user, pwd)
```

<img width="1919" height="1079" alt="nestedif py" src="https://github.com/user-attachments/assets/804bc5f9-d1e2-4676-a5a0-2af4153bc87a" />


<img width="903" height="259" alt="image" src="https://github.com/user-attachments/assets/39027556-dbd4-40e2-a862-a737d542f070" />

```
def print_numbers(count):
    if count <= 0:
        print("Invalid loop count")
        return

    for i in range(5):
        print(i + 1)

count = 5

print_numbers(count)
```

<img width="1919" height="1079" alt="forloop" src="https://github.com/user-attachments/assets/b35b7c24-e6bb-42e2-a30e-068d9d891626" />


<img width="882" height="263" alt="image" src="https://github.com/user-attachments/assets/8e0324bf-3676-4c04-ba17-431346eabdbe" />

```
def countdown(count):
    if count <= 0:
        print("Invalid count value")
        return

    while count > 0:
        print(count)
        count -= 1

count = 5

countdown(count)
```

<img width="1917" height="1073" alt="whileloop" src="https://github.com/user-attachments/assets/e827f5d5-f218-4e2b-a56a-16e3e1147038" />


<img width="885" height="289" alt="image" src="https://github.com/user-attachments/assets/648c5939-c1f1-44cf-9f2f-5ba41768b765" />

```
def find_first_even(range_size):
    if range_size <= 0:
        print("Invalid range size")
        return

    for i in range(1, range_size + 1):
        if i % 2 == 0:
            print(f"First even number: {i}")
            break

range_size = 10

find_first_even(range_size)
```
<img width="1919" height="1077" alt="break" src="https://github.com/user-attachments/assets/63cf8972-0627-4919-a186-0a8467e71aeb" />



<img width="872" height="588" alt="image" src="https://github.com/user-attachments/assets/df26019c-10f0-4ce1-b735-f5fe59754595" />

```
def sum_odd_numbers(limit):
    if limit <= 0:
        print("Invalid range")
        return

    total = 0

    for i in range(10):
        if i % 2 == 0:
            continue

        total += i

    print(f"Sum of odd numbers: {total}")

sum_odd_numbers(10)
```

<img width="1919" height="1079" alt="continue" src="https://github.com/user-attachments/assets/70165c9e-cf1c-42a9-a746-3eba8e5e2473" />


<img width="893" height="268" alt="image" src="https://github.com/user-attachments/assets/fb3f6bc3-0e54-4b6b-85db-bfac50f0b189" />

```
def my_function():
    pass

my_function()

print("Function defined")
```


<img width="1919" height="1076" alt="pass" src="https://github.com/user-attachments/assets/fe87d9ec-fbb2-41b6-945a-a05c2a6fdfad" />


## WhiteSpace Importance

<img width="808" height="285" alt="image" src="https://github.com/user-attachments/assets/31bdf6b9-62c1-4be3-bdf0-e0a67aa96ecd" />

```
def check_conditions():
    condition1 = True
    condition2 = True

    if condition1:
        if condition2:
            print("Nested")

    print("Confirmation message")

check_conditions()
```

<img width="1919" height="1079" alt="intendation" src="https://github.com/user-attachments/assets/06c3fd48-551c-4395-83e4-1097de75e71a" />


## Organizing Programs

<img width="830" height="271" alt="image" src="https://github.com/user-attachments/assets/c9e33767-a0f5-4a86-89ac-39dbfd3cd918" />

```
def calculate_total_salary():
    # Define the base salary
    base_salary = 50000

    # Define the bonus amount
    bonus = 10000

    # Calculate the total salary
    total_salary = base_salary + bonus

    # Display the total salary
    print(f"Total Salary: {total_salary}")

calculate_total_salary()
```
<img width="1919" height="1079" alt="comment" src="https://github.com/user-attachments/assets/630e9934-079e-463a-8be7-63696b268569" />

## Modules

<img width="938" height="541" alt="image" src="https://github.com/user-attachments/assets/ad7d5def-390e-43da-860f-408e36c830ba" />


```
import math

def calculate_area(radius):
    if radius <= 0:
        print("Invalid radius")
        return

    area = math.pi * radius ** 2
    print(f"Area of Circle: {area:.2f}")

radius = 5

calculate_area(radius)
```

<img width="1919" height="1079" alt="module" src="https://github.com/user-attachments/assets/17d36c93-3970-4e0c-8bd2-579405b86ca8" />


<img width="887" height="290" alt="image" src="https://github.com/user-attachments/assets/53394dd4-a0bf-41ca-a881-5286f29c9558" />

```
from math import *

def math_operations(number):
    if number < 0:
        print("Invalid input")
        return

    print(f"Square Root: {sqrt(number):.2f}")
    print(f"Power (number²): {pow(number, 2):.2f}")
    print(f"Value of Pi: {pi:.2f}")

number = 16

math_operations(number)
```

<img width="1917" height="1079" alt="import" src="https://github.com/user-attachments/assets/65667359-e4af-47e1-9dd4-ca3341ecd959" />


## Functions

<img width="848" height="256" alt="image" src="https://github.com/user-attachments/assets/b529c57f-ed14-400e-86bb-fc3bf1d31d7e" />


```
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        print("Invalid input")
        return None

    return a + b

result = add(5, 3)

if result is not None:
    print(f"Sum: {result}")
```

<img width="1919" height="1079" alt="parameters" src="https://github.com/user-attachments/assets/ae90f409-4dbf-48f1-ba21-47141bf27dd8" />


<img width="889" height="264" alt="image" src="https://github.com/user-attachments/assets/dc2c28e8-33f4-4b36-b11a-e7b3785c91c4" />

```
def area(length, width):
    if length <= 0 or width <= 0:
        print("Invalid dimensions")
        return None

    return length * width

result = area(5, 3)

if result is not None:
    print(f"Area: {result}")
```


<img width="1919" height="1079" alt="multiple py" src="https://github.com/user-attachments/assets/c49a47e2-7384-4d13-84a1-868aeac26562" />



# Built-in Functions

<img width="812" height="298" alt="image" src="https://github.com/user-attachments/assets/1c0f83d0-59ba-4720-9c13-013fa1189ebb" />


```
def string_length(text):
    if text.strip() == "":
        print("Invalid string")
        return

    print(f"Length: {len(text)}")

text = "Hello World"

string_length(text)
```

<img width="1919" height="1079" alt="len" src="https://github.com/user-attachments/assets/0a373235-dad6-4e62-b6c4-c3eac3ee87c9" />


## File I/O

<img width="802" height="254" alt="image" src="https://github.com/user-attachments/assets/d7330fcf-add9-4f03-bf6e-2d63b08e519b" />


```
def write_greeting():
    with open("greeting.txt", "w") as file:
        file.write("Hello World")

    print("Message written to file successfully")

write_greeting()
```

<img width="1919" height="1079" alt="wtofile" src="https://github.com/user-attachments/assets/e4696890-b8c0-4e86-a495-ae8c154c5f73" />


<img width="815" height="275" alt="image" src="https://github.com/user-attachments/assets/86e2afd4-5cab-4582-9165-d6046daca37a" />

```
def read_file():
    try:
        with open("greeting.txt", "r") as file:
            content = file.read()
            print("File Content:")
            print(content)

    except FileNotFoundError:
        print("File not found")

read_file()
```

<img width="1919" height="1079" alt="rff" src="https://github.com/user-attachments/assets/492b92ce-297b-4fde-a185-428fec72f474" />

## Error Handling

<img width="949" height="264" alt="image" src="https://github.com/user-attachments/assets/dc85a05b-b3af-4262-b48c-124a164610fd" />

```
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"Result: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

divide_numbers(10, 2)
```


<img width="1913" height="1079" alt="error" src="https://github.com/user-attachments/assets/3a9bebc5-39e0-4ae1-9006-7ee8b89e9639" />



## Lists

<img width="840" height="233" alt="image" src="https://github.com/user-attachments/assets/c874f4cf-7ca6-4503-b808-c55ce4a9ca15" />


```
def display_cart():
    cart = [100, 250, 75]

    if not cart:
        print("Cart is empty")
        return

    print("Cart Contents:")
    for item in cart:
        print(item)

display_cart()
```

<img width="1919" height="1079" alt="create" src="https://github.com/user-attachments/assets/594ddb8c-cfad-49e0-8b6d-875696d1d1c9" />




<img width="899" height="521" alt="image" src="https://github.com/user-attachments/assets/e5b4dbf5-5627-47a2-aeee-be179df093a3" />

```
def add_expense(expenses, amount):
    if amount <= 0:
        print("Invalid expense amount")
        return

    expenses.append(amount)
    print("Updated Expenses List:")
    print(expenses)

expenses = [100, 250, 75]

add_expense(expenses, 150)
```

<img width="1919" height="1079" alt="append" src="https://github.com/user-attachments/assets/d727d931-4d3e-4b9e-91c2-decd702bd14d" />



# Dictionaries

<img width="819" height="238" alt="image" src="https://github.com/user-attachments/assets/955a42fd-81f4-4c0a-89b8-db8a4197cb87" />

```
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
```


<img width="1919" height="1079" alt="dictionary" src="https://github.com/user-attachments/assets/1acda580-aa26-49d8-97c7-f80a9b934cef" />



<img width="885" height="252" alt="image" src="https://github.com/user-attachments/assets/4c707d4c-3e0a-46d5-9e07-97c6a9d3b302" />


```
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
```

<img width="1919" height="1079" alt="nested" src="https://github.com/user-attachments/assets/ada53cab-a9be-403c-baad-67e08732f582" />


## Tuples and Sets

<img width="782" height="237" alt="image" src="https://github.com/user-attachments/assets/01b40621-d15a-4ba5-bee6-7cbc314ad53e" />

```
def display_coordinates(coords):
    if len(coords) != 2:
        print("Invalid coordinates")
        return

    x, y = coords

    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        print("Invalid coordinate values")
        return

    print(f"X Coordinate: {x}")
    print(f"Y Coordinate: {y}")

coordinates = (10, 20)

display_coordinates(coordinates)
```

<img width="1919" height="1079" alt="tuple" src="https://github.com/user-attachments/assets/f2f5e633-d7f8-4687-90ad-048255769a01" />



<img width="924" height="347" alt="image" src="https://github.com/user-attachments/assets/75168d0a-7d45-4dac-a10c-1385d166eb8a" />


```
def find_common_skills(skills1, skills2):
    if not isinstance(skills1, set) or not isinstance(skills2, set):
        print("Invalid input")
        return

    common_skills = skills1 & skills2

    print("Common Skills:")
    print(common_skills)

employee1_skills = {"Python", "Java", "SQL"}
employee2_skills = {"Python", "C++", "SQL"}

find_common_skills(employee1_skills, employee2_skills)
```

<img width="1919" height="1079" alt="set" src="https://github.com/user-attachments/assets/feb2d894-117e-4035-9ddc-ef15ec41b908" />



# OOP Concepts
# Classes


<img width="794" height="236" alt="image" src="https://github.com/user-attachments/assets/9b6afc49-a7c8-4ada-a608-ab0bfe34044c" />


```
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

emp1 = Employee("Anki", 101)
emp2 = Employee("Rahul", 102)
emp3 = Employee("Priya", 103)

emp1.display_info()
emp2.display_info()
emp3.display_info()


print("\nEmployee Names:")
print(emp1.name)
print(emp2.name)
print(emp3.name)
```

<img width="1919" height="1078" alt="mi" src="https://github.com/user-attachments/assets/f117814c-5a3d-404c-a810-7c77953afe68" />


<img width="909" height="268" alt="image" src="https://github.com/user-attachments/assets/e82c0502-eb30-42c1-af39-23bb9cc83a31" />


```
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
```

<img width="1918" height="1079" alt="methodchaining" src="https://github.com/user-attachments/assets/3f70120a-7319-49d7-829c-f3c3721e8e41" />


# Custom Classes and Inheritance

<img width="866" height="283" alt="image" src="https://github.com/user-attachments/assets/4e202677-3880-4b64-8831-364e8b672c97" />

```
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
```


<img width="1917" height="1076" alt="polymorphism" src="https://github.com/user-attachments/assets/ce0c15a2-c0a1-44d5-ac19-bccb1ecfaefc" />


<img width="860" height="285" alt="image" src="https://github.com/user-attachments/assets/702d2970-2628-46b5-b637-c5699e0dabdc" />


```
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
```

<img width="1919" height="1014" alt="classmethods" src="https://github.com/user-attachments/assets/38baa026-ba79-48d8-bb16-ae5759b7337d" />


# Real time Simulation hands-on questions


<img width="881" height="262" alt="image" src="https://github.com/user-attachments/assets/e8e7c5c2-6cbe-463e-8d51-bc0e7a28dda0" />


```
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
```

<img width="1919" height="1079" alt="ems" src="https://github.com/user-attachments/assets/f55de510-df23-40d5-a065-0b43b924acb7" />


<img width="846" height="259" alt="image" src="https://github.com/user-attachments/assets/0ac8d1dd-981f-4e08-aa05-ca1547a7acec" />


```
import statistics

def analyze_sales():
    try:
        with open("sales.txt", "r") as file:
            sales = []

            for line in file:
                sales.append(float(line.strip()))

        mean_sales = statistics.mean(sales)
        median_sales = statistics.median(sales)

        print("Sales Statistics Summary")
        print(f"Total Records: {len(sales)}")
        print(f"Mean Sales: {mean_sales:.2f}")
        print(f"Median Sales: {median_sales:.2f}")

    except FileNotFoundError:
        print("Error: sales.txt file not found")

    except ValueError:
        print("Error: Invalid data in sales file")

analyze_sales()
```

<img width="1919" height="1079" alt="dap" src="https://github.com/user-attachments/assets/b3236c9e-38f0-446b-8d75-6bedc3c91a1d" />


<img width="942" height="299" alt="image" src="https://github.com/user-attachments/assets/7bc3f69d-11cd-4683-b8ff-335e7a531b7d" />


```
import configparser

class Config:
    def __init__(self, file):
        self.config = configparser.ConfigParser()
        self.config.read(file)

class DatabaseConfig(Config):
    def __init__(self, file):
        super().__init__(file)
        self.data = self.config["database"]
        req = ["host","port","username","password","dbname"]
        for k in req:
            if k not in self.data:
                raise Exception("Missing key: " + k)

db = DatabaseConfig("db.ini")
print("Config loaded successfully")
```

<img width="1919" height="1079" alt="configuration" src="https://github.com/user-attachments/assets/c8499d7f-f2d5-4c19-997f-9c8f94e2e4fa" />



<img width="936" height="238" alt="image" src="https://github.com/user-attachments/assets/42f00c2c-e7cd-4ad9-8e56-083951f18b05" />


```
import csv


with open("employees.csv", "r") as file:
    reader = csv.DictReader(file)
    employees = list(reader)

for emp in employees:
    emp["salary"] = int(emp["salary"])


high_salary = [emp for emp in employees if emp["salary"] > 50000]


total_salary = sum(emp["salary"] for emp in employees)
avg_salary = total_salary / len(employees)

print("Employees with salary > 50000:")
for emp in high_salary:
    print(emp)

print("\nAverage Salary:", avg_salary)
```


<img width="1919" height="1079" alt="employees" src="https://github.com/user-attachments/assets/06263fe9-78e0-48c3-bea8-a1e1479b8b1d" />


<img width="931" height="564" alt="image" src="https://github.com/user-attachments/assets/712b2817-4a91-4408-b4f6-02a1aa94f73a" />


```
import csv
from datetime import datetime


with open("expenses.csv", "r") as file:
    reader = csv.DictReader(file)
    expenses = list(reader)


for exp in expenses:
    exp["amount"] = float(exp["amount"])


now = datetime.now()
current_month = now.month
current_year = now.year


current_expenses = [
    exp for exp in expenses
    if datetime.strptime(exp["date"], "%Y-%m-%d").month == current_month
    and datetime.strptime(exp["date"], "%Y-%m-%d").year == current_year
]


category_totals = {}

for exp in current_expenses:
    cat = exp["category"]
    category_totals[cat] = category_totals.get(cat, 0) + exp["amount"]


print("Expense Summary (Current Month):")
for cat, total in category_totals.items():
    print(cat, ":", total)
```


<img width="1919" height="1079" alt="expenses" src="https://github.com/user-attachments/assets/4114864b-cc4c-45e3-9b43-4b534d46a084" />


<img width="894" height="299" alt="image" src="https://github.com/user-attachments/assets/1a54f986-c88c-46de-8e7d-acd174c24f77" />


```
class WeatherAPI:
    def fetch_data(self):
        data = {
            "main": {"temp": 28.5},
            "weather": [{"description": "clear sky"}]
        }

        print("Weather Report")
        print("Temperature:", data["main"]["temp"])
        print("Condition:", data["weather"][0]["description"])

api = WeatherAPI()
api.fetch_data()
```


<img width="1917" height="1079" alt="api" src="https://github.com/user-attachments/assets/95833e29-f92a-4a15-9452-78b0312210d0" />


# Additional real-time simulation hands on questions

<img width="613" height="263" alt="image" src="https://github.com/user-attachments/assets/765b1466-c619-4f33-9525-a9aaecf6767d" />


```
def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError
        return a / b
    else:
        return "Invalid operator"

try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    result = calculate(a, b, op)
    print("Result:", result)

except ValueError:
    print("Error: Invalid number input")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")
```

<img width="1919" height="1079" alt="calculator python" src="https://github.com/user-attachments/assets/18ed5d1e-fe4a-4bbe-8be6-2199e9e15bd2" />



<img width="900" height="372" alt="image" src="https://github.com/user-attachments/assets/6df9f8dd-1fa7-4e8f-8afb-a3d149003ed5" />


```
class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]

    def calculate_total(self):
        return sum(item.total() for item in self.items)

    def print_receipt(self):
        print("\n--- Receipt ---")
        for item in self.items:
            print(item.name, item.price, "x", item.quantity, "=", item.total())

        total = self.calculate_total()
        gst = total * 0.18
        final = total + gst

        print("\nSubtotal:", total)
        print("GST (18%):", gst)
        print("Final Total:", final)



cart = ShoppingCart()

cart.add_item(CartItem("Book", 200, 2))
cart.add_item(CartItem("Pen", 20, 5))
cart.add_item(CartItem("Bag", 500, 1))

cart.remove_item("Pen")
cart.print_receipt()
```

<img width="1919" height="1078" alt="cart" src="https://github.com/user-attachments/assets/4c18edb7-fede-41c4-88f6-3f236f20d3e7" />



<img width="801" height="563" alt="image" src="https://github.com/user-attachments/assets/4c177421-e7e7-4adb-bbdc-919cf3cc356a" />


```
from tabulate import tabulate

class Converter:
    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15


conv = Converter()

while True:
    print("\n1. C to F")
    print("2. F to C")
    print("3. C to K")
    print("4. K to C")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        break

    value = float(input("Enter temperature: "))

    if choice == 1:
        result = conv.c_to_f(value)
        unit = "F"
    elif choice == 2:
        result = conv.f_to_c(value)
        unit = "C"
    elif choice == 3:
        result = conv.c_to_k(value)
        unit = "K"
    elif choice == 4:
        result = conv.k_to_c(value)
        unit = "C"
    else:
        print("Invalid choice")
        continue

    table = [["Input", "Result"], [value, round(result, 2)]]

    print(tabulate(table, headers="firstrow", tablefmt="grid"))
```

<img width="1919" height="1079" alt="temper" src="https://github.com/user-attachments/assets/5547a5be-27d0-44d4-b346-cac08774a2ba" />



<img width="872" height="271" alt="image" src="https://github.com/user-attachments/assets/5869554f-5687-41dc-a988-c89b440a3dd9" />


```
import os
import shutil

class BackupUtility:
    def __init__(self, source, backup):
        self.source = source
        self.backup = backup
        self.copied = set()

    def backup_files(self):
        os.makedirs(self.backup, exist_ok=True)

        log = open("backup.log", "w")

        try:
            files = os.listdir(self.source)

            for file in files:
                if file in self.copied:
                    continue

                src = os.path.join(self.source, file)
                dest = os.path.join(self.backup, file)

                try:
                    shutil.copy2(src, dest)
                    self.copied.add(file)
                    log.write(f"Copied: {file}\n")
                    print("Copied:", file)

                except FileNotFoundError:
                    log.write(f"Missing file: {file}\n")
                    print("File not found:", file)

                except PermissionError:
                    log.write(f"Permission denied: {file}\n")
                    print("Permission error:", file)

        finally:
            log.close()


# Example usage
source_folder = "source_files"
backup_folder = "backup_files"

backup = BackupUtility(source_folder, backup_folder)
backup.backup_files()
```

<img width="1919" height="1079" alt="utility" src="https://github.com/user-attachments/assets/bfd606a9-dc94-4ed7-894c-95545e9bb4c6" />



<img width="974" height="267" alt="image" src="https://github.com/user-attachments/assets/de052b98-9199-4db6-9778-0879385831d4" />


```
import hashlib

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        hash_obj = hashlib.md5(url.encode())
        short = hash_obj.hexdigest()[:6]
        self.url_map[short] = url
        return short

    def retrieve(self, short):
        return self.url_map.get(short, "URL not found")


u = URLShortener()

short = u.shorten("https://www.google.com")
print("Short URL:", short)

original = u.retrieve(short)
print("Original URL:", original)
```

<img width="1919" height="1079" alt="url" src="https://github.com/user-attachments/assets/d54b8d33-2252-4f38-9fde-2c810e097fa1" />



<img width="876" height="290" alt="image" src="https://github.com/user-attachments/assets/f0fdb9d1-3470-4979-b7ee-937f0352a56f" />


```
import json

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_grade(self, name, grade):
        if not (0 <= grade <= 100):
            print("Invalid grade")
            return

        if name not in self.students:
            self.students[name] = []

        self.students[name].append(grade)

    def calculate_gpa(self, grades):
        return sum(grades) / len(grades) if grades else 0

    def class_average(self):
        all_grades = [g for grades in self.students.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def save(self, file="grades.json"):
        with open(file, "w") as f:
            json.dump(self.students, f)

    def load(self, file="grades.json"):
        try:
            with open(file, "r") as f:
                self.students = json.load(f)
        except FileNotFoundError:
            print("No saved data found")



g = Gradebook()

g.add_grade("Anki", 85)
g.add_grade("Anki", 90)
g.add_grade("John", 70)

print("Anki GPA:", g.calculate_gpa(g.students["Anki"]))
print("Class Average:", g.class_average())

g.save()
```

<img width="1919" height="1079" alt="gradebook" src="https://github.com/user-attachments/assets/2b85e2f2-7e18-44a3-b171-0d41bf580f0d" />


<img width="947" height="299" alt="image" src="https://github.com/user-attachments/assets/4354635f-1716-452b-9699-bf20e22cc69e" />


```
from datetime import datetime

class Task:
    def __init__(self, name, due_date, priority):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.priority = priority

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def sort_tasks(self):
        self.tasks.sort(key=lambda x: x.due_date)

    def get_overdue(self):
        now = datetime.now()
        return [t for t in self.tasks if t.due_date < now]

    def print_tasks(self):
        print("\n--- Task Schedule ---")
        for t in self.tasks:
            print(t.name, t.due_date.date(), "Priority:", t.priority)



scheduler = TaskScheduler()

scheduler.add_task(Task("Math Assignment", "2026-06-01", "High"))
scheduler.add_task(Task("Project", "2026-06-10", "Medium"))
scheduler.add_task(Task("Exam Prep", "2026-05-30", "High"))

scheduler.sort_tasks()
scheduler.print_tasks()

print("\n--- Overdue Tasks ---")
for t in scheduler.get_overdue():
    print(t.name, t.due_date.date())
```

<img width="1919" height="1079" alt="task" src="https://github.com/user-attachments/assets/f6137749-cc54-42c4-93ad-655fd68ffbd8" />


<img width="893" height="579" alt="image" src="https://github.com/user-attachments/assets/ca83c416-774b-4c9b-a570-d3081e636f3d" />


```
class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


class Perishable(Product):
    pass


class Electronics(Product):
    pass


class Inventory:
    def __init__(self):
        self.items = {}          # dictionary: name -> product
        self.low_stock = set()   # set for alerts

    def add_product(self, product):
        self.items[product.name] = product

    def update_stock(self, name, stock):
        if name in self.items:
            self.items[name].stock = stock

    def check_low_stock(self):
        self.low_stock.clear()
        for name, product in self.items.items():
            if product.stock < 5:
                self.low_stock.add(name)

    def print_summary(self):
        print("\n--- Inventory Summary ---")
        for name, product in self.items.items():
            print(name, "Stock:", product.stock)

        self.check_low_stock()

        print("\nLow Stock Alerts:")
        for item in self.low_stock:
            print(item)


inv = Inventory()

inv.add_product(Perishable("Milk", 3))
inv.add_product(Electronics("Laptop", 10))
inv.add_product(Perishable("Eggs", 2))

inv.print_summary()
```


<img width="1919" height="1078" alt="inventory" src="https://github.com/user-attachments/assets/67b68ba2-fa53-41e5-8d14-48c02baad819" />


<img width="1021" height="401" alt="image" src="https://github.com/user-attachments/assets/c9536744-de0f-4c62-a613-6ed9aca6151a" />


```
import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        self.spent += amount
        if self.spent > self.limit:
            print("Alert:", self.name, "budget exceeded!")


class BudgetPlanner:
    def __init__(self):
        self.categories = {}

    def add_category(self, name, limit):
        self.categories[name] = Category(name, limit)

    def add_expense(self, name, amount):
        if name in self.categories:
            self.categories[name].add_expense(amount)

    def show_summary(self):
        names = []
        spent = []

        print("\n--- Budget Summary ---")
        for cat in self.categories.values():
            print(cat.name, "Spent:", cat.spent, "Limit:", cat.limit)
            names.append(cat.name)
            spent.append(cat.spent)

       
        plt.figure()
        plt.pie(spent, labels=names, autopct="%1.1f%%")
        plt.title("Monthly Budget Distribution")
        plt.show()

bp = BudgetPlanner()

bp.add_category("Food", 5000)
bp.add_category("Rent", 10000)
bp.add_category("Travel", 3000)

while True:
    choice = input("Add expense? (y/n): ")
    if choice.lower() != "y":
        break

    cat = input("Category: ")
    amt = float(input("Amount: "))

    bp.add_expense(cat, amt)

bp.show_summary()
```

<img width="1916" height="1079" alt="budget" src="https://github.com/user-attachments/assets/88e85da4-efd5-455e-9b93-133cb9f24636" />
