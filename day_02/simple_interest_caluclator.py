principle = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = (principle * rate_of_interest * time_period) / 100

print(f"\nPrincipal Amount: {principle}")
print(f"Rate of Interest: {rate_of_interest}%")
print(f"Time Period: {time_period} years")
print(f"Simple Interest: {simple_interest}")
