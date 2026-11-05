from admission import admission_count
from placement import placed_count
from student import student_count

# Fetch data from modules
total_students = student_count()
total_admissions = admission_count()
total_placed = placed_count()

# Show the dashboard
print("\n")
print("=" * 50)
print(f"{'UNIVERSITY ADMIN DASHBOARD':^50}")
print("=" * 50)
print(f"{'Total Students':<25}: {total_students}")
print(f"{'Total Admissions':<25}: {total_admissions}")
print(f"{'Students Placed':<25}: {total_placed}")
print("=" * 50)
