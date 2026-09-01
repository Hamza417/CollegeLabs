customer_name = input("Enter the customer's name: ")
food_bill = float(input("Enter the food bill amount: "))
gst_percentage = float(input("Enter the GST percentage: "))
gst_amount = (food_bill * gst_percentage) / 100
total_bill = food_bill + gst_amount

print(f"\nCustomer Name: {customer_name}")
print(f"Food Bill Amount: {food_bill}")
print(f"GST Amount: {gst_amount}")
print(f"Total Bill Amount: {total_bill}")
