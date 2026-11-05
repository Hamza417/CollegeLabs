subtotal = 0
total_items = 0

print("Enter product details. Type 'done' as the product name to finish.\n")

while True:
    product = input("Enter Product Name: ")

    if product.lower() == "done":
        break

    qty = int(input(f"Enter Quantity for {product}: "))

    if qty <= 0:
        print("Invalid quantity! Skipping to next item.\n")
        continue

    price = abs(float(input(f"Enter Price per unit for {product}: ")))

    subtotal += (qty * price)
    total_items += qty
    print(f"Item Added. Current Subtotal: {subtotal:.2F} Rs\n")

# Calculate discount based on subtotal tiers
if subtotal >= 5000:
    discount_rate = 0.10
elif subtotal >= 2500:
    discount_rate = 0.05
else:
    discount_rate = 0

discount_amount = subtotal * discount_rate
final_amount = subtotal - discount_amount

# Show the dashboard
print("\n")
print("=" * 50)
print(f"{'SUPERMARKET & SHOPPING MALL DASHBOARD':^50}")
print("=" * 50)
print(f"{'Total Items':<25}: {total_items}")
print(f"{'Subtotal':<25}: {subtotal:.2F} Rs")
print(f"{'Discount (' + str(int(discount_rate * 100)) + '%)':<25}: {discount_amount:.2F} Rs")
print("-" * 50)
print(f"{'Final Amount':<25}: {final_amount:.2F} Rs")
print("=" * 50)
