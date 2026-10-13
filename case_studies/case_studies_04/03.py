# Constants
ROOMS = {"AC": 2500, "General": 1000}

# Declare the variables
patient_id = input("Enter Patient ID: ")
name = input("Enter Patient Name: ").title()
room_type = input("Enter Room Type (AC, General): ")
no_of_days = int(input("Enter No of Days Room was Booked for: "))
doctor_fee = int(input("Enter Doctor Fee: "))
diagnostics_charges = int(input("Enter Diagnostics Charges: "))
medicine_charges = int(input("Enter Medicine Charges: "))
discount = 0

# Evaluate the amount
room_cost = ROOMS[room_type] * no_of_days
total_bill = doctor_fee + room_cost + medicine_charges + diagnostics_charges

# Calculate the discount percentage based on the bill
if total_bill >= 20000:
    discount = 0.10
elif total_bill >= 10000:
    discount = 0.05
else:
    discount = 0

calculated_discount = total_bill * discount

# Show the dashboard

print()
print("=" * 50)
print(f"{'HOSPITAL BILL DASHBOARD':^50}")
print("=" * 50)
print(f"{'Patient ID':<25}: {patient_id}")
print(f"{'Patient Name':<25}: {name}")
print(f"{'Room Type':<25}: {ROOMS[room_type]}")
print(f"{'Stayed For':<25}: {no_of_days} Days")
print("-" * 50)
print(f"{'Doctor Fee':<25}: {doctor_fee} Rs")
print(f"{'Diagnostic Charges':<25}: {diagnostics_charges} Rs")
print(f"{'Room Charges':<25}: {room_cost} Rs")
print("-" * 50)
print(f"{'Total Bill':<25}: {total_bill} Rs")
print(f"{'Discount':<25}: {discount * 100}%")
print(f"{'Net Bill':<25}: {total_bill - calculated_discount} Rs")
print("=" * 50)
