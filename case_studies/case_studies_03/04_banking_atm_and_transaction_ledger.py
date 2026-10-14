# Constants
ACCOUNT = {
    'account_number': '88291039',
    'holder_name': 'Adib Khan',
    'pin': '1234',
    'balance': 1000.00,
    'initial_balance': 1000.00,
    'transactions': []
}

# Declare the variables
authenticated = False
transaction_status = []

# Authenticate user
while not authenticated:
    entered_pin = input("Enter your 4-digit PIN: ").strip()
    if entered_pin == ACCOUNT['pin']:
        authenticated = True
        print("Authentication Successful.\n")
    else:
        print("Invalid PIN. Please try again.")

deposit_amount = float(input("Enter amount to deposit: $"))
withdrawal_amount = float(input("Enter amount to withdraw: $"))

# Evaluate the transactions
if deposit_amount > 0:
    ACCOUNT['balance'] += deposit_amount
    ACCOUNT['transactions'].append(('Deposit', deposit_amount))
    transaction_status.append(f"Deposit Approved (+${deposit_amount:.2f})")

if withdrawal_amount > 0:
    if ACCOUNT['balance'] >= withdrawal_amount:
        ACCOUNT['balance'] -= withdrawal_amount
        ACCOUNT['transactions'].append(('Withdrawal', withdrawal_amount))
        transaction_status.append(f"Withdrawal Approved (-${withdrawal_amount:.2f})")
    else:
        transaction_status.append(f"Withdrawal Denied (Insufficient Funds for ${withdrawal_amount:.2f})")

# Show the dashboard
print()
print("=" * 55)
print(f"{'BANK STATEMENT REPORT':^55}")
print("=" * 55)
print(f"Account Number: {ACCOUNT['account_number']}")
print(f"Holder Name   : {ACCOUNT['holder_name']}")
print("-" * 55)

# Display recent transaction statuses
for status in transaction_status:
    print(f"System: {status}")

print("-" * 55)
print(f"{'Type':<15} | {'Amount ($)':<12} | {'Balance ($)'}")
print("-" * 55)

# Print initial state
print(f"{'Initial Balance':<15} | {'':<12} | {ACCOUNT['initial_balance']:,.2f}")

# Reconstruct rolling balance for the ledger display
rolling_balance = ACCOUNT['initial_balance']

for transaction_type, amount in ACCOUNT['transactions']:
    if transaction_type == 'Deposit':
        rolling_balance += amount
    elif transaction_type == 'Withdrawal':
        rolling_balance -= amount

    print(f"{transaction_type:<15} | {amount:<12,.2f} | {rolling_balance:,.2f}")

print("-" * 55)
print(f"{'Closing Balance':<15} : ${ACCOUNT['balance']:,.2f}")
print("=" * 55)