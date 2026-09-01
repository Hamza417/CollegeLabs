def collect_ticket_input():
    """Prompts the user for passenger details, flight information, and ticket pricing.

    Validates numeric inputs for age, ticket count, and price per ticket to prevent runtime errors.

    Returns:
        tuple: A tuple containing:
            - passenger_info (dict): Details like Name, Age, and Gender.
            - flight_info (dict): Route, Flight Number, and Travel Date.
            - pricing_info (dict): Ticket count and price per ticket.
    """
    passenger_info = {
        "Passenger Name": input("Passenger Name: ").strip(),
    }

    # Validate age input
    while True:
        try:
            age = int(input("Age: "))
            if age <= 0:
                print("Age must be a positive integer.")
                continue
            passenger_info["Age"] = str(age)
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for age.")

    passenger_info["Gender"] = input("Gender: ").strip()

    flight_info = {
        "From": input("From: ").strip(),
        "To": input("To: ").strip(),
        "Flight Number": input("Flight Number: ").strip(),
        "Travel Date": input("Travel Date: ").strip(),
    }

    # Validate number of tickets
    while True:
        try:
            num_tickets = int(input("Number of Tickets: "))
            if num_tickets <= 0:
                print("Number of tickets must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for ticket count.")

    # Validate price per ticket
    while True:
        try:
            price_per_ticket = float(input("Price per Ticket: "))
            if price_per_ticket < 0:
                print("Price cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric price.")

    pricing_info = {
        "num_tickets": num_tickets,
        "price_per_ticket": price_per_ticket,
    }

    return passenger_info, flight_info, pricing_info


def calculate_ticket_metrics(pricing_info):
    """Calculates the total amount for the ticket booking.

    Args:
        pricing_info (dict): Contains 'num_tickets' and 'price_per_ticket'.

    Returns:
        float: The grand total amount.
    """
    total_amount = pricing_info["num_tickets"] * pricing_info["price_per_ticket"]
    return total_amount


def format_currency(amount):
    """Formats numeric values into a currency string without trailing decimal zeros if whole.

    Args:
        amount (float): Amount to format.

    Returns:
        str: Formatted currency string with '₹'.
    """
    if amount.is_integer():
        return f"₹{int(amount)}"
    return f"₹{amount:.2f}"


def format_air_ticket(passenger_info, flight_info, pricing_info, total_amount):
    """Formats passenger and flight data into an aligned air ticket output.

    Dynamically aligns colons and adjusts borders based on maximum string width.

    Args:
        passenger_info (dict): Passenger metadata (Name, Age, Gender).
        flight_info (dict): Flight route and schedule details.
        pricing_info (dict): Ticket counts and pricing.
        total_amount (float): Grand total calculation.

    Returns:
        str: Fully formatted multi-line air ticket layout.
    """
    num_tickets = pricing_info["num_tickets"]
    price_per_ticket = pricing_info["price_per_ticket"]

    # Define logical display sections
    section_passenger = passenger_info
    section_flight = flight_info
    section_pricing = {
        "Number of Tickets": str(num_tickets),
        "Price per Ticket": format_currency(price_per_ticket),
    }
    section_total = {
        "Total Amount": format_currency(total_amount),
    }

    # Aggregate keys across all sections to compute maximum key width for colon alignment
    all_keys = (
        list(section_passenger.keys())
        + list(section_flight.keys())
        + list(section_pricing.keys())
        + list(section_total.keys())
    )
    max_key_len = max(len(key) for key in all_keys)

    # Helper function to convert a dictionary section into formatted key-value lines
    def format_section(section_dict):
        return [f"{key:<{max_key_len}} : {val}" for key, val in section_dict.items()]

    # Collect sample formatted lines to compute full border width dynamically
    sample_lines = (
        format_section(section_passenger)
        + format_section(section_flight)
        + format_section(section_pricing)
        + format_section(section_total)
    )

    title = "AIR TICKET"
    wish_text = "HAVE A SAFE JOURNEY!"
    max_line_len = max(len(line) for line in sample_lines)
    border_width = max(max_line_len, len(title) + 12, len(wish_text) + 8)

    # Build header, footer, and section separators
    header = f" {title} ".center(border_width, "=")
    footer = "=" * border_width
    dashed_line = "-" * border_width

    output = [
        header,
        "",
        *format_section(section_passenger),
        "",
        *format_section(section_flight),
        "",
        *format_section(section_pricing),
        "",
        dashed_line,
        *format_section(section_total),
        dashed_line,
        "",
        wish_text.center(border_width),
        footer,
    ]

    return "\n".join(output)


def main():
    passenger_info, flight_info, pricing_info = collect_ticket_input()
    total_amount = calculate_ticket_metrics(pricing_info)
    ticket = format_air_ticket(passenger_info, flight_info, pricing_info, total_amount)

    print("\n" + ticket)


if __name__ == "__main__":
    main()