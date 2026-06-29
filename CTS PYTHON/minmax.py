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