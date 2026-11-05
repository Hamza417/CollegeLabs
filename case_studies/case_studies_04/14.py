# 14.py
import sqlite3

try:
    # Connect to the SQLite database
    conn = sqlite3.connect("career_management.db")
    cur = conn.cursor()

    # Create the tables
    cur.execute(
        "CREATE TABLE IF NOT EXISTS placement (id INTEGER PRIMARY KEY, company TEXT, package REAL, status TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS training (id INTEGER PRIMARY KEY, name TEXT, participants INTEGER)")
    cur.execute("CREATE TABLE IF NOT EXISTS alumni (id INTEGER PRIMARY KEY, name TEXT, company TEXT)")

    # Insert initial records using transactions
    cur.execute("INSERT OR IGNORE INTO placement VALUES (1, 'ABC Technologies', 8.5, 'Placed')")
    cur.execute("INSERT OR IGNORE INTO training VALUES (1, 'Python & AI Training', 120)")
    cur.execute("INSERT OR IGNORE INTO alumni VALUES (1, 'Rahul', 'XYZ Ltd')")

    # Commit the transaction
    conn.commit()

    # Execute SQL queries to fetch the required statistics
    cur.execute("SELECT COUNT(*) FROM placement WHERE status='Placed'")
    students_placed = cur.fetchone()[0]

    cur.execute("SELECT SUM(participants) FROM training")
    students_trained = cur.fetchone()[0] or 0

    cur.execute("SELECT COUNT(*) FROM alumni")
    registered_alumni = cur.fetchone()[0]

    cur.execute("SELECT MAX(package) FROM placement")
    highest_package = cur.fetchone()[0] or 0

    # Show the dashboard (Using 55 width to accommodate the longer title)
    print("\n")
    print("=" * 55)
    print(f"{'PLACEMENT, TRAINING & ALUMNI DASHBOARD':^55}")
    print("=" * 55)
    print(f"{'Students Placed':<25}: {students_placed}")
    print(f"{'Students Trained':<25}: {students_trained}")
    print("-" * 55)
    print(f"{'Registered Alumni':<25}: {registered_alumni}")
    print(f"{'Highest Package':<25}: {highest_package} LPA")
    print("=" * 55)

except sqlite3.Error as e:
    # Rollback in case of error during transaction
    if "conn" in locals():
        conn.rollback()
    print(f"Database Error: {e}")

finally:
    # Always ensure the database connection is closed safely
    if "conn" in locals():
        conn.close()