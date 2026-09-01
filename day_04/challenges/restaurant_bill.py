from report_utils import build_formatted_card, format_currency, get_valid_number


def main():
    customer_name = input("Customer Name: ").strip()

    sections = [{"Customer Name": customer_name}]
    grand_total = 0.0

    for i in range(1, 4):
        print(f"\n--- Item {i} Details ---")
        name = input(f"Item {i} Name: ").strip()
        price = get_valid_number(f"Item {i} Price: ", num_type=float, min_value=0)
        qty = get_valid_number(f"Item {i} Quantity: ", num_type=int, min_value=1)

        amount = price * qty
        grand_total += amount

        sections.append({
            f"Item {i}": name,
            "Quantity": str(qty),
            "Amount": format_currency(amount),
        })

    sections.append({"Total Bill": format_currency(grand_total)})

    bill = build_formatted_card(
        title="RESTAURANT BILL",
        sections=sections,
        divider_indices=[len(sections) - 1],  # Dashed line before Total Bill
    )

    print("\n" + bill)


if __name__ == "__main__":
    main()
