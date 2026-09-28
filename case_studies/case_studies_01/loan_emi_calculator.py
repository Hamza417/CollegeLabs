loan_amount = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the annual interest rate (in %): "))
loan_period = float(input("Enter the loan period (in years): "))
monthly_interest_rate = interest_rate / (12 * 100)
number_of_payments = loan_period * 12

# Calculate Equated Monthly Installment (EMI) using the standard amortization formula.
# loan_amount: Principal borrowed (P)
# monthly_interest_rate: Monthly rate in decimal form (Annual Rate / 12 / 100) (r)
# number_of_payments: Total duration in months (Years * 12) (n)
emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / (
        (1 + monthly_interest_rate) ** number_of_payments - 1)

print(f"\nLoan Amount: {loan_amount}")
print(f"Annual Interest Rate: {interest_rate}%")
print(f"Loan Period: {loan_period} years")
print(f"Monthly EMI: {emi:.2F}")
