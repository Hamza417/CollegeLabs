import re

name = input("Applicant: ")
email = input("Email: ")
mobile = input("Mobile: ")
app = input("Application ID (APP1234): ")
email_ok = bool(re.match(r'^[\w.-]+@[\w.-]+\.\w+$', email))
mobile_ok = bool(re.match(r'^[6-9]\d{9}$', mobile))
app_ok = bool(re.match(r'^APP\d{4}$', app))
status = "ACCEPTED" if email_ok and mobile_ok and app_ok else "RECHECK DETAILS"
print("\n===================================")
print("   UNIVERSITY ADMISSION DASHBOARD")
print("===================================")
print("Applicant:", name)
print("Email:", "VALID" if email_ok else "INVALID")
print("Mobile:", "VALID" if mobile_ok else "INVALID")
print("Application ID:", "VALID" if app_ok else "INVALID")
print("Application:", status)
print("===================================")
