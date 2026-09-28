student_name = input("Enter the student's name: ")
subject_marks = {}

num_subjects = int(input("Enter the number of subjects: "))
for i in range(num_subjects):
    subject = input(f"Enter the name of subject {i + 1}: ")
    marks = float(input(f"Enter the marks obtained in {subject}: "))
    subject_marks[subject] = marks

total_marks = sum(subject_marks.values())
percentage = (total_marks / (num_subjects * 100)) * 100

print(f"\nStudent Name: {student_name}")
print("Subject Marks:")

for subject, marks in subject_marks.items():
    print(f"{subject}: {marks}")

print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
