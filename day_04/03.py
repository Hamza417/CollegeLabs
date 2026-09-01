def collect_bill_input():
    """Prompts the user for customer details, item names, unit prices, and quantities.

    Validates numeric inputs for prices and quantities to prevent runtime errors.

    Returns:
        tuple: A tuple containing:
            - customer_name (str): The name of the customer.
            - items (list[dict]): A list of dicts containing item details ('name', 'price', 'qty').
    """
    customer_name = input("Customer Name: ").strip()

    items = []
    for i in range(1, 4):
        print(f"\n--- Enter Item {i} Details ---")
        name = input(f"Item {i} Name: ").strip()

        # Validate numeric price input
        while True:
            try:
                price = float(input(f"Item {i} Price: "))
                if price < 0:
                    print("Price cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a numeric price.")

        # Validate integer quantity input
        while True:
            try:
                qty = int(input(f"Item {i} Quantity: "))
                if qty < 0:
                    print("Quantity cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for quantity.")

        items.append({"name": name, "price": price, "qty": qty})

    return customer_name, items


def calculate_bill_metrics(items):
    """Calculates total amount per item and the grand total for the bill.

    Args:
        items (list[dict]): List of item dictionaries with 'price' and 'qty'.

    Returns:
        tuple: A tuple containing:
            - items (list[dict]): Updated items list including calculated 'amount'.
            - total_bill (float): The grand total bill amount.
    """
    total_bill = 0.0
    for item in items:
        item["amount"] = item["price"] * item["qty"]
        total_bill += item["amount"]

    return items, total_bill


def format_restaurant_bill(customer_name, items, total_bill):
    """Formats the bill data into a dynamic, vertically aligned receipt format.

    Dynamically aligns colons and adjusts border width based on maximum content length.

    Args:
        customer_name (str): Customer's name.
        items (list[dict]): Processed item dictionaries with names, quantities, and amounts.
        total_bill (float): Calculated grand total.

    Returns:
        str: Fully formatted, multi-line bill string.
    """
    # Group data into logical display sections
    sections = [
        {"Customer Name": customer_name}
    ]

    for i, item in enumerate(items, 1):
        sections.append({
            f"Item {i}": item["name"],
            "Quantity": str(item["qty"]),
            "Amount": f"{item['amount']:.2f}"
        })

    sections.append({"Total Bill": f"{total_bill:.2f}"})

    # Determine maximum label width across all keys to align colons
    all_keys = [key for section in sections for key in section]
    max_key_len = max(len(key) for key in all_keys)

    # Build key-value line strings with dynamic field padding
    lines = []
    for idx, section in enumerate(sections):
        for key, val in section.items():
            lines.append(f"{key:<{max_key_len}} : {val}")
        # Insert blank line separator between sections (except the last section)
        if idx < len(sections) - 1:
            lines.append("")

    # Dynamically scale border width based on maximum content length
    title = "RESTAURANT BILL"
    max_line_len = max(len(line) for line in lines)
    border_width = max(max_line_len, len(title) + 8)

    # Construct dynamic top header and bottom border
    header = f" {title} ".center(border_width, "=")
    footer = "=" * border_width

    return "\n".join([header] + lines + [footer])


def main():
    customer_name, items = collect_bill_input()
    items, total_bill = calculate_bill_metrics(items)
    bill = format_restaurant_bill(customer_name, items, total_bill)

    print("\n" + bill)


if __name__ == "__main__":
    main()