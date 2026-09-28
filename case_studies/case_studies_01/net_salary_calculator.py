employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
hra = 0.2 * basic_salary  # House Rent Allowance (20% of basic salary)
da = 0.1 * basic_salary   # Dearness Allowance (10% of basic salary)
gross_salary = basic_salary + hra + da

tax_rate = 0.1  # Assuming a flat tax rate of 10%
tax_amount = gross_salary * tax_rate
net_salary = gross_salary - tax_amount

print(f"\nEmployee Name: {employee_name}")
print(f"Basic Salary: {basic_salary}")
print(f"House Rent Allowance (HRA): {hra}")
print(f"Dearness Allowance (DA): {da}")
print(f"Gross Salary: {gross_salary}")
print(f"Tax Amount: {tax_amount}")
print(f"Net Salary: {net_salary}")
