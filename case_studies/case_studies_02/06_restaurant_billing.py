# Task 1: Create a dictionary mapping integer item codes to menu items and prices
menu = {
    101: ("gourmet burger", 12.50),
    102: ("garlic fries", 5.00),
    103: ("soda", 2.50),
    104: ("chef salad", 9.00)
}

order_list = []

# Task 2: Collect order choices in a 'while' loop
# We simulate user input: (item_code, quantity) and 0 triggers the exit condition
# While the inputs are simulated, the while loop will terminate itself once 0 is entered.
simulated_inputs = [(101, 2), (102, 1), (103, 2), (0, 0)]
input_index = 0

while True:
    item_code, quantity = simulated_inputs[input_index]
    input_index += 1

    if item_code == 0:  # Exit condition
        break

    if item_code in menu:
        # Task 4: Standardize string formatting at the point of ingestion
        item_name = menu[item_code][0].title()
        unit_price = menu[item_code][1]

        # Calculate line item total
        line_total = unit_price * quantity

        # Store order as a tuple as requested (name, qty, unit, total)
        order_list.append((item_name, quantity, unit_price, line_total))
    else:
        print(f"Error: Item code {item_code} not found on the menu.")

# Task 3: Calculate subtotal, tax, and conditional discount
# Summing the 4th element (index 3) of every tuple in the list
subtotal = sum(item[3] for item in order_list)

tax_rate = 0.08
tax = subtotal * tax_rate

# Apply a $5 discount if subtotal exceeds $50 using if-else
if subtotal > 50.00:
    discount = 5.00
else:
    discount = 0.00

final_amount = subtotal + tax - discount

# Task 5: Print itemized Restaurant Customer Receipt Report
print("=" * 50)
print(f"{'GOURMET BISTRO RECEIPT':^50}")
print("=" * 50)
print(f"{'Item':<16} | {'Qty':<3} | {'Unit Price':<10} | {'Total ($)'}")
print("-" * 50)

# Unpacking the tuples directly in the loop signature
for item, qty, u_price, t_price in order_list:
    print(f"{item:<16} | {qty:<3} | ${u_price:<9.2f} | ${t_price:.2f}")

print("-" * 50)
print(f"{'Subtotal':<16} : ${subtotal:.2f}")

# Dynamically display the discount line only if it was applied
if discount > 0:
    print(f"{'Discount':<16} : -${discount:.2f}")

print(f"{'Tax (8%)':<16} : ${tax:.2f}")
print(f"{'Final Amount':<16} : ${final_amount:.2f}")
print("=" * 50)
