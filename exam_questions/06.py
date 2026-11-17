passengers = ["Ayesha", "Zoha", "Hamza", "Adib"]

while True:
    print(
        "1. Add",
        "2. Remove",
        "3. Sort",
        "4. Search",
        "5. Dashboard",
        "0. Exit",
        sep="\n"
    )

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter New Passenger's Name: ")
        passengers.append(name)
        print(name, "has been added to list.")
        continue

    if choice == 2:
        name = input("Enter Passenger's Name to Remove: ")
        if name in passengers:
            passengers.remove(name)
            print(name, "has been removed.")
            continue

    if choice == 3:
        passengers.sort()
        print("New List: ", passengers)
        continue

    if choice == 4:
        name = input("Enter Passenger's Name to Search: ")
        if name in passengers:
            print("FOUND")
        else:
            print("NOT FOUND")

    if choice == 5:
        print(50 * "=")
        print(f"{'AIRPLANE PASSENGERS LIST DASHBOARD':^50}")
        print(50 * "=")
        for i, p in enumerate(passengers, 1):
            print(f"{i:<2}. {p:<25}")
        print(50 * "-")
        print(f"{'Total Passengers':<25}: {len(passengers)}")
        print(50 * "=")
        continue

    if choice == 0:
        print("Exiting...")
        break