filename = "event_participants.txt"

num_participants = int(input("Enter number of participants to register: "))

# Append new participants to the file
with open(filename, "a") as f:
    for i in range(num_participants):
        name = input(f"Enter Name for Participant {i+1}: ")
        institution = input(f"Enter Institution for Participant {i+1}: ")
        f.write(f"{name} - {institution}\n")

# Read all registered participants
with open(filename, "r") as f:
    records = f.readlines()

# Show the dashboard
print("\n")
print("=" * 50)
print(f"{'NATIONAL EVENT DASHBOARD':^50}")
print("=" * 50)
print(f"{'Total Registrations':<25}: {len(records)}")
print("-" * 50)

for i, r in enumerate(records, 1):
    print(f"{str(i) + '.':<5} {r.strip()}")

print("=" * 50)
