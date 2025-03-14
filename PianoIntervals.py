# Write a function that takes a list of piano keys played in sequence and returns 
# the largest interval (in semitones) between any two consecutive keys. Assume the 
# lowest note is A0, and the highest is C8. 

def find_largest_interval(notes):
    semitones = {'C':0, 'D':2, 'E':4, 'F':5, 'G':7, 'A':9, 'B':11}

    max = 0
    for i in range(len(notes) - 1):
        octaves_diff = (int(notes[i + 1][1]) - int(notes[i][1]))
        notes_diff = semitones[notes[i + 1][0]] - semitones[notes[i][0]]
        diff = abs(octaves_diff * 12 + notes_diff)

        if diff > max:
            max = diff
    
    return max

print(find_largest_interval(['A0', 'C1', 'G1', 'C2']))
# 7

print(find_largest_interval(['C4', 'G4', 'C5', 'G3']))
# 17

print(find_largest_interval(['E2', 'C3', 'G3', 'C8']))
# 53