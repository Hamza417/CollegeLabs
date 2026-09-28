cost_price = float(input("Enter the cost price of the item: "))
selling_price = float(input("Enter the selling price of the item: "))
profit_or_loss = selling_price - cost_price

if profit_or_loss > 0:
    print(f"\nCost Price: {cost_price}")
    print(f"Selling Price: {selling_price}")
    print(f"Profit: {profit_or_loss} rupees")
elif profit_or_loss < 0:
    print(f"\nCost Price: {cost_price}")
    print(f"Selling Price: {selling_price}")
    print(f"Loss: {-profit_or_loss} rupees")
else:
    print(f"\nCost Price: {cost_price}")
    print(f"Selling Price: {selling_price}")
    print("No profit, no loss.")
