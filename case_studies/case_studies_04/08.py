def check_eligibility(percentage):
    """Checks if a candidate is eligible (>= 60%)."""
    return percentage >= 60


# List of candidates with their percentages
candidates = [
    ("Ahmed", 86),
    ("Sara", 72),
    ("Rahul", 58),
    ("Ayesha", 91),
    ("Sameer", 67)
]

# Filter eligible candidates and create a list of dictionaries for easier handling
eligible_candidates = [{"name": name, "percentage": p} for name, p in candidates if check_eligibility(p)]

# Sort the eligible candidates by percentage in descending order using a lambda function
eligible_candidates = sorted(eligible_candidates, key=lambda x: x["percentage"], reverse=True)

# Show the dashboard
print("\n")
print("=" * 50)
print(f"{'JOB MELA DASHBOARD':^50}")
print("=" * 50)
print(f"{'Total Candidates':<25}: {len(candidates)}")
print(f"{'Eligible Candidates':<25}: {len(eligible_candidates)}")
print("-" * 50)

# Display the sorted eligible candidates
for i, candidate in enumerate(eligible_candidates, 1):
    print(f"{str(i) + '.':<5} {candidate['name']:<20} {candidate['percentage']} %")

print("=" * 50)
