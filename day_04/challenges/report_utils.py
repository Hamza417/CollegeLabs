def get_valid_number(prompt, num_type=float, min_value=0):
    """Generic input prompt loop with type-casting and range validation."""
    while True:
        try:
            val = num_type(input(prompt))
            if min_value is not None and val < min_value:
                print(f"Value cannot be less than {min_value}.")
                continue
            return val
        except ValueError:
            expected_type = "an integer" if num_type is int else "a numeric value"
            print(f"Invalid input. Please enter {expected_type}.")


def format_currency(amount):
    """Formats numeric values into a rupee string without unnecessary decimal points."""
    if isinstance(amount, (int, float)) and amount.is_integer():
        return f"₹{int(amount)}"
    return f"₹{amount:.2f}"


def build_formatted_card(title, sections, footer_text=None, divider_indices=None):
    """Renders grouped dictionary sections into a dynamic, colon-aligned receipt/report.

    Args:
        title (str): Card title for top border header.
        sections (list[dict]): List of dictionary sections to print.
        footer_text (str, optional): Centered footer greeting or message.
        divider_indices (list[int], optional): Section indices where a dashed separator line
          should be rendered instead of a blank space.
    """
    if divider_indices is None:
        divider_indices = []

    # Find the longest key across all sections to justify colons
    all_keys = [key for section in sections for key in section]
    max_key_len = max((len(key) for key in all_keys), default=0)

    # Format key-value pairs
    lines = []
    for idx, section in enumerate(sections):
        if idx in divider_indices:
            lines.append("---DIVIDER---")
        elif idx > 0:
            lines.append("")  # Blank line separator

        for key, val in section.items():
            lines.append(f"{key:<{max_key_len}} : {val}")

    # Calculate optimal border width based on longest content line
    content_lines = [l for l in lines if l != "---DIVIDER---"]
    max_line_len = max((len(l) for l in content_lines), default=0)

    title_width = len(title) + 12
    footer_width = len(footer_text) + 8 if footer_text else 0
    border_width = max(max_line_len, title_width, footer_width)

    # Replace divider placeholders with scaled dashed lines
    dashed_line = "-" * border_width
    processed_lines = [
        dashed_line if line == "---DIVIDER---" else line for line in lines
    ]

    # Construct borders
    header = f" {title} ".center(border_width, "=")
    footer = "=" * border_width

    output = [header]
    if processed_lines and processed_lines[0] != "":
        output.append("")
    output.extend(processed_lines)

    if footer_text:
        output.extend(["", dashed_line, "", footer_text.center(border_width)])

    output.append(footer)
    return "\n".join(output)