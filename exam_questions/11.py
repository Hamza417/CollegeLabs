filename = "event_participants.txt"
count = int(input("Enter Number of Participants: "))

with open(filename, "a") as f:
    for i in range(0, count):
        name = input("Enter Name: ")
        institution = input("Enter Institution: ")
        f.write(name + " | " + institution + "\n")

    f.close()

record = []

with open(filename, "r") as f:
    record = f.readlines()
    f.close()

print(50 * "=")
print(f"{'FESTIVAL PARTICIPANTS':^50}")
print(50 * "=")
for i, p in enumerate(record, 1):
    print(f"{i}. {p.strip()}")
print(50 * "-")
print(f"{'Total Registrations':<50}")
print(50 * "=")