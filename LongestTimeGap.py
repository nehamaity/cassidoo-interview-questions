# Write a function that takes an array of timestamps (HH:MM) from the same day 
# and returns the longest gap in minutes between consecutive timestamps.

def find_longest_time_gap(times):
    times_mins = []
    diff = 0
    max = 0

    for time in times:
        hours = int(time[0:2]) * 60
        minutes = int(time[3:5])
        times_mins.append(hours + minutes)

    times_mins = sorted(times_mins)

    for i in range(len(times) - 1):
        diff = times_mins[i + 1] - times_mins[i]
        if diff > max:
            max = diff

    return max


print(find_longest_time_gap(['12:00']))
# 0

print(find_longest_time_gap(['09:00', '11:00']))
# 120

print(find_longest_time_gap(['14:00', '09:00', '15:00', '10:30']))
# 210

print(find_longest_time_gap(['08:00', '10:00', '10:00', '14:00']))
# 240