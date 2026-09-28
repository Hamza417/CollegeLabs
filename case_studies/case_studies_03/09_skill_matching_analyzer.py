# Task 1: Define a set of job_requirements containing required skills
job_requirements = {'Python', 'SQL', 'Git', 'Docker'}

# Task 2: Store candidate profiles in a dictionary
# Keys are candidate names, values are sets of their skills
candidates = {
    'Adib': {'Python', 'SQL', 'Git', 'Docker', 'AWS'},
    'Hamza': {'Python', 'SQL', 'Java'},
    'Hassan': {'SQL', 'HTML'}
}

processed_candidates = []

for name, skills in candidates.items():
    # Task 3: Use set intersection (matched) and difference (missing)
    matched = job_requirements.intersection(skills)
    missing = job_requirements.difference(skills)

    # Task 4: Calculate candidate match percentage using floating-point math
    score = (float(len(matched)) / len(job_requirements)) * 100

    processed_candidates.append({
        'name': name,
        'score': score,
        'matched': matched,
        'missing': missing
    })

# Sort the evaluated candidates by their score in descending order
processed_candidates.sort(key=lambda x: x['score'], reverse=True)

# Task 5: Generate the HR Recruitment Skill Compatibility Report
print("=" * 60)
print(f"{'HR RECRUITMENT MATCH REPORT':^60}")
print("=" * 60)
print(f"{'Candidate':<9} | {'Match Score':<11} | {'Matched Skills':<16} | Missing")
print("-" * 60)

for candidate in processed_candidates:
    # Formatting matched skills display directly from the Set
    if len(candidate['matched']) == len(job_requirements):
        matched_str = "All Required"
    else:
        # Just convert the set to a list and join it (Order will be random)
        matched_str = ", ".join(list(candidate['matched']))

    # Formatting missing skills display directly from the Set
    if len(candidate['missing']) == 0:
        missing_str = "None"
    else:
        missing_list = list(candidate['missing'])
        if len(missing_list) > 2:
            missing_str = f"{missing_list[0]}, {missing_list[1]}..."
        else:
            missing_str = ", ".join(missing_list)

    # Outputting the parsed row
    # Since we are intersecting and differencing sets, the order of skills
    # in matched_str and missing_str may vary each time the code is run.
    print(f"{candidate['name']:<9} | {candidate['score']:<10.0f}% | {matched_str:<16} | {missing_str}")

print("-" * 60)
best_candidate = processed_candidates[0]
print(f"Best Candidate Match  : {best_candidate['name']} ({best_candidate['score']:.0f}%)")
print("=" * 60)
