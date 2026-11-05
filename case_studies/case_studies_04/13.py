import sqlite3

# Connect to the SQLite database (this creates 'university.db' if it doesn't exist)
conn = sqlite3.connect("university.db")
cur = conn.cursor()

# Create the student table
cur.execute("""CREATE TABLE IF NOT EXISTS student(
            student_id INTEGER PRIMARY KEY, 
            name TEXT, 
            department TEXT, 
            cgpa REAL)""")

# Prepare the initial student data
data = [
    (101, "Ayesha", "CSE", 8.8),
    (102, "Rahul", "IT", 7.9),
    (103, "Sara", "CSE", 9.1),
    (104, "Sameer", "ECE", 8.2)
]

# Insert the data using executemany, ignoring duplicates if the script is run multiple times
cur.executemany("INSERT OR IGNORE INTO student VALUES (?,?,?,?)", data)
conn.commit()

# Execute SQL queries to fetch the required statistics
cur.execute("SELECT COUNT(*) FROM student")
total_students = cur.fetchone()[0]

cur.execute("SELECT AVG(cgpa) FROM student")
avg_cgpa = cur.fetchone()[0]

cur.execute("SELECT name, cgpa FROM student ORDER BY cgpa DESC LIMIT 1")
top_student_record = cur.fetchone()
top_name = top_student_record[0]
top_cgpa = top_student_record[1]

# Close the database connection
conn.close()

# Show the dashboard
print("\n")
print("=" * 50)
print(f"{'UNIVERSITY DATABASE DASHBOARD':^50}")
print("=" * 50)
print(f"{'Total Students':<25}: {total_students}")
print(f"{'Average CGPA':<25}: {avg_cgpa:.2F}")
print("-" * 50)
print(f"{'Top Student':<25}: {top_name}")
print(f"{'Top CGPA':<25}: {top_cgpa}")
print("=" * 50)