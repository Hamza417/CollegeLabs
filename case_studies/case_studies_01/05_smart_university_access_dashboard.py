from box_utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row
)


def generate_access_dashboard(user_name, role, id_valid):
    # ======= Access Validation Logic =======
    # Membership operator 'in' to check if role is authorized
    authorized_roles = ['Student', 'Faculty', 'Admin']
    is_authorized = role in authorized_roles

    # Boolean representation for ID validity is passed directly as `id_valid`

    # Determine if they have restricted area access (Assuming Admin only)
    restricted_area = (role == 'Admin') and id_valid

    # Final access determination combining compulsory conditions
    access_granted = is_authorized and id_valid

    # Determine Access Level string to display
    access_level = role.upper() if access_granted else "NONE"

    # ======= Dashboard UI Generation =======
    print()
    print_top_border()
    render_title("SMART ACCESS DASHBOARD")
    print_separator()

    render_row("User Name", user_name, 20)
    render_row("Role", role, 20)
    render_row("ID Card", "VALID" if id_valid else "INVALID", 20)
    print_separator()

    render_row("Authorized Role", "YES" if is_authorized else "NO", 20)
    render_row("ID Card Valid", "YES" if id_valid else "NO", 20)
    render_row("Restricted Area", "YES" if restricted_area else "NO", 20)
    render_row("Access Level", access_level, 20)
    print_separator()

    render_row("ACCESS STATUS", "GRANTED" if access_granted else "DENIED", 20)
    print_bottom_border()


def demonstrate_identity_vs_equality():
    """
    Demonstrates the difference between '==' (value equality) and 'is' (object identity).
    """
    print("\n" + "-" * 50)
    print("DEMONSTRATION: '==' vs 'is' Operator")
    print("-" * 50)

    a = [1, 2, 3]
    b = a  # b references the exact same list object in memory as a
    c = [1, 2, 3]  # c is a completely new list object in memory, with the same values

    print(f"List a: {a} (Memory address: {id(a)})")
    print(f"List b: {b} (Memory address: {id(b)})")
    print(f"List c: {c} (Memory address: {id(c)})\n")

    print("1. Equality (==) compares values:")
    print(f"   a == c : {a == c} (Because their contents are identical)")

    print("\n2. Identity (is) compares memory locations:")
    print(f"   a is b : {a is b} (Because they point to the exact same object)")
    print(f"   a is c : {a is c} (Because they point to different objects in memory)")
    print("-" * 50)


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (Valid Student):
       - Data: Role 'Student', ID Valid is True.
       - Expected: Authorized Role YES, Access GRANTED, Restricted Area NO.
       - Purpose: Validates the standard non-privileged access flow.

    Normal Case 2 (Unauthorized Role):
       - Data: Role 'Guest', ID Valid is True.
       - Expected: Authorized Role NO, Access DENIED.
       - Purpose: Verifies the `in` membership operator correctly filters out 
         roles not explicitly listed in the authorized_roles list.

    Edge Case (Admin with Invalid ID):
       - Data: Role 'Admin', ID Valid is False.
       - Expected: Authorized Role YES, but Access DENIED and Restricted Area NO.
       - Purpose: Tests that a highly privileged role cannot bypass the physical 
         ID card requirement. The `and` logic must strict-fail the entire transaction.
    """

    print("\nExecuting Test Case 1: Normal Case (Valid Student)")
    generate_access_dashboard("Rahul Sharma", "Student", True)

    print("\nExecuting Test Case 2: Normal Case (Unauthorized Role)")
    generate_access_dashboard("Anita Desai", "Guest", True)

    print("\nExecuting Test Case 3: Edge Case (Admin with Invalid ID)")
    generate_access_dashboard("Dr. Vivek Singh", "Admin", False)

    # Run the identity demonstration requested by the case study
    demonstrate_identity_vs_equality()
