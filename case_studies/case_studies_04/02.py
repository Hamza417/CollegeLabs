account_no = int(input("Enter Account No: "))
name = input("Enter Name: ")

balance = abs(float(input("Enter Opening Balance: ")))

print()
print("Options")
print("1. Check Balance", "2. Deposit", "3. Withdrawal", "4: Statement", "0. Exit", sep="\n")

while True:
    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        print(f"Your Current Balance is: {balance:.2F} Rs")
        continue

    if choice == 2:
        amount = abs(float(input("Enter Amount to be Deposited: ")))
        balance += amount
        print(f"Amount Deposited Successfully, Updated Balance: {balance:.2F} Rs")
        continue

    if choice == 3:
        amount = abs(float(input("Enter Amount to be Withdrawn: ")))

        if amount <= balance:
            balance -= amount
        else:
            print(f"Insufficient Balance: {balance:.2F} Rs")
            continue

        print(f"Amount {amount:.2F} Rs withdrawn successfully."
              "\n"
              f"Remaining Balance: {balance:.2F} Rs")
        continue

    if choice == 4:
        print()
        print("=" * 40)
        print(f"{'BANK ACCOUNT STATEMENT':^40}")
        print("=" * 40)
        print(f"{'Name ':<20} : {name}")
        print(f"{'Account No ':<20} : {account_no}")
        print(f"{'Balance':<20} : {balance}")
        print("=" * 40)
        continue

    if choice == 0:
        print("Exiting...")
        break

    if choice not in range(0, 4):
        print("Invalid Choice!")
        continue
