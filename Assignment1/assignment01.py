# Sakshat Garg
# Assignment: #1

# Basic details about the gym member
gym_member = "Alex Alliton"  # String
preferred_weight_kg = 20.5  # Float
highest_reps = 25  # Integer
membership_active = True  # Boolean

# Dictionary storing workout stats (yoga, running, weightlifting)
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (21, 65, 32),
    "Taylor": (94, 35, 25)
}

# Calculate and store total workout minutes
total_workout = {}
for friend, durations in workout_stats.items():
    total_workout[friend] = sum(durations)

# Creating a nested list with workout details
# Each row represents a friend, and each column represents an activity
workout_list = [list(durations) for durations in workout_stats.values()]

# Extract and display yoga & running minutes
print("Yoga and Running minutes for all friends:")
for row in workout_list:
    print(row[:2])

# Display weightlifting minutes for the last two friends
print("\nWeightlifting minutes for the last two friends:")
for row in workout_list[1:]:
    print(row[2])

# Check if any friend worked out for 120 minutes or more
for friend, total in total_workout.items():
    if total >= 120:
        print(f"Great job staying active, {friend}!")

# User input to check workout records
input_name = input("\nEnter a friend's name: ")
if input_name in workout_stats:
    activities = workout_stats[input_name]
    print(f"{input_name}'s workout minutes: Yoga: {activities[0]} min, Running: {activities[1]} min, Weightlifting: {activities[2]} min")
    print(f"Total workout minutes: {total_workout[input_name]}")
else:
    print(f"Friend {input_name} not found in the records.")

# Identify the most and least active friends
most_active = max(total_workout, key=total_workout.get)
least_active = min(total_workout, key=total_workout.get)

print(f"\nFriend with the highest workout minutes: {most_active} ({total_workout[most_active]} mins)")
print(f"Friend with the lowest workout minutes: {least_active} ({total_workout[least_active]} mins)")