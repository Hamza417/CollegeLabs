from report_utils import build_formatted_card, get_valid_number


def main():
    info = {
        "Name": input("Student Name: ").strip(),
        "Roll Number": input("Roll Number: ").strip(),
        "Age": str(get_valid_number("Age: ", num_type=int, min_value=1)),
        "Course": input("Course: ").strip(),
        "College": input("College: ").strip(),
    }

    marks = {}
    print("\n--- Enter Subject Marks ---")
    for i in range(1, 4):
        score = get_valid_number(
            f"Marks in Subject {i}: ", num_type=float, min_value=0
        )
        marks[f"Subject {i}"] = f"{score:.2f}"

    raw_scores = [float(val) for val in marks.values()]
    total = sum(raw_scores)
    avg = total / len(raw_scores)

    metrics = {
        "Total Marks": f"{total:.2f}",
        "Average": f"{avg:.2f}",
    }

    report = build_formatted_card(
        title="STUDENT REPORT",
        sections=[info, marks, metrics],
    )

    print("\n" + report)


if __name__ == "__main__":
    main()