name = input("Enter Name: ")
account_no = input("Enter Account No: ")
balance = float(input("Enter Balance: "))

while True:
    print(
        "1. Check Balance",
        "2. Deposit",
        "3. Withdraw",
        "4. Show Dashboard",
        "0. Exit",
        sep="\n"
    )

    print()
    choice = int(input("Enter Choice: "))

    if choice == 1:
        print(balance, "Rs")
    elif choice == 2:
        amount = float(input("Enter Amount to be Deposited:"))
        balance += amount
        print(amount, "Rs. has been deposited.")
    elif choice == 3:
        amount = float(input("Enter Amount to be Withdrawn:"))
        if amount <= balance:
            balance = balance - amount
        else:
            print("Not enough balance", balance, "Rs")
    elif choice == 4:
        print(50 * "=")
        print(f"{'BANK DASHBOARD':^50}")
        print(50 * "=")
        print(f"{'Customer Name':<25}: {name}")
        print(f"{'Account No':<25}, {account_no}")
        print(f"{'Current Balance':<25}: {round(balance)} Rs.")
        print(50 * "=")
    elif choice == 0:
        print("Exiting...")
        break
