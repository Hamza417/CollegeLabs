from report_utils import build_formatted_card, format_currency, get_valid_number


def main():
    passenger_info = {
        "Passenger Name": input("Passenger Name: ").strip(),
        "Age": str(get_valid_number("Age: ", num_type=int, min_value=1)),
        "Gender": input("Gender: ").strip(),
    }

    flight_info = {
        "From": input("From: ").strip(),
        "To": input("To: ").strip(),
        "Flight Number": input("Flight Number: ").strip(),
        "Travel Date": input("Travel Date: ").strip(),
    }

    num_tickets = get_valid_number("Number of Tickets: ", num_type=int, min_value=1)
    price_per_ticket = get_valid_number("Price per Ticket: ", num_type=float, min_value=0)
    total_amount = num_tickets * price_per_ticket

    pricing_info = {
        "Number of Tickets": str(num_tickets),
        "Price per Ticket": format_currency(price_per_ticket),
    }

    total_info = {
        "Total Amount": format_currency(total_amount),
    }

    sections = [passenger_info, flight_info, pricing_info, total_info]

    ticket = build_formatted_card(
        title="AIR TICKET",
        sections=sections,
        footer_text="HAVE A SAFE JOURNEY!",
        divider_indices=[3],  # Add dashed line before Total Amount section
    )

    print("\n" + ticket)


if __name__ == "__main__":
    main()