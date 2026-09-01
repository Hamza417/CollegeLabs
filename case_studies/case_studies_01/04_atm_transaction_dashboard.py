from utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row
)


def generate_atm_dashboard(holder, balance, txn_type, amount, limit=20000):
    # ======= Transaction Validation Logic =======
    valid_txn_types = ['DEPOSIT', 'WITHDRAW', 'BALANCE']
    is_valid_type = txn_type in valid_txn_types

    # Initialize flags (defaulting to True for non-applicable transaction types)
    suff_balance = True
    within_limit = True
    is_positive = True

    if txn_type in ['WITHDRAW', 'DEPOSIT']:
        is_positive = amount > 0

    if txn_type == 'WITHDRAW':
        suff_balance = balance >= amount
        within_limit = amount <= limit

    if txn_type == 'BALANCE':
        amount = 0  # Force 0 for display consistency

    # Combine conditions based on strict requirements for approval
    is_approved = is_valid_type and is_positive and suff_balance and within_limit

    # ======= Balance Update =======
    prev_balance = balance
    if is_approved:
        if txn_type == 'WITHDRAW':
            balance -= amount  # Direct assignment update
        elif txn_type == 'DEPOSIT':
            balance += amount  # Direct assignment update

    # ======= Dashboard UI Generation =======
    print()
    print_top_border()
    render_title("ATM DASHBOARD")
    print_separator()

    render_row("Account Holder", holder, 22)
    render_row("Current Balance", f"₹ {prev_balance:,.2f}", 22)
    render_row("Transaction Type", txn_type, 22)
    render_row("Transaction Amount", f"₹ {amount:,.2f}", 22)
    print_separator()

    # N/A handling for deposits/balance inquiries to keep UI accurate
    display_suff = "YES" if suff_balance else "NO"
    display_limit = "YES" if within_limit else "NO"

    if txn_type != 'WITHDRAW':
        display_suff = "N/A"
        display_limit = "N/A"

    render_row("Sufficient Balance", display_suff, 22)
    render_row("Within Limit", display_limit, 22)
    render_row("Valid Amount", "YES" if is_positive else "NO", 22)
    print_separator()

    render_row("Transaction Status", "APPROVED" if is_approved else "DECLINED", 22)
    render_row("Previous Balance", f"₹ {prev_balance:,.2f}", 22)
    render_row("New Balance", f"₹ {balance:,.2f}", 22)
    print_bottom_border()


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (Valid Withdrawal):
       - Data: Balance ₹ 50,000, WITHDRAW ₹ 10,000. Limit is ₹ 20,000.
       - Expected: All checks YES. Status APPROVED. New balance ₹ 40,000.
       - Purpose: Validates the standard withdrawal flow and the `-=` operator.

    Normal Case 2 (Valid Deposit):
       - Data: Balance ₹ 5,000, DEPOSIT ₹ 15,000.
       - Expected: Valid Amount is YES. Status APPROVED. New balance ₹ 20,000.
       - Purpose: Verifies deposit logic ignores limit/sufficient balance checks 
         and correctly uses the `+=` operator.

    Normal Case 3 (Declined Withdrawal - Limit Exceeded):
       - Data: Balance ₹ 50,000, WITHDRAW ₹ 25,000. Limit is ₹ 20,000.
       - Expected: Within Limit is NO. Status DECLINED. Balance remains ₹ 50,000.
       - Purpose: Ensures the `and` logic correctly intercepts a single failure 
         (limit exceeded) even when funds are sufficient.

    Edge Case (Exact Maximum Constraints):
       - Data: Balance ₹ 20,000, WITHDRAW ₹ 20,000. Limit is ₹ 20,000.
       - Expected: All checks YES. Status APPROVED. New balance ₹ 0.
       - Purpose: Tests the inclusive boundaries (`<=` for limit, `>=` for balance). 
         If strict inequalities were used, this perfectly valid transaction would fail.
    """

    print("\nExecuting Test Case 1: Normal Case (Valid Withdrawal)")
    generate_atm_dashboard("John Doe", 50000, "WITHDRAW", 10000)

    print("\nExecuting Test Case 2: Normal Case (Valid Deposit)")
    generate_atm_dashboard("Jane Smith", 5000, "DEPOSIT", 15000)

    print("\nExecuting Test Case 3: Normal Case (Declined - Limit Exceeded)")
    generate_atm_dashboard("Mike Ross", 50000, "WITHDRAW", 25000)

    print("\nExecuting Test Case 4: Edge Case (Exact Maximum Constraints)")
    generate_atm_dashboard("Clark Kent", 20000, "WITHDRAW", 20000)
