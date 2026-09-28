# Task 1: Create a nested dictionary for the inventory state
inventory = {
    101: {'name': 'Laptop', 'price': 800.00, 'stock': 10},
    102: {'name': 'Mouse', 'price': 25.00, 'stock': 45},
    103: {'name': 'Keyboard', 'price': 50.00, 'stock': 12}
}


# Task 3: Accept a purchase order, update stock, and validate
def process_purchase(item_id, quantity):
    """Validates and processes a transaction, updating inventory state."""
    if item_id in inventory and inventory[item_id]['stock'] >= quantity:
        inventory[item_id]['stock'] -= quantity
    else:
        print("Transaction Failed: Invalid ID or insufficient stock.")


# Simulating a purchase
process_purchase(101, 2)

# Task 2, 4, & 5: Filter low stock, calculate valuation, and print dashboard
LOW_STOCK_THRESHOLD = 10
total_valuation = 0.0
low_stock_count = 0

# Print Dashboard Header
print("=" * 50)
print(f"{'E-COMMERCE STOCK REPORT':^50}")
print("=" * 50)
print(f"{'ID':<4} | {'Name':<10} | {'Price (₹)':<9} | {'Stock':<5} | Status")
print("-" * 50)

# Iterate through the dictionary to aggregate data and format rows
for item_id, details in inventory.items():
    name = details['name']
    price = details['price']
    stock = details['stock']

    # Task 4: Accumulate total store inventory valuation
    total_valuation += (price * stock)

    # Task 2: Evaluate stock threshold using if-else logic
    if stock < LOW_STOCK_THRESHOLD:
        status = "LOW STOCK"
        low_stock_count += 1
    else:
        status = "IN STOCK"

    # Task 5: Print formatted row dynamically
    print(f"{item_id:<4} | {name:<10} | {price:<9.2f} | {stock:<5} | {status}")

# Print Dashboard Footer
print("-" * 50)
# Using ',.2f' formatting to automatically add commas to large floats
print(f"Total Inventory Valuation: ${total_valuation:,.2f}")
print(f"Low Stock Items Count    : {low_stock_count}")
print("=" * 50)