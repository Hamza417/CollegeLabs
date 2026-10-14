# Constants
MENU = {
    101: ("gourmet burger", 12.50),
    102: ("garlic fries", 5.00),
    103: ("soda", 2.50),
    104: ("chef salad", 9.00)
}
TAX_RATE = 0.08
DISCOUNT_THRESHOLD = 50.00
DISCOUNT_AMOUNT = 5.00

# Declare the variables and collect input
raw_order = []
print(f"Available Menu Codes: {list(MENU.keys())} (Enter 0 to finish)")

while True:
    item_code = int(input("Enter Item Code: "))
    if item_code == 0:
        break

    if item_code in MENU:
        quantity = int(input(f"Enter Quantity for {MENU[item_code][0].title()}: "))
        raw_order.append((item_code, quantity))
    else:
        print(f"Error: Item code {item_code} not found on the menu. Try again.")

# Evaluate the order
processed_items = []
subtotal = 0.0

for code, qty in raw_order:
    item_name = MENU[code][0].title()
    unit_price = MENU[code][1]
    line_total = unit_price * qty

    # Store processed data for the dashboard
    processed_items.append((item_name, qty, unit_price, line_total))
    subtotal += line_total

tax = subtotal * TAX_RATE
discount = DISCOUNT_AMOUNT if subtotal > DISCOUNT_THRESHOLD else 0.00
final_amount = subtotal + tax - discount

# Show the dashboard
print()
print("=" * 55)
print(f"{'GOURMET BISTRO RECEIPT':^55}")
print("=" * 55)
print(f"{'Item':<18} | {'Qty':<4} | {'Unit Price':<11} | {'Total ($)'}")
print("-" * 55)

# Unpack the processed items to display rows
for item, qty, u_price, t_price in processed_items:
    print(f"{item:<18} | {qty:<4} | ${u_price:<10.2f} | ${t_price:.2f}")

print("-" * 55)
print(f"{'Subtotal':<25}: ${subtotal:.2f}")

# Dynamically display the discount line only if it was applied
if discount > 0:
    print(f"{'Discount':<25}: -${discount:.2f}")

print(f"{'Tax (8%)':<25}: ${tax:.2f}")
print(f"{'Final Amount':<25}: ${final_amount:.2f}")
print("=" * 55)