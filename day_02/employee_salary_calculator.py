employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
hra = 0.2 * basic_salary  # House Rent Allowance (20% of basic salary)
da = 0.1 * basic_salary   # Dearness Allowance (10% of basic salary)
gross_salary = basic_salary + hra + da

print(f"\nEmployee Name: {employee_name}")
print(f"Basic Salary: {basic_salary}")
print(f"House Rent Allowance (HRA): {hra}")
print(f"Dearness Allowance (DA): {da}")
print(f"Gross Salary: {gross_salary}")