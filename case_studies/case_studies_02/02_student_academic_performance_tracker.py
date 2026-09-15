# Task 1: Store student records in a dictionary
# Key: Student ID | Value: Tuple (Name, Math, Science, English)
students = {
    'S101': ('Adib', 85, 80, 88),
    'S102': ('Riyaz', 95, 90, 90),
    'S103': ('Hamza', 60, 62, 64)
}

processed_students = []
class_total_score = 0.0

# Task 2 & 3: Compute averages and assign grades
for student_id, data in students.items():
    name = data[0]
    grades = data[1:]

    # Task 2: Compute average using arithmetic operators and type casting
    # Explicitly casting the sum to a float before division
    average = float(sum(grades)) / len(grades)
    class_total_score += average

    # Task 3: Nested if-elif-else statements for letter grades and status
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

    # Append to a list for sorting later
    processed_students.append({
        'id': student_id,
        'name': name,
        'average': average,
        'grade': grade,
        'status': status
    })

# Task 4: Sort the list of students by average marks in descending order
# Using a lambda function to target the 'average' key for sorting
processed_students.sort(key=lambda x: x['average'], reverse=True)

# Task 5: Output structured Student Gradebook Report
print("=" * 55)
print(f"{'ACADEMIC PERFORMANCE DASHBOARD':^55}")
print("=" * 55)
print(f"{'Rank':<4} | {'ID':<6} | {'Name':<10} | {'Average':<7} | {'Grade':<5} | Status")
print("-" * 55)

# Enumerate allows us to automatically generate the Rank (starting at 1)
for rank, student in enumerate(processed_students, start=1):
    print(f"{rank:<4} | {student['id']:<6} | {student['name']:<10} | "
          f"{student['average']:<7.2f} | {student['grade']:<5} | {student['status']}")

print("-" * 55)

# Calculate class-wide statistics
class_average = class_total_score / len(students)
top_student = processed_students[0]

print(f"Class Average Score   : {class_average:.2f}")
print(f"Top Scoring Student   : {top_student['name']} ({top_student['average']:.2f})")
print("=" * 55)
