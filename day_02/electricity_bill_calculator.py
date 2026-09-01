consumer_name = input("Enter consumer name: ")
units_consumed = float(input("Enter the number of units consumed: "))

COST_OF_UNIT = 5.0  # Cost per unit in currency
COST_OF_UNIT_EXCESS = 7.0  # Cost per unit for excess consumption in currency
COST_OF_UNIT_ABOVE_THRESHOLD = 10.0  # Cost per unit for consumption above threshold in currency

if units_consumed <= 100:
    bill_amount = units_consumed * COST_OF_UNIT  # Rate for first 100 units
elif units_consumed <= 200:
    bill_amount = (100 * COST_OF_UNIT) + ((units_consumed - 100) * COST_OF_UNIT_EXCESS)  # Rate for next 100 units
else:
    bill_amount = ((100 * COST_OF_UNIT) + (100 * COST_OF_UNIT_EXCESS)
                   + ((units_consumed - 200) * COST_OF_UNIT_ABOVE_THRESHOLD))  # Rate for units above 200

print(f"\nConsumer Name: {consumer_name}")
print(f"Units Consumed: {units_consumed}")
print(f"Total Bill Amount: {bill_amount}")
