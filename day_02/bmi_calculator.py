person_name = input("Enter your name: ")
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)

print(f"\nPerson Name: {person_name}")
print(f"Weight: {weight} kg")
print(f"Height: {height} m")
if bmi < 18.5:
    print(f"BMI: {bmi:.2f} (Underweight)")
elif 18.5 <= bmi < 24.9:
    print(f"BMI: {bmi:.2f} (Normal weight)")
elif 25 <= bmi < 29.9:
    print(f"BMI: {bmi:.2f} (Overweight)")
else:
    print(f"BMI: {bmi:.2f} (Obesity)")
