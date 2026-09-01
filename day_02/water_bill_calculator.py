consumer_name = input("Enter consumer name: ")
units_consumed = float(input("Enter the number of units consumed: "))
if units_consumed <= 100:
    bill_amount = units_consumed * 5  # Rate for first 100 units
elif units_consumed <= 200:
    bill_amount = (100 * 5) + ((units_consumed - 100) * 7)  # Rate for next 100 units
else:
    bill_amount = (100 * 5) + (100 * 7) + ((units_consumed - 200) * 10)  # Rate for units above 200

print(f"\nConsumer Name: {consumer_name}")
print(f"Units Consumed: {units_consumed}")
print(f"Total Bill Amount: {bill_amount}")
