import re

name = input("Enter Applicant Name: ")
email = input("Enter Email Address: ")
mobile = input("Enter Mobile Number: ")
app_id = input("Enter Application ID (e.g., APP1234): ")

# Validate using Regular Expressions
email_valid = bool(re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email))
mobile_valid = bool(re.match(r'^[6-9]\d{9}$', mobile))
app_id_valid = bool(re.match(r'^APP\d{4}$', app_id))

# Determine final status
status = "ACCEPTED" if email_valid and mobile_valid and app_id_valid else "RECHECK DETAILS"

# Show the dashboard
print("\n")
print("=" * 50)
print(f"{'UNIVERSITY ADMISSION DASHBOARD':^50}")
print("=" * 50)
print(f"{'Applicant Name':<25}: {name}")
print("-" * 50)
print(f"{'Email Status':<25}: {'VALID' if email_valid else 'INVALID'}")
print(f"{'Mobile Status':<25}: {'VALID' if mobile_valid else 'INVALID'}")
print(f"{'Application ID Status':<25}: {'VALID' if app_id_valid else 'INVALID'}")
print("-" * 50)
print(f"{'Application Status':<25}: {status}")
print("=" * 50)
