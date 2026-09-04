from box_utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row 
)


def render_custom_line(text):
    """Renders a custom formatted string within the dashboard borders."""
    print(f"│{text.ljust(58)}│")


def generate_cafeteria_dashboard(name, s_id, category, item, qty, coupon, balance):
    # ======= Data Dictionaries =======
    menu = {'Burger': 150, 'Pizza': 250, 'Coffee': 50, 'Sandwich': 100}
    valid_coupons = {'WELCOME50': 50, 'LUNCH20': 20}

    # ======= Validation & Calculations =======
    # Membership operator to check item availability
    item_available = item in menu
    price = menu.get(item, 0)

    # Arithmetic operators for subtotal
    subtotal = price * qty

    # Comparison and arithmetic for discounts
    student_discount = subtotal * 0.15 if category == 'Student' else 0

    # Membership for coupon validation
    coupon_valid = coupon in valid_coupons
    coupon_discount = valid_coupons.get(coupon, 0) if coupon_valid else 0

    # Logical operators for delivery charge (e.g., charge 30 if order is small)
    delivery_charge = 30 if (200 > subtotal > 0) else 0

    # Operator precedence demonstration: price * quantity - discounts + delivery
    final_amount = subtotal - student_discount - coupon_discount + delivery_charge
    final_amount = max(0, final_amount)  # Prevent negative bill

    # Comparison operator for balance
    sufficient_balance = balance >= final_amount

    # Logical 'and' to combine multiple conditions for final status
    is_confirmed = item_available and sufficient_balance

    # Assignment operator '-=' to update balance if confirmed
    if is_confirmed:
        balance -= final_amount

    # ======= Dashboard UI Generation =======
    print()
    print_top_border()
    render_title("SMART UNIVERSITY CAFETERIA")
    print_separator()

    # Custom multi-column headers
    student_info = f" STUDENT: {name:<12} ID: {s_id:<6} Category: {category}"
    order_info = f" ORDER: {item:<14} Qty: {qty:<4} Price: ₹ {price:,.2f}"
    render_custom_line(student_info)
    render_custom_line(order_info)
    print_separator()

    render_title("BILL")
    render_row("Subtotal", f"₹ {subtotal:,.2f}", 20)
    render_row("Student Discount", f"₹ {student_discount:,.2f}", 20)
    render_row("Coupon Discount", f"₹ {coupon_discount:,.2f}", 20)
    render_row("Delivery Charge", f"₹ {delivery_charge:,.2f}", 20)
    print_separator()

    render_row("FINAL AMOUNT", f"₹ {final_amount:,.2f}", 20)
    render_row("Menu Item", "✓ AVAILABLE" if item_available else "X UNAVAILABLE", 20)
    render_row("Coupon", "✓ VALID" if coupon_valid else "X INVALID", 20)
    render_row("Balance", "✓ SUFFICIENT" if sufficient_balance else "X INSUFFICIENT", 20)
    print_separator()

    # Ternary operator for final status
    final_status = "ORDER CONFIRMED" if is_confirmed else "ORDER REJECTED"
    render_title(final_status)
    print_bottom_border()


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (Successful Student Order):
       - Data: Student, Burger, Qty 2, Coupon 'LUNCH20', Balance ₹ 500.
       - Expected: Subtotal 300. Student discount applies (15% = 45). Coupon applies (20). 
                   Delivery is free (subtotal > 200). Final: 300 - 45 - 20 = 235.
                   Order CONFIRMED. Balance updated to ₹ 265.
       - Purpose: Validates the happy path where all conditions are met and 
         multiple discounts apply correctly via operator precedence.

    Normal Case 2 (Failed Order - Insufficient Funds):
       - Data: Faculty, Pizza, Qty 3, Coupon 'NONE', Balance ₹ 200.
       - Expected: Subtotal 750. No student discount. Delivery free. Final: 750.
                   Balance (200) < Final (750), so SUFFICIENT is X.
                   Order REJECTED. Balance remains ₹ 200.
       - Purpose: Verifies that the balance comparison (`>=`) correctly halts the 
         order confirmation and protects the balance from dipping below zero.

    Edge Case (Exact Zero Balance After Purchase):
       - Data: Student, Coffee, Qty 1, Coupon 'NONE', Balance ₹ 72.50.
       - Expected: Subtotal 50. Discount 7.50. Delivery 30. Final: 72.50.
                   Balance equals final amount. 
                   Order CONFIRMED. New balance ₹ 0.00.
       - Purpose: Tests the strict boundaries of small-order delivery fees and 
         the inclusive `>=` balance check, ensuring valid exact-change orders succeed.
    """

    print("\nExecuting Test Case 1: Normal Case (Successful Student Order)")
    generate_cafeteria_dashboard("Pooja M.", "ST01", "Student", "Burger", 2, "LUNCH20", 500.0)

    print("\nExecuting Test Case 2: Normal Case (Failed - Insufficient Funds)")
    generate_cafeteria_dashboard("Prof. Rao", "FA42", "Faculty", "Pizza", 3, "NONE", 200.0)

    print("\nExecuting Test Case 3: Edge Case (Exact Zero Balance Output)")
    generate_cafeteria_dashboard("Rahul S.", "ST09", "Student", "Coffee", 1, "NONE", 72.50)
