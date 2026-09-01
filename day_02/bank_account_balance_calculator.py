customer_name = input("Enter the customer's name: ")
current_balance = float(input("Enter the current account balance: "))
deposit_amount = float(input("Enter the deposit amount: "))
withdrawal_amount = float(input("Enter the withdrawal amount: "))
updated_balance = current_balance + deposit_amount - withdrawal_amount

print(f"\nCustomer Name: {customer_name}")
print(f"Current Account Balance: {current_balance}")
print(f"Deposit Amount: {deposit_amount}")
print(f"Withdrawal Amount: {withdrawal_amount}")
print(f"Updated Account Balance: {updated_balance}")
