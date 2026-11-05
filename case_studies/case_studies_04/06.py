passengers = ["Ayesha", "Zoha", "Hamza", "Adib"]

print("Options")
print(
    "1. Add Passenger",
    "2. Remove Passenger",
    "3. Search Passenger",
    "4. Sort Passengers",
    "5. Dashboard",
    "0. Exit",
    sep="\n"
)

while True:
    choice = int(input("\nEnter Your Choice: "))

    if choice == 1:
        name = input("Enter Passenger Name to Add: ")
        passengers.append(name)
        print(f"Passenger '{name}' added successfully.")
        continue

    if choice == 2:
        name = input("Enter Passenger Name to Remove: ")
        if name in passengers:
            passengers.remove(name)
            print(f"Passenger '{name}' removed successfully.")
        else:
            print(f"Passenger '{name}' not found in the list.")
        continue

    if choice == 3:
        name = input("Enter Passenger Name to Search: ")
        if name in passengers:
            print(f"FOUND: Passenger '{name}' is in the list.")
        else:
            print(f"NOT FOUND: Passenger '{name}' is not in the list.")
        continue

    if choice == 4:
        passengers.sort()
        print("Passenger list sorted successfully.")
        continue

    if choice == 5:
        print("\n")
        print("=" * 50)
        print(f"{'AIRPORT PASSENGER DASHBOARD':^50}")
        print("=" * 50)
        print(f"{'Total Passengers':<25}: {len(passengers)}")
        print("-" * 50)
        for i, p in enumerate(passengers, 1):
            # Left aligning the number and printing the name
            print(f"{str(i) + '.':<5} {p}")
        print("=" * 50)
        continue

    if choice == 0:
        print("Exiting...")
        break

    if choice not in range(0, 6):
        print("Invalid Choice!")
        continue
