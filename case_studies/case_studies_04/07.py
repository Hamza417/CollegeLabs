def calculate_item_amount(price, qty):
    """Calculates the total amount for a specific item based on quantity."""
    return price * qty


def calculate_tax(amount, rate=5):
    """Calculates the tax on the given amount with a default rate of 5%."""
    return amount * rate / 100


def show_dashboard(table_no, subtotal, tax_amount):
    """Displays the final restaurant order dashboard."""
    total = subtotal + tax_amount

    print("\n")
    print("=" * 50)
    print(f"{'RESTAURANT ORDER DASHBOARD':^50}")
    print("=" * 50)
    print(f"{'Table No':<25}: {table_no}")
    print("-" * 50)
    print(f"{'Subtotal':<25}: {subtotal:.2F} Rs")
    print(f"{'Tax (5%)':<25}: {tax_amount:.2F} Rs")
    print("-" * 50)
    print(f"{'Total Amount':<25}: {total:.2F} Rs")
    print("=" * 50)


# Main Execution
menu = {
    "Biryani": 250,
    "Juice": 80,
    "Dessert": 120,
    "Coffee": 60
}

table_number = input("Enter Table No: ")
current_subtotal = 0

print("\nEnter quantities for the menu items (enter 0 if none):")
for item, price in menu.items():
    quantity = int(input(f"Enter quantity for {item} (Price: {price} Rs): "))
    current_subtotal += calculate_item_amount(price, quantity)

calculated_tax = calculate_tax(current_subtotal)

show_dashboard(table_number, current_subtotal, calculated_tax)
