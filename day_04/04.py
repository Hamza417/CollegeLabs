def collect_student_input():
    """Prompts the user for student metadata and marks in 5 specific subjects.

    Validates numeric inputs for marks to prevent runtime errors.

    Returns:
        tuple: A tuple containing:
            - info (dict): Student metadata ('Student Name', 'Roll Number').
            - marks (dict): Subject names mapped to their numeric scores.
    """
    info = {
        "Student Name": input("Student Name: ").strip(),
        "Roll Number": input("Roll Number: ").strip(),
    }

    subjects = [
        "English",
        "Mathematics",
        "Computer Science",
        "Science",
        "Social Studies",
    ]

    marks = {}
    print("\n--- Enter Subject Marks ---")
    for subject in subjects:
        while True:
            try:
                val = float(input(f"Marks in {subject}: "))
                if val < 0:
                    print("Marks cannot be negative.")
                    continue
                marks[subject] = val
                break
            except ValueError:
                print("Invalid input. Please enter a numeric score.")

    return info, marks


def calculate_metrics(marks):
    """Calculates total and average marks across all subjects.

    Args:
        marks (dict): Dictionary mapping subject names to float scores.

    Returns:
        tuple: A tuple containing:
            - total (float): The sum of all subject marks.
            - average (float): The mean score across all subjects.
    """
    total = sum(marks.values())
    average = total / len(marks) if marks else 0.0
    return total, average


def format_marksheet(info, marks, total, average):
    """Formats student details, marks, and calculated summary metrics.

    Dynamically adjusts colon alignment and border width based on content length.

    Args:
        info (dict): Student metadata (Name, Roll Number).
        marks (dict): Subject names and scores.
        total (float): Grand total of marks.
        average (float): Average score.

    Returns:
        str: Fully formatted multi-line student marksheet string.
    """
    # Group data into logical display sections
    sections = [
        info,
        {subject: f"{score:.2f}" for subject, score in marks.items()},
        {"Total Marks": f"{total:.2f}", "Average Marks": f"{average:.2f}"},
    ]

    # Find maximum label width across all keys to align colons vertically
    all_keys = [key for section in sections for key in section]
    max_key_len = max(len(key) for key in all_keys)

    # Build key-value line strings with dynamic field padding
    lines = []
    for idx, section in enumerate(sections):
        for key, val in section.items():
            lines.append(f"{key:<{max_key_len}} : {val}")
        # Insert a blank separator line between sections (except the last section)
        if idx < len(sections) - 1:
            lines.append("")

    # Dynamically scale border width based on maximum content length
    title = "STUDENT MARKSHEET"
    max_line_len = max(len(line) for line in lines)
    border_width = max(max_line_len, len(title) + 8)

    # Construct dynamic header and footer
    header = f" {title} ".center(border_width, "=")
    footer = "=" * border_width

    return "\n".join([header] + lines + [footer])


def main():
    info, marks = collect_student_input()
    total, average = calculate_metrics(marks)
    marksheet = format_marksheet(info, marks, total, average)

    print("\n" + marksheet)


if __name__ == "__main__":
    main()