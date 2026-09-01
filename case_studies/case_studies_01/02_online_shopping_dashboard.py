from utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row
)


def generate_shopping_dashboard(product, quantity, price, coupon_code):
    # ======= Billing Calculations =======
    # Calculate subtotal
    subtotal = price * quantity

    # Check 10% discount eligibility
    base_discount = subtotal * 0.10 if subtotal >= 5000 else 0

    # Coupon validation
    valid_coupons = ['SAVE200', 'FESTIVAL500']
    is_coupon_valid = coupon_code in valid_coupons

    coupon_discount = 0
    if is_coupon_valid:
        coupon_discount = 200 if coupon_code == 'SAVE200' else 500

    # Calculate amount before delivery to determine delivery eligibility
    discounted_amount = subtotal - base_discount - coupon_discount
    discounted_amount = max(0, discounted_amount)  # Prevent negative bill

    # Delivery charge calculation
    is_delivery_free = discounted_amount >= 3000
    delivery_charge = 0 if is_delivery_free else 150

    # Final amount calculation
    final_amount = discounted_amount + delivery_charge

    # Order validation (simple check to ensure valid quantities/prices)
    is_confirmed = quantity > 0 and price > 0

    # ======= Dashboard UI Generation =======
    print()
    print_top_border()
    render_title("ONLINE SHOPPING DASHBOARD")
    print_separator()

    # Label width increased to 20 to accommodate longer labels like "Coupon Discount"
    render_row("Product", product, 20)
    render_row("Quantity", quantity, 20)
    render_row("Price per Item", f"₹ {price:,.2f}", 20)
    render_row("Coupon Code", coupon_code, 20)
    print_separator()

    render_row("Subtotal", f"₹ {subtotal:,.2f}", 20)
    render_row("Discount", f"₹ {base_discount:,.2f}", 20)
    render_row("Coupon Discount", f"₹ {coupon_discount:,.2f}", 20)
    render_row("Delivery Charge", f"₹ {delivery_charge:,.2f}", 20)
    print_separator()

    render_row("Final Amount", f"₹ {final_amount:,.2f}", 20)
    render_row("Coupon Status", "VALID" if is_coupon_valid else "INVALID", 20)
    render_row("Delivery Status", "FREE" if is_delivery_free else "CHARGED", 20)
    render_row("Order Status", "CONFIRMED" if is_confirmed else "REJECTED", 20)
    print_bottom_border()


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (High Value Order):
       - Data: Smartphone, Qty 1, Price ₹ 15000, Coupon: 'FESTIVAL500'
       - Expected: Subtotal >= 5000 (triggers 10% discount). Coupon is VALID (triggers ₹ 500 discount). 
                   Final amount > 3000 (triggers FREE delivery).
       - Purpose: Validates all discount logic and free delivery logic applying concurrently.

    Normal Case 2 (Low Value Order):
       - Data: Wireless Mouse, Qty 2, Price ₹ 800, Coupon: 'INVALID123'
       - Expected: Subtotal is ₹ 1600 (No 10% discount). Coupon is INVALID. 
                   Final amount < 3000 (triggers ₹ 150 CHARGED delivery).
       - Purpose: Verifies the fallback constraints when no thresholds are met.

    Edge Case (Exact Discount Threshold):
       - Data: Office Chair, Qty 1, Price ₹ 5000, Coupon: 'NONE'
       - Expected: Subtotal is exactly ₹ 5000. 10% discount MUST apply because the rule 
                   is `>= 5000`. Discounted total is ₹ 4500, which still qualifies for FREE delivery.
       - Purpose: Tests the strict lower boundary of the 10% discount rule to ensure the 
                   inclusive `>=` operator is functioning correctly.
    """

    print("\nExecuting Test Case 1: Normal Case (High Value Order)")
    generate_shopping_dashboard("Smartphone", 1, 15000, "FESTIVAL500")

    print("\nExecuting Test Case 2: Normal Case (Low Value Order)")
    generate_shopping_dashboard("Wireless Mouse", 2, 800, "INVALID123")

    print("\nExecuting Test Case 3: Edge Case (Exact Discount Threshold)")
    generate_shopping_dashboard("Office Chair", 1, 5000, "NONE")
