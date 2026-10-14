# Constants
STUDENTS = {
    'S101': ('Adib', 85, 80, 88),
    'S102': ('Riyaz', 95, 90, 90),
    'S103': ('Hamza', 60, 62, 64)
}

# Declare the variables
processed_students = []
class_total_score = 0.0

# Evaluate the grades and rankings
for student_id, data in STUDENTS.items():
    name = data[0]
    grades = data[1:]

    # Compute average
    average = float(sum(grades)) / len(grades)
    class_total_score += average

    # Assign letter grades and status
    if average >= 90:
        grade = 'A'
        status = 'PASS'
    elif average >= 80:
        grade = 'B'
        status = 'PASS'
    elif average >= 60:
        grade = 'C'
        status = 'PASS'
    else:
        grade = 'F'
        status = 'FAIL'

    # Append to our list for processing
    processed_students.append({
        'id': student_id,
        'name': name,
        'average': average,
        'grade': grade,
        'status': status
    })

# Sort the list by average marks in descending order
processed_students.sort(key=lambda x: x['average'], reverse=True)

# Calculate class-wide statistics
class_average = class_total_score / len(STUDENTS)
top_student = processed_students[0]

# Show the dashboard
print()
print("=" * 60)
print(f"{'ACADEMIC PERFORMANCE DASHBOARD':^60}")
print("=" * 60)
print(f"{'Rank':<5} | {'ID':<6} | {'Name':<12} | {'Average':<7} | {'Grade':<5} | Status")
print("-" * 60)

# Iterate to display the formatted rows
for rank, student in enumerate(processed_students, start=1):
    print(f"{rank:<5} | {student['id']:<6} | {student['name']:<12} | {student['average']:<7.2f} | {student['grade']:<5} | {student['status']}")

print("-" * 60)
print(f"{'Class Average Score':<25}: {class_average:.2f}")
print(f"{'Top Scoring Student':<25}: {top_student['name']} ({top_student['average']:.2f})")
print("=" * 60)