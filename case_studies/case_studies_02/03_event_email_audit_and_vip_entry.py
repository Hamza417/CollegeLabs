# Simulated raw data representing form submissions (can contain duplicates)
raw_registrations = [
    "adib@email.com", "adim@email.com", "aysha@email.com",
    "saima@email.com", "shifa@email.com", "hassan@email.com",
    "riyaz@email.com", "mobasshara@email.com", "adib@email.com"
]

# Simulated data for people who actually scanned their ticket at the door
actual_check_ins_list = [
    "adib@email.com", "aysha@email.com", "saima@email.com", "hassan@email.com", "riyaz@email.com"
]

# Predefined set of VIPs
vip_list = {
    "adib@email.com", "riyaz@email.com", "hassan@email.com", "aysha@email.com"
}

# Task 1: Convert raw lists into Sets to automatically extract unique values
unique_registrants = set(raw_registrations)
actual_check_ins = set(actual_check_ins_list)

# Task 2: Perform set intersection to find VIPs who actually checked in
vips_present = actual_check_ins.intersection(vip_list)

# Task 3: Perform set difference to find registered individuals who did not attend
absentees = unique_registrants.difference(actual_check_ins)

# Task 4: Normalize user input and verify registration
simulated_input = ""

# Validate the entered email id format
# This should prevent just any string input and ensure it resembles an email format
while not simulated_input:
    simulated_input = input("Enter email to check registration: ").strip()

    # Repeat until a valid email format is provided
    if simulated_input.split("@")[-1] not in ["email.com", "gmail.com"]:
        print("Invalid email domain. Please enter a valid email address.")
        simulated_input = ""

# Chaining string methods to sanitize the input data
normalized_email = simulated_input.lower().strip()
# Boolean check using the 'in' operator (O(1) time complexity in a set)
is_registered = normalized_email in unique_registrants

# Calculate metrics for the dashboard
total_registered = len(unique_registrants)
total_checked_in = len(actual_check_ins)
attendance_rate = (total_checked_in / total_registered) * 100 if total_registered > 0 else 0

print("\n")

# Task 5: Generate Event Check-in Analytics Report
print("=" * 50)
print(f"{'EVENT CHECK-IN ANALYTICS DASHBOARD':^50}")
print("=" * 50)
print(f"{'Metric':<28} | Count")
print("-" * 50)
print(f"{'Total Unique Registrations':<28} | {total_registered}")
print(f"{'Actual Check-ins':<28} | {total_checked_in}")
print(f"{'Absentees':<28} | {len(absentees)}")
print(f"{'VIP Guests Present':<28} | {len(vips_present)}")
print("-" * 50)
print(f"Attendance Rate              : {attendance_rate:.2f}%")
print("=" * 50)

# Optional print to demonstrate the boolean check from Task 4
print(f"\nRegistration check for '{normalized_email}': {is_registered}")
