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