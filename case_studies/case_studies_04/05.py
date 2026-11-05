# Collect inputs
feedback = input("Enter Student Feedback: ")
search_word = input("Enter Word to search: ")
replacement_word = input("Enter Replacement word: ")

# Process string data
words = feedback.split()
char_count = len(feedback)
word_count = len(words)

first_word = words[0] if words else ""
last_word = words[-1] if words else ""

# Case-insensitive count for search occurrences
search_count = feedback.lower().count(search_word.lower())

# Replace the specific word (case-sensitive as per standard replace)
updated_feedback = feedback.replace(search_word, replacement_word)

# Show the dashboard (using width 70 to accommodate longer string outputs)
print("\n")
print("=" * 50)
print(f"{'UNIVERSITY FEEDBACK DASHBOARD':^50}")
print("=" * 50)
print(f"{'Characters':<25}: {char_count}")
print(f"{'Words':<25}: {word_count}")
print("-" * 50)
print(f"{'Uppercase':<25}: {feedback.upper()}")
print(f"{'Lowercase':<25}: {feedback.lower()}")
print("-" * 50)
print(f"{'First Word':<25}: {first_word}")
print(f"{'Last Word':<25}: {last_word}")
print(f"{'Search Count':<25}: {search_count}")
print("-" * 50)
print(f"{'Updated Feedback':<25}: {updated_feedback}")
print("=" * 50)
