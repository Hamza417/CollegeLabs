# Constants
RAW_REGISTRATIONS = [
    "adib@email.com", "adim@email.com", "aysha@email.com",
    "saima@email.com", "shifa@email.com", "hassan@email.com",
    "riyaz@email.com", "mobasshara@email.com", "adib@email.com"
]
ACTUAL_CHECK_INS_LIST = [
    "adib@email.com", "aysha@email.com", "saima@email.com", "hassan@email.com", "riyaz@email.com"
]
VIP_LIST = {
    "adib@email.com", "riyaz@email.com", "hassan@email.com", "aysha@email.com"
}

# Declare the variables
search_email = ""

# Validate the entered email ID format
while not search_email:
    search_email = input("Enter email to check registration: ").strip()
    if search_email.split("@")[-1] not in ["email.com", "gmail.com"]:
        print("Invalid email domain. Please enter a valid email address.")
        search_email = ""

# Evaluate the sets and analytics
normalized_email = search_email.lower().strip()

# Convert raw lists into Sets to automatically extract unique values
unique_registrants = set(RAW_REGISTRATIONS)
actual_check_ins = set(ACTUAL_CHECK_INS_LIST)

# Perform set operations for insights
vips_present = actual_check_ins.intersection(VIP_LIST)
absentees = unique_registrants.difference(actual_check_ins)

# Boolean check using the 'in' operator (O(1) time complexity in a set)
is_registered = normalized_email in unique_registrants

# Calculate metrics
total_registered = len(unique_registrants)
total_checked_in = len(actual_check_ins)
attendance_rate = (total_checked_in / total_registered) * 100 if total_registered > 0 else 0

# Show the dashboard
print()
print("=" * 55)
print(f"{'EVENT CHECK-IN ANALYTICS DASHBOARD':^55}")
print("=" * 55)
print(f"{'Metric':<30} | Count")
print("-" * 55)
print(f"{'Total Unique Registrations':<30} | {total_registered}")
print(f"{'Actual Check-ins':<30} | {total_checked_in}")
print(f"{'Absentees':<30} | {len(absentees)}")
print(f"{'VIP Guests Present':<30} | {len(vips_present)}")
print("-" * 55)
print(f"{'Attendance Rate':<30}: {attendance_rate:.2f}%")
print(f"{'Lookup: ' + normalized_email:<30}: {'Registered' if is_registered else 'Not Registered'}")
print("=" * 55)