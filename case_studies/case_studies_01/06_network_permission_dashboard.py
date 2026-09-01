from utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row,
    render_table_header,
    render_table_row
)


def generate_permission_dashboard(name, role, current_perms):
    # ======= Bitwise Permission Logic =======
    # Define the binary flags as given in the problem statement
    READ = 1  # 001 in binary
    WRITE = 2  # 010 in binary
    EXECUTE = 4  # 100 in binary

    # Check permissions using Bitwise AND (&)
    has_read = bool(current_perms & READ)
    has_write = bool(current_perms & WRITE)
    has_execute = bool(current_perms & EXECUTE)

    # Calculate binary representation for display
    # bin() returns e.g., '0b101', so we slice [2:] and zfill to ensure 3 digits
    binary_val = bin(current_perms)[2:].zfill(3)

    # ======= Dashboard UI Generation =======
    print()
    print_top_border()
    render_title("NETWORK PERMISSION DASHBOARD")
    print_separator()

    render_row("User Name", name, 18)
    render_row("User Role", role, 18)
    print_separator()

    render_table_header("Permission", "Binary", "Status")
    print_separator()

    render_table_row("READ", "001", "ALLOWED" if has_read else "DENIED")
    render_table_row("WRITE", "010", "ALLOWED" if has_write else "DENIED")
    render_table_row("EXECUTE", "100", "ALLOWED" if has_execute else "DENIED")
    print_separator()

    render_row("Permission Value", current_perms, 18)
    render_row("Binary Value", binary_val, 18)
    print_bottom_border()


def demonstrate_bitwise_operators():
    """
    Demonstrates the functionality of specific operators requested in the case study.
    """
    READ, WRITE, EXECUTE = 1, 2, 4

    print("\n" + "-" * 60)
    print("DEMONSTRATION: Bitwise & Logical Operators")
    print("-" * 60)

    print("1. Combining Permissions (|):")
    combined = READ | WRITE
    print(f"   READ (1) | WRITE (2) = {combined} (Binary: {bin(combined)[2:].zfill(3)})")

    print("\n2. 'and' (Logical) vs '&' (Bitwise):")
    print(f"   Logical (1 and 2): {1 and 2} (Evaluates truthiness, returns the second true value)")
    print(f"   Bitwise (1 & 2)  : {1 & 2} (Evaluates bits: 001 & 010 = 000)")

    print("\n3. Bitwise XOR (^):")
    print(f"   Returns 1 if bits are different, 0 if same.")
    print(f"   (READ | WRITE) ^ WRITE = {combined ^ WRITE} (Toggles WRITE off)")

    print("\n4. Bitwise Shifts (<<, >>):")
    print(f"   Left shift multiplies by 2: READ (1) << 1 = {READ << 1} (Which is WRITE)")
    print(f"   Right shift divides by 2: EXECUTE (4) >> 1 = {EXECUTE >> 1} (Which is WRITE)")
    print("-" * 60)


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (Multiple Permissions):
       - Data: Permission Value 6 (which is WRITE | EXECUTE)
       - Expected: READ is DENIED, WRITE is ALLOWED, EXECUTE is ALLOWED. Binary is 110.
       - Purpose: Validates that bitwise AND correctly extracts multiple independent 
         flags from a combined integer.

    Normal Case 2 (Single Permission):
       - Data: Permission Value 1 (READ only)
       - Expected: READ is ALLOWED, others DENIED. Binary is 001.
       - Purpose: Verifies standard single-flag extraction.

    Edge Case (Zero Permissions):
       - Data: Permission Value 0
       - Expected: All DENIED. Binary is 000.
       - Purpose: Tests the absolute boundary where no flags are set, ensuring 
         evaluations gracefully resolve to False/DENIED without errors.
    """

    print("\nExecuting Test Case 1: Normal Case (WRITE + EXECUTE)")
    generate_permission_dashboard("DevOps Team", "Admin", 6)

    print("\nExecuting Test Case 2: Normal Case (READ Only)")
    generate_permission_dashboard("Alice Smith", "Guest", 1)

    print("\nExecuting Test Case 3: Edge Case (No Permissions)")
    generate_permission_dashboard("Banned User", "None", 0)

    demonstrate_bitwise_operators()
