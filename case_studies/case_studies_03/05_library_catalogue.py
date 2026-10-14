# Constants
CATALOG = {
    'B101': {'title': 'Python Fundamentals', 'author': 'John Doe'},
    'B102': {'title': 'Data Science Essentials', 'author': 'Jane Smith'},
    'B103': {'title': 'Clean Code Principles', 'author': 'Robert Roe'}
}

# Initialize state
available_books = set(CATALOG.keys())
issued_books = set()

# Pre-issue a book so the dashboard has mixed data
available_books.remove('B102')
issued_books.add('B102')

# Declare the variables
print(f"Valid Book IDs: {list(CATALOG.keys())}")
action = input("Enter action (issue/return): ").strip().lower()
book_id = input("Enter Book ID: ").strip().upper()
transaction_status = ""

# Evaluate the circulation action
if book_id not in CATALOG:
    transaction_status = f"Failed (Book ID '{book_id}' does not exist)"
elif action == 'issue':
    if book_id in available_books:
        available_books.remove(book_id)
        issued_books.add(book_id)
        transaction_status = f"Success (Book '{book_id}' has been issued)"
    else:
        transaction_status = f"Failed (Book '{book_id}' is already issued)"
elif action == 'return':
    if book_id in issued_books:
        issued_books.remove(book_id)
        available_books.add(book_id)
        transaction_status = f"Success (Book '{book_id}' has been returned)"
    else:
        transaction_status = f"Failed (Book '{book_id}' is not currently issued)"
else:
    transaction_status = "Failed (Invalid operation. Use 'issue' or 'return')"

# Show the dashboard
print()
print("=" * 60)
print(f"{'LIBRARY CATALOG STATUS DASHBOARD':^60}")
print("=" * 60)
print(f"{'Recent Action':<15}: {transaction_status}")
print("-" * 60)
print(f"{'ID':<6} | {'Book Title':<28} | Status")
print("-" * 60)

# Iterate over catalog to map data with dynamic set-based status
for current_id, details in CATALOG.items():
    title = details['title']
    status = "AVAILABLE" if current_id in available_books else "ISSUED"

    print(f"{current_id:<6} | {title:<28} | {status}")

print("-" * 60)
print(f"{'Total Catalog Books':<22}: {len(CATALOG)}")
print(f"{'Available Copies':<22}: {len(available_books)}")
print(f"{'Issued Copies':<22}: {len(issued_books)}")
print("=" * 60)
