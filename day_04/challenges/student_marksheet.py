from report_utils import build_formatted_card, get_valid_number


def main():
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
    print("\n--- Enter Marks ---")
    for subject in subjects:
        marks[subject] = f"{get_valid_number(f'{subject}: '):.2f}"

    raw_scores = [float(val) for val in marks.values()]
    total = sum(raw_scores)
    avg = total / len(raw_scores)

    metrics = {
        "Total Marks": f"{total:.2f}",
        "Average Marks": f"{avg:.2f}",
    }

    marksheet = build_formatted_card(
        title="STUDENT MARKSHEET",
        sections=[info, marks, metrics],
    )

    print("\n" + marksheet)


if __name__ == "__main__":
    main()