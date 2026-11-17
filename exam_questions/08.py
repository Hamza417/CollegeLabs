def is_elidgible(p):
    return p>=60

candidates = [
    ("Ayesha", 60),
    ("Adib", 72),
    ("Zoha", 84),
    ("Hamza", 76),
    ("Riyaz", 42)
]

selected = [{"name":n, "percentage":p} for n, p in candidates if is_elidgible(p)]
selected = sorted(selected, key=lambda x:x["percentage"], reverse=True)

print(50 * "=")
print(f"{'JOB MELA CANDIDATE DASHBOARD':^50}")
print(50 * "=")
for i, c in enumerate(selected, 1):
    print(f"{i:<1}. {c["name"]:<25}: {c["percentage"]}%")
print(50 * "=")