from student import student_count
from placement import placement_count
from admission import admission_count

print(50 * "=")
print(f"{'UNIVERSITY DATA':^50}")
print(50 * "=")
print(f"{'Student Count':<25}: {student_count()}")
print(f"{'Admission Count':<25}: {placement_count()}")
print(f"{'Placement Count':<25}: {placement_count()}")
print(50 * "=")