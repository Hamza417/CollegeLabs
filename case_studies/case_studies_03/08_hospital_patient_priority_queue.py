# Task 1: Initialize the waiting list as a list of dictionaries
waiting_list = []


def add_patient(name, age, is_emergency):
    """Task 2: Route patients based on priority using if-else logic."""
    patient = {'name': name, 'age': age, 'is_emergency': is_emergency}

    if is_emergency:
        # Insert critical patients at the head of the queue (Index 0)
        waiting_list.insert(0, patient)
    else:
        # Append standard patients to the tail of the queue
        waiting_list.append(patient)


def call_next_patient():
    """Task 3: Dequeue patients as doctors become available."""
    if len(waiting_list) > 0:
        # .pop(0) removes and returns the first element in the list
        return waiting_list.pop(0)
    else:
        print("Queue is empty.")
        return None


# ========================== Simulating Triage Operations ==========================

# 1. A critical patient arrives and is added to the empty queue
add_patient("Jane Roe", 55, True)

# 2. Regular patients arrive and are appended to the back
add_patient("Mary Smith", 29, False)
add_patient("Alex Brown", 42, False)

# 3. A doctor becomes available and calls the first patient (Jane Roe is dequeued)
call_next_patient()

# 4. A new critical patient arrives and jumps to the front of the line
add_patient("John Doe", 64, True)

# 5. Another regular patient arrives and is added to the back
add_patient("Emily Davis", 37, False)

# A major issue here any new critical patient will always be added to the front of the queue,
# regardless of how many critical patients are already waiting. This could lead to a situation
# where a patient who has been waiting for a long time is continually pushed back by new arrivals,
# which may not be ideal in a real-world triage scenario.

# 6. A new critical patient arrives and is added to the front of the queue
# Like in this case, Michael will be given priority over John Doe, even though John has been waiting longer.
add_patient("Michael Johnson", 70, True)

# One way to simply solve this is to maintain a separate priority queue for critical patients where
# they are first in the main line but still maintain their order of arrival among themselves.
# This way, the first critical patient to arrive will be treated before any subsequent critical
# patients, while still allowing regular patients to be treated in the order they arrived.

# ========================== End Simulation ==========================

# Task 4: Calculate average waiting patient age
total_age = 0
for patient in waiting_list:
    total_age += patient['age']

# Type casting to ensure clean float division, as requested
average_age = float(total_age) / int(len(waiting_list))

# Task 5: Generate the Hospital Triage Queue Dashboard
print("=" * 50)
print(f"{'HOSPITAL TRIAGE QUEUE DASHBOARD':^50}")
print("=" * 50)
print(f"{'Pos':<3} | {'Patient Name':<16} | {'Age':<3} | Priority Status")
print("-" * 50)

for index, patient in enumerate(waiting_list, start=1):
    # Ternary-style if-else (conditional expression) for inline string formatting
    status = "CRITICAL" if patient['is_emergency'] else "REGULAR"

    print(f"{index:<3} | {patient['name']:<16} | {patient['age']:<3} | {status}")

print("-" * 50)
print(f"{'Total Waiting Patients':<22} : {len(waiting_list)}")
print(f"{'Average Patient Age':<22} : {average_age:.1f} years")
print("=" * 50)