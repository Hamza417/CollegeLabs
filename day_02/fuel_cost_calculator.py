distance = float(input("Enter the distance traveled (in kms): "))
mileage = float(input("Enter the mileage of the vehicle (in kms per liter): "))
fuel_price = float(input("Enter the fuel price (in rupees per liter): "))
fuel_required = distance / mileage
fuel_cost = fuel_required * fuel_price

print(f"\nDistance Traveled: {distance} kms")
print(f"Mileage of Vehicle: {mileage} kms/liter")
print(f"Fuel Price: {fuel_price} rupees/liter")
print(f"Fuel Required: {fuel_required} liters")
print(f"Total Fuel Cost: {fuel_cost} rupees")
