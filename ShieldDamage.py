'''
Given an array of attack damages and a shield capacity for a spaceship, 
return the index when cumulative damage exceeds the shield. 
Return -1 if shield survives. 
'''
def find_shield_break(damages, capacity):
    cummulative_damage = 0
    for i in range(len(damages)):
        cummulative_damage += damages[i]
        if cummulative_damage > capacity:
            return i

    return -1


print(find_shield_break([10, 20, 30, 40], 50))
# 2

print(find_shield_break([1, 2, 3, 4], 20))
# -1

print(find_shield_break([50], 30))
# 0
