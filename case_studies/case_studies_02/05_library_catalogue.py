# Task 1: Store library catalog items in a nested dictionary
catalog = {
    'B101': {'title': 'Python Fundamentals', 'author': 'John Doe'},
    'B102': {'title': 'Data Science Essentials', 'author': 'Jane Smith'},
    'B103': {'title': 'Clean Code Principles', 'author': 'Robert Roe'}
}

# Task 2: Maintain two distinct Python sets for circulation state
# All books start as available
available_books = {'B101', 'B102', 'B103'}
issued_books = set()  # No book has been issued yet, so this set is empty


# Task 3 & 4: Menu dispatching function to issue and return books
def process_circulation(action, book_id):
    """Handles circulation desk operations by shifting IDs between sets."""
    # Standard if-elif-else control flow for dispatching
    if action == 'issue':
        if book_id in available_books:
            available_books.remove(book_id)
            issued_books.add(book_id)
        else:
            print(f"Error: Book {book_id} is already issued or invalid.")

    elif action == 'return':
        if book_id in issued_books:
            issued_books.remove(book_id)
            available_books.add(book_id)
        else:
            print(f"Error: Book {book_id} is not currently issued.")

    else:
        print("Error: Invalid operation. Use 'issue' or 'return'.")


# Issuing 'B102' shifts it from available_books to issued_books
process_circulation('issue', 'B102')

# Task 5: Print a structured Library Catalog Status Dashboard
print("=" * 50)
print(f"{'LIBRARY CATALOG STATUS DASHBOARD':^50}")
print("=" * 50)
print(f"{'ID':<6} | {'Book Title':<25} | Status")
print("-" * 50)

# Iterate over catalog to map data with dynamic set-based status
for book_id, details in catalog.items():
    title = details['title']

    # Fast O(1) membership testing using Sets
    if book_id in available_books:
        status = "AVAILABLE"
    else:
        status = "ISSUED"

    print(f"{book_id:<6} | {title:<25} | {status}")

print("-" * 50)
print(f"Total Catalog Books : {len(catalog)}")
print(f"Available Copies    : {len(available_books)}")
print(f"Issued Copies       : {len(issued_books)}")
print("=" * 50)
