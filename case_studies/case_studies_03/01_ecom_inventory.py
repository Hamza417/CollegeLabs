# Constants
INVENTORY = {
    101: {'name': 'Laptop', 'price': 800.00, 'stock': 10},
    102: {'name': 'Mouse', 'price': 25.00, 'stock': 45},
    103: {'name': 'Keyboard', 'price': 50.00, 'stock': 12}
}

LOW_STOCK_THRESHOLD = 10

# Declare the variables
print(f"Available Item IDs: {list(INVENTORY.keys())}")
purchase_id = int(input("Enter Item ID to purchase: "))
purchase_quantity = int(input("Enter Quantity: "))
transaction_status = ""
total_valuation = 0.0
low_stock_count = 0

# Evaluate the transaction and update stock
if purchase_id in INVENTORY and INVENTORY[purchase_id]['stock'] >= purchase_quantity:
    INVENTORY[purchase_id]['stock'] -= purchase_quantity
    transaction_status = "Successful"
else:
    transaction_status = "Failed (Invalid ID or Insufficient Stock)"

# Calculate final store valuation and low stock count
for details in INVENTORY.values():
    total_valuation += (details['price'] * details['stock'])
    if details['stock'] < LOW_STOCK_THRESHOLD:
        low_stock_count += 1

# Show the dashboard
print()
print("=" * 55)
print(f"{'E-COMMERCE STOCK REPORT':^55}")
print("=" * 55)
print(f"{'Recent Transaction':<20}: {transaction_status}")
print("-" * 55)
print(f"{'ID':<6} | {'Name':<12} | {'Price ($)':<9} | {'Stock':<5} | Status")
print("-" * 55)

# Iterate through the dictionary to format dashboard rows
for item_id, details in INVENTORY.items():
    name = details['name']
    price = details['price']
    stock = details['stock']
    status = "LOW STOCK" if stock < LOW_STOCK_THRESHOLD else "IN STOCK"

    print(f"{item_id:<6} | {name:<12} | {price:<9.2f} | {stock:<5} | {status}")

print("-" * 55)
print(f"{'Total Inventory Valuation':<26}: ${total_valuation:,.2f}")
print(f"{'Low Stock Items Count':<26}: {low_stock_count}")
print("=" * 55)
