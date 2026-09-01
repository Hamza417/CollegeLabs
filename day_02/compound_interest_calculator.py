principle = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))
compound_interest = principle * (1 + rate_of_interest / 100) ** time_period - principle
amount = principle + compound_interest

print(f"\nPrincipal Amount: {principle}")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Time Period: {time_period} years")
print(f"Compound Interest: {compound_interest}")
print(f"Total Amount after {time_period} years: {amount}")