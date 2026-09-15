# Task 1: Initialize account details in a dictionary (assume this is a database record for a single user)
account = {
    'account_number': '88291039',
    'holder_name': 'Adib Khan',
    'pin': '1234',
    'balance': 1000.00,
    'initial_balance': 1000.00,  # Stored separately to anchor the ledger
    'transactions': []  # Empty list for the audit trail
}

# Task 2: Implement a loop that verifies customer PIN using if-else
authenticated = False
entered_pin = ""

while entered_pin != account['pin']:
    entered_pin = input("Enter your 4-digit PIN: ").strip()

    if entered_pin == account['pin']:
        authenticated = True
        print("Authentication Successful.", end="\n\n")
    else:
        print("Invalid PIN. Please try again.")

# Erase entered pin store after authentication for security
entered_pin = ""

# Task 3 & 4: Create transactions and validate withdrawal limits
if authenticated:
    # Processing a Deposit
    deposit_amount = 250.00
    account['balance'] += deposit_amount
    account['transactions'].append(('Deposit', deposit_amount))

    # Processing a Withdrawal with Limit Validation
    withdrawal_amount = 100.00
    if account['balance'] - withdrawal_amount >= 0:
        account['balance'] -= withdrawal_amount
        account['transactions'].append(('Withdrawal', withdrawal_amount))
    else:
        # Prevents balance from dropping below zero
        print("Transaction Denied: Insufficient Funds.")

# Task 5: Output a formatted Bank Account Statement Report
print("=" * 55)
print(f"{'BANK STATEMENT REPORT':^55}")
print("=" * 55)
print(f"Account Number: {account['account_number']}")
print(f"Holder Name   : {account['holder_name']}")
print("-" * 55)
print(f"{'Type':<15} | {'Amount ($)':<12} | {'Balance ($)'}")
print("-" * 55)

# Print initial state
print(f"{'Initial Balance':<15} | {'':<12} | {account['initial_balance']:,.2f}")

# Reconstruct rolling balance for the ledger display
rolling_balance = account['initial_balance']

for transaction_type, amount in account['transactions']:
    if transaction_type == 'Deposit':
        rolling_balance += amount
    elif transaction_type == 'Withdrawal':
        rolling_balance -= amount

    print(f"{transaction_type:<15} | {amount:<12,.2f} | {rolling_balance:,.2f}")

print("-" * 55)
print(f"Closing Balance : ${account['balance']:,.2f}")
print("=" * 55)
