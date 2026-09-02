from box_utils import (
    print_top_border,
    print_bottom_border,
    print_separator,
    render_title,
    render_row,
    render_marks
)


def generate_student_dashboard(name, student_id, internal, assignment, midterm, endsem, attendance):
    # ======= Academic Calculations =======
    total_marks = internal + assignment + midterm + endsem
    max_marks = 20 + 15 + 25 + 50  # 110 total
    percentage = (total_marks / max_marks) * 100

    if percentage >= 90:
        grade = 'O'
    elif percentage >= 80:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 60:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'

    # ======= Status Calculations =======
    is_eligible = attendance >= 75
    is_pass = (percentage >= 40) and is_eligible

    # ======= Dashboard UI Generation =======
    print()
    print_top_border()
    render_title("STUDENT RESULT DASHBOARD")
    print_separator()

    render_row("Student Name", name)
    render_row("Student ID", student_id)
    print_separator()

    render_marks("Internal Marks", internal, 20)
    render_marks("Assignment Marks", assignment, 15)
    render_marks("Mid-Term Marks", midterm, 25)
    render_marks("End-Semester", endsem, 50)
    print_separator()

    render_row("Total Marks", total_marks)
    render_row("Percentage", f"{percentage:.2f}%")
    render_row("Grade", grade)
    render_row("Attendance", f"{attendance}%")
    print_separator()

    render_row("Examination Status", "ELIGIBLE" if is_eligible else "NOT ELIGIBLE")
    render_row("Final Result", "PASS" if is_pass else "FAIL")
    print_bottom_border()


# ======= Execution & Test Cases =======
if __name__ == "__main__":
    """
    TEST CASES DOCUMENTATION:

    Normal Case 1 (Good Standing):
       - Data: High marks across the board, 85% attendance.
       - Expected: ELIGIBLE status, high percentage, PASS result. 
       - Purpose: Validates the standard "happy path" logic and arithmetic.

    Normal Case 2 (Academic Failure):
       - Data: Low marks (38/110 total), 80% attendance.
       - Expected: ELIGIBLE (due to >=75% attendance) but FAIL (marks < 40%).
       - Purpose: Verifies that passing the attendance check does not bypass the 
         academic grade requirements.

    Edge Case (Strict Boundary Failure):
       - Data: Near-perfect marks (108/110), but exactly 74% attendance.
       - Expected: NOT ELIGIBLE (74% < 75%), resulting in a forced FAIL.
       - Purpose: Tests the strict lower boundary of the eligibility threshold.
         Ensures high academic performance cannot override attendance prerequisites.
    """

    print("\nExecuting Test Case 1: Normal Case (Good Standing)")
    generate_student_dashboard("Rahul Sharma", "CS042", 18, 14, 22, 45, 85)

    print("\nExecuting Test Case 2: Normal Case (Academic Failure)")
    generate_student_dashboard("Aman Gupta", "CS019", 8, 5, 10, 15, 80)

    print("\nExecuting Test Case 3: Edge Case (Boundary Failure)")
    generate_student_dashboard("Priya Singh", "CS099", 20, 15, 25, 48, 74)
