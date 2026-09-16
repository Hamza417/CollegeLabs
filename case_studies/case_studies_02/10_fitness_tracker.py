# Task 1: Store activity logs in a list of dictionaries

# Note:
# While the question specifically pre-sets the 'goal_met' key,
# it is more apt to calculate it dynamically based on the daily step goal.
activity_logs = [
    {"day": "Mon", "steps": 10200, "calories": 450, "goal_met": True},
    {"day": "Tue", "steps": 8550, "calories": 380, "goal_met": True},
    {"day": "Wed", "steps": 4300, "calories": 200, "goal_met": False},
    {"day": "Thu", "steps": 11000, "calories": 500, "goal_met": True},
    {"day": "Fri", "steps": 2100, "calories": 410, "goal_met": True}
]

# Constants
DAILY_STEP_GOAL = 5000
MET_INDICATOR = "✔️"
NOT_MET_INDICATOR = "❌"


# function to format steps e.g., 1500 -> 1.5K
def format_steps(steps):
    """Formats step counts into a more readable format (e.g., 1500 -> 1.5K)."""
    if steps >= 1000:
        return f"{steps / 1000:.2f}K"
    return str(steps)


# Initialize aggregation variables
total_steps = 0
total_calories = 0
days_goal_met = 0

# Task 2: Calculate weekly cumulative stats using 'for' loops and compound operators (+=)
for log in activity_logs:
    total_steps += log["steps"]
    total_calories += log["calories"]

    # Task 3: Check if the daily step goal was met and update the 'goal_met' key accordingly
    if log["steps"] >= DAILY_STEP_GOAL:
        log["goal_met"] = True
        days_goal_met += 1
    else:
        log["goal_met"] = False

# Task 4: Determine average daily steps and cast floating values to integers
# The division results in a float, which we cast to int() for clean presentation
average_steps = int(total_steps / len(activity_logs))

# Calculate percentage for the dashboard
goal_completion_rate = (days_goal_met / len(activity_logs)) * 100

# Task 5: Format and output the Weekly Fitness Activity Analytics Dashboard report
print("=" * 55)
print(f"{'WEEKLY FITNESS ANALYTICS REPORT':^55}")
print("=" * 55)
print(f"{'Day':<5} | {'Steps':<7} | {'Calories (kcal)':<17} | Daily Goal Met")
print("-" * 55)

for log in activity_logs:
    # Convert boolean True/False to MET/NOT_MET for the dashboard
    goal_status = MET_INDICATOR if log["goal_met"] else NOT_MET_INDICATOR

    # Note: Formatting steps with a comma using :,
    print(f"{log['day']:<5} | {format_steps(log['steps']):<7} | {log['calories']:<17} | {goal_status}")

print("-" * 55)
print(f"{'Total Weekly Steps':<22} : {format_steps(total_steps)}")
print(f"{'Average Daily Steps':<22} : {format_steps(average_steps)}")
print(f"{'Goal Completion Rate':<22} : {goal_completion_rate:.1f}%")
print("=" * 55)
