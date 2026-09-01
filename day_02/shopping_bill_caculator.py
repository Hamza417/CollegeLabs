item_name = input("Enter the item name: ")
quantity = int(input("Enter the quantity of the item: "))
unit_price = float(input("Enter the unit price of the item: "))
total_price = quantity * unit_price

print(f"\nItem Name: {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: {unit_price}")
print(f"Total Price: {total_price}")