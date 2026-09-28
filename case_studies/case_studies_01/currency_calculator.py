amount = input("Enter the amount in USD: ")
exchange_rate = float(input("Enter the exchange rate (1 USD to target currency): "))
converted_amount = float(amount) * exchange_rate

print(f"\nAmount in USD: {amount}")
print(f"Exchange Rate: {exchange_rate}")
print(f"Converted Amount: {converted_amount}")

