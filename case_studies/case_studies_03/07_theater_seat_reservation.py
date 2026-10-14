# Constants
ROWS = 3
COLS = 4
BOOKED_STATE = "(■)"
NOT_BOOKED_STATE = "[ ]"

# Initialize the 3x4 grid (Pre-booking a few seats to match your data)
theater_grid = [[False for _ in range(COLS)] for _ in range(ROWS)]

# Declare the variables
print(f"Available Rows: 0 to {ROWS-1} | Available Cols: 0 to {COLS-1}")
book_row = int(input("Enter Row to book: "))
book_col = int(input("Enter Column to book: "))
transaction_status = ""
total_seats = ROWS * COLS
booked_seats = 0

# Evaluate the booking attempt
if 0 <= book_row < ROWS and 0 <= book_col < COLS:
    if not theater_grid[book_row][book_col]:
        theater_grid[book_row][book_col] = True
        transaction_status = f"Success (Row {book_row}, Col {book_col} booked)"
    else:
        transaction_status = f"Failed (Seat at Row {book_row}, Col {book_col} is already taken)"
else:
    transaction_status = "Failed (Invalid row or column selection)"

# Calculate final occupancy metrics
for row in theater_grid:
    for seat in row:
        if seat:
            booked_seats += 1

occupancy_rate = (booked_seats / total_seats) * 100

# Show the dashboard
print()
print("=" * 55)
print(f"{'THEATER OCCUPANCY DASHBOARD':^55}")
print("=" * 55)
print(f"{'Recent Action':<15}: {transaction_status}")
print("-" * 55)
print(f"{'Grid Layout':^55}")
print(f"{f'{NOT_BOOKED_STATE} = Empty, {BOOKED_STATE} = Booked':^55}")
print("-" * 55)

# Iterate through the grid to render the visual map
for i, row in enumerate(theater_grid):
    row_display = ""
    for seat in row:
        if seat:
            row_display += BOOKED_STATE + " "
        else:
            row_display += NOT_BOOKED_STATE + " "
    # Printing with some padding to center the grid visually
    print(f"Row {i}:    {row_display.strip()}")

print("-" * 55)
print(f"{'Total Seats':<25}: {total_seats}")
print(f"{'Booked Seats':<25}: {booked_seats}")
print(f"{'Occupancy Rate':<25}: {occupancy_rate:.1f}%")
print("=" * 55)