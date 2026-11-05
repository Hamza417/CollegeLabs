filename = "academic_events.txt"

# Initial data to write to the file
events = [
    ("Seminar", "AI & Data Science", 120),
    ("Workshop", "Python Programming", 80),
    ("Hackathon", "Innovation Challenge", 150),
    ("Seminar", "Machine Learning", 100),
    ("Workshop", "Cyber Security", 75)
]

# Write data to file using '|' as a delimiter
with open(filename, "w") as f:
    for event_type, title, participants in events:
        f.write(f"{event_type}|{title}|{participants}\n")

# Initialize counters for the dashboard
counts = {"Seminar": 0, "Workshop": 0, "Hackathon": 0}
total_participants = 0

# Read data from the file and process it
with open(filename, "r") as f:
    for line in f:
        # Strip newline characters and split by the delimiter
        event_type, title, participants = line.strip().split("|")

        # Increment counts
        if event_type in counts:
            counts[event_type] += 1

        total_participants += int(participants)

# Show the dashboard
print("\n")
print("=" * 55)
print(f"{'SEMINAR / WORKSHOP / HACKATHON DASHBOARD':^55}")
print("=" * 55)
print(f"{'Total Seminars':<25}: {counts['Seminar']}")
print(f"{'Total Workshops':<25}: {counts['Workshop']}")
print(f"{'Total Hackathons':<25}: {counts['Hackathon']}")
print("-" * 55)
print(f"{'Total Participants':<25}: {total_participants}")
print("=" * 55)