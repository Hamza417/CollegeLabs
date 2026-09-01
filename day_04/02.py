def collect_student_input():
    """Prompts the user for student metadata and numeric scores for 3 subjects.

    Validates numeric inputs for marks to prevent runtime errors.

    Returns:
        tuple: A tuple containing:
            - info (dict): General student details (Name, Roll Number, Age, etc.).
            - marks (list[float]): List of numeric marks for each subject.
    """
    # Collect basic string metadata
    info = {
        "Name": input("Student Name: ").strip(),
        "Roll Number": input("Roll Number: ").strip(),
        "Age": input("Age: ").strip(),
        "Course": input("Course: ").strip(),
        "College": input("College: ").strip(),
    }

    # Prompt and validate subject marks sequentially
    marks = []
    for i in range(1, 4):
        while True:
            try:
                val = float(input(f"Marks in Subject {i}: "))
                marks.append(val)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric score.")

    return info, marks


def calculate_metrics(marks):
    """Calculates summary statistics for a list of marks.

    Args:
        marks (list[float]): List of numeric scores.

    Returns:
        tuple: A tuple containing:
            - total (float): The sum of all marks.
            - average (float): The mean score across all subjects.
    """
    total = sum(marks)
    average = total / len(marks) if marks else 0.0
    return total, average


def format_student_report(info, marks, total, average):
    """Formats student metadata and performance metrics into a aligned report card string.

    Dynamically adjusts colon alignment and border width based on text length.

    Args:
        info (dict): Student metadata keys and values.
        marks (list[float]): Individual subject scores.
        total (float): Sum of student marks.
        average (float): Mean student score.

    Returns:
        str: Fully formatted, multi-line student report card.
    """
    # Group data into distinct logical sections for visual spacing
    sections = [
        info,
        {f"Subject {i + 1}": f"{score:.2f}" for i, score in enumerate(marks)},
        {"Total Marks": f"{total:.2f}", "Average": f"{average:.2f}"},
    ]

    # Calculate max key length across all sections to align colons vertically
    all_keys = [key for section in sections for key in section]
    max_key_len = max(len(key) for key in all_keys)

    # Build key-value line strings with dynamic left-justified field width
    lines = []
    for idx, section in enumerate(sections):
        for key, val in section.items():
            lines.append(f"{key:<{max_key_len}} : {val}")
        # Insert a blank separator line between sections (except the last one)
        if idx < len(sections) - 1:
            lines.append("")

    # Determine overall border width based on the longest formatted line
    title = "STUDENT REPORT"
    max_line_len = max(len(line) for line in lines)
    border_width = max(max_line_len, len(title) + 8)

    # Build top and bottom decorative borders centered around the title
    header = f" {title} ".center(border_width, "=")
    footer = "=" * border_width

    # Combine borders and content into a single string
    return "\n".join([header] + lines + [footer])


def main():
    info, marks = collect_student_input()
    total, average = calculate_metrics(marks)
    report = format_student_report(info, marks, total, average)

    print("\n" + report)


if __name__ == "__main__":
    main()