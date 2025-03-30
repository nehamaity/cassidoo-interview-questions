# Write a function that finds the longest streak of consecutive true values in a boolean 
# array that meets or exceeds a given streak goal. Return 0 if no such streak exists. 

def find_longest_streak(array, goal):
    streak = 0
    for a in array:
        if a:
            streak += 1
        else:
            streak = 0

    if streak >= goal:
        return streak
        
    return 0

print(find_longest_streak([True, True, False, True, True, True], 3))
# 3

print(find_longest_streak([True, True, True, False, True], 4))
# 0

print(find_longest_streak([True, True, True, True], 2))
# 4
