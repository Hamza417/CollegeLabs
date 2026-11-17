student_id = input("Enter ID: ")
name = input("Enter Name: ")
department = input("Enter Department: ")
total_marks = 0
avg = 0

print()

marks = {
    "Python": 0,
    "DBMS": 0,
    "DSA": 0,
    "Java": 0,
    "IT": 0
}

for sub in marks.keys():
    marks[sub] = int(input(f"Enter marks for {sub}: "))
    total_marks += marks[sub]

avg = total_marks / len(marks)

print()

print("=" * 50)
print(f"{'UNIVERSITY STUDENT ACADEMIC DASHBOARD':^50}")
print("=" * 50)
print(f"{'ID':<25}: {student_id}")
print(f"{'Name':<25}: {name}")
print(f"{'Department':<25}: {department}")
print()
print(f"{'Marks':<25}")
for sub, marks in marks.items():
    print(f"{sub:<25}: {marks}")
print()
print(f"{'Average':<25}: {avg}")
print(f"{'Total Marks':<25}: {total_marks}")
print("=" * 50)
