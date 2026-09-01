# Price Constants
NOTEBOOK_PRICE = 50
PEN_PRICE = 10
BAG_PRICE = 500

# Take Item Counts
notebook_count = int(input("Enter Number of Notebooks to Purchase: "))
pen_count = int(input("Enter Number of Pens to Purchase: "))
bag_count = int(input("Enter Number of Bags to Purchase: "))

# Calculate total amount
total_amount = (notebook_count * NOTEBOOK_PRICE) + (pen_count * PEN_PRICE) + (bag_count * BAG_PRICE)

print("Total Bill Amount:", total_amount, "Rs", sep=" ")