from box_utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row
)


def generate_eligibility_dashboard(name, attendance, internal_marks, assignment_submitted, fees_paid):
    # ======= Eligibility Calculations =======
    # Evaluate numeric conditions using comparison operators
    att_ok = attendance >= 75
    int_ok = internal_marks >= 40

    # Combine all conditions using the logical 'and' operator
    # If any single condition here evaluates to False, the entire expression becomes False.
    is_eligible = att_ok and int_ok and assignment_submitted and fees_paid

    # ======= Dashboard UI Generation =======
    # Using the ternary operator heavily here to quickly toggle display strings
    # based on boolean states, keeping the code clean and fast.
    print()
    print_top_border()
    render_title("EXAMINATION ELIGIBILITY DASHBOARD")
    print_separator()

    render_row("Student Name", name, 20)
    render_row("Attendance", f"{attendance}%", 20)
    render_row("Internal Marks", f"{internal_marks}%", 20)
    render_row("Assignment", "SUBMITTED" if assignment_submitted else "NOT SUBMITTED", 20)
    render_row("Fees", "PAID" if fees_paid else "NOT PAID", 20)
    print_separator()

    # Validation checkboxes layer
    render_row("Attendance", "✓" if att_ok else "X", 20)
    render_row("Academic Criteria", "✓" if int_ok else "X", 20)
    render_row("Assignment", "✓" if assignment_submitted else "X", 20)
    render_row("Fee Status", "✓" if fees_paid else "X", 20)
    print_separator()

    render_row("EXAMINATION STATUS", "ELIGIBLE" if is_eligible else "NOT ELIGIBLE", 20)
    print_bottom_border()


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (All Requirements Met):
       - Data: 85% attendance, 60% internal marks, assignment submitted (True), fees paid (True).
       - Expected: All checks pass (✓), Status is ELIGIBLE.
       - Purpose: Validates that when all operands in the `and` chain are True, the 
         final result is True.

    Normal Case 2 (Missing Administrative Requirement):
       - Data: 90% attendance, 70% internal marks, assignment submitted (True), fees paid (False).
       - Expected: Academic checks pass (✓), Fee check fails (X). Status is NOT ELIGIBLE.
       - Purpose: Verifies that a single False condition (unpaid fees) collapses the 
         entire `and` expression, accurately reflecting strict university policies.

    Edge Case (Exact Threshold Boundaries):
       - Data: Exactly 75% attendance, Exactly 40% internal marks, assignment submitted, fees paid.
       - Expected: All checks pass (✓), Status is ELIGIBLE.
       - Purpose: Tests the inclusive `>=` comparison operators. If we accidentally used 
         strictly greater than (`>`), this valid student would be falsely rejected.
    """

    print("\nExecuting Test Case 1: Normal Case (All Requirements Met)")
    generate_eligibility_dashboard("Vikram Singh", 85, 60, True, True)

    print("\nExecuting Test Case 2: Normal Case (Missing Administrative Requirement)")
    generate_eligibility_dashboard("Neha Patel", 90, 70, True, False)

    print("\nExecuting Test Case 3: Edge Case (Exact Threshold Boundaries)")
    generate_eligibility_dashboard("Arjun Nair", 75, 40, True, True)
