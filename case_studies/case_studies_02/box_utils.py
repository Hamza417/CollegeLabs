WIDTH = 60

'''
Box character ref was taken from: https://en.wikipedia.org/wiki/Box-drawing_characters
'''


def print_top_border():
    """Prints the top edge of the dashboard box."""
    print(f"┌{'─' * (WIDTH - 2)}┐")


def print_bottom_border():
    """Prints the bottom edge of the dashboard box."""
    print(f"└{'─' * (WIDTH - 2)}┘")


def print_separator():
    """Prints a horizontal separator with T-junctions on the sides."""
    print(f"├{'─' * (WIDTH - 2)}┤")


def render_title(title):
    """Centers the title within the dashboard box vertical borders."""
    print(f"│{title.center(WIDTH - 2)}│")


def render_row(label, value, label_width=18):
    """Aligns a label, a colon, and its value, wrapped in vertical borders."""
    content = f" {label:<{label_width}} : {value}"
    # Pad the remaining space so the right border aligns perfectly
    print(f"│{content.ljust(WIDTH - 2)}│")


def render_marks(label, scored, total, label_width=18):
    """Formats marks with the 'scored / total' layout inside the box."""
    content = f" {label:<{label_width}} : {scored:<4} / {total}"
    print(f"│{content.ljust(WIDTH - 2)}│")


def render_table_header(col1, col2, col3):
    """Renders a 3-column table header within the box."""
    # Column widths: 15, 10, 27 (Total inner width = 58)
    content = f" {col1:<15} │ {col2:<10} │ {col3:<26}"
    print(f"│{content.ljust(58)}│")


def render_table_row(col1, col2, col3):
    """Renders a 3-column table row within the box."""
    content = f" {col1:<15} │ {col2:<10} │ {col3:<26}"
    print(f"│{content.ljust(58)}│")
