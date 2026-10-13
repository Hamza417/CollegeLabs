student_id = input("Enter ID: ")
name = input("Enter Name: ")
department = input("Enter Department: ")
total = 0
MAX_MARKS = 500

# Create a dictionary of subjects and marks for five subjects.
# -1 indicates marks are not updated yet for that subject
subject_marks = {
    "Python": -1,
    "DBMS": -1,
    "English": -1,
    "DSA": 96,
    "CSA": -1
}

print(f"\n{' Enter Subject Marks ':*^50}")

for subject, marks in subject_marks.items():
    if marks == -1:
        subject_marks[subject] = int(input(f"Enter marks for {subject}: "))
    else:
        print(f"{subject} marks is already set: {marks}")

for subject, marks in subject_marks.items():
    total += marks

avg = total / len(subject_marks)
percentage = (total / MAX_MARKS) * 100

print("\n")

print("=" * 50)
print(f"{'UNIVERSITY STUDENT DASHBOARD':^50}")
print("=" * 50)
print(f"{'Student ID:':<25} {student_id}")
print(f"{'Name:':<25} {name}")
print(f"{'Department:':<25} {department}")
print()
print(f"{'Evaluation ':-<50}")
print(f"{'Total:':<25} {total}/{MAX_MARKS}")
print(f"{'Percentage:':<25} {percentage:.2F} %")
print(f"{'Average:':<25} {round(avg, 2):.2F}")
print("=" * 50)
