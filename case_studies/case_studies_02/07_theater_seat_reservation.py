# Task 1: Represent a 3x4 seat matrix using a 2D nested list containing booleans
# False = Vacant, True = Booked
# Using a list comprehension to initialize a 3 (rows) x 4 (columns) grid
theater_grid = [[False for _ in range(4)] for _ in range(3)]

# Constants for visual representation of seat states
BOOKED_STATE = "(■)"
NOT_BOOKED_STATE = "[ ]"

def print_dashboard():
    """Task 5: Renders the real-time Theater Occupancy Dashboard."""
    # Task 3: Compute total seats, reserved count, and occupancy using list iteration
    total_seats = 0
    booked_seats = 0

    for row in theater_grid:
        for seat in row:
            total_seats += 1
            if seat:
                booked_seats += 1

    occupancy_rate = (booked_seats / total_seats) * 100

    print("=" * 50)
    print(f"{'THEATER OCCUPANCY DASHBOARD':^50}")
    print("=" * 50)
    print(f"{'Grid Layout':^50}")
    print(f"{f'{NOT_BOOKED_STATE} = Empty, {BOOKED_STATE} = Booked':^50}")
    print("-" * 50)

    # Iterate through the grid to render the visual map
    for i, row in enumerate(theater_grid):
        row_display = ""
        for seat in row:
            if seat:
                row_display += BOOKED_STATE + " "
            else:
                row_display += NOT_BOOKED_STATE + " "
        print(f"Row {i}: {row_display.strip()}")

    print("-" * 50)
    print(f"{'Total Seats':<15} : {total_seats}")
    print(f"{'Booked Seats':<15} : {booked_seats}")
    print(f"{'Occupancy Rate':<15} : {occupancy_rate:.1f}%")
    print("=" * 50)


# Task 2: Booking routine verifying availability using if-else
def process_menu_action(action, row_idx=None, col_idx=None):
    """Task 4: Interactive menu dispatcher using if-elif-else structure."""
    if action == 'book':
        # Validate grid boundaries before attempting to access the index
        if 0 <= row_idx < len(theater_grid) and 0 <= col_idx < len(theater_grid[0]):
            if not theater_grid[row_idx][col_idx]:
                theater_grid[row_idx][col_idx] = True
            else:
                print(f"System: Seat at Row {row_idx}, Col {col_idx} is already booked!", end="\n\n")
        else:
            print("System: Invalid row or column selection.")

    elif action == 'view':
        print_dashboard()

    elif action == 'exit':
        print("System: Exiting reservation engine.")

    else:
        print("System: Invalid menu command.")


# Simulating the interactive menu inputs to match the requested final output
# Booking 3 specific seats -> Row 0/Col 0, Row 0/Col 3, and Row 2/Col 3
process_menu_action('book', 0, 0)
process_menu_action('book', 0, 3)
process_menu_action('book', 2, 3)

# Simulating an attempt to book an already reserved seat to demonstrate error handling
process_menu_action('book', 0, 0)  # This should trigger an error

# Triggering the view command to generate the final dashboard
process_menu_action('view')
