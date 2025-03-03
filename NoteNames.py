# Given a list of frequencies (in Hz), write a function to determine the closest musical note for each 
# frequency based on the A440 pitch standard. Extra credit: indicate if the note is flat or sharp! 
#
# Reference: https://en.wikipedia.org/wiki/Scientific_pitch_notation#Table_of_note_frequencies

def get_note_names(frequencies):
    names = []

    for n in frequencies:
        min = n
        note = ""

        # Check if frequency is within 0.01Hz of a natural, otherwise is a flat or sharp
        for i in range(13):
            if abs(n - 8.175799 * (2 ** i)) < 0.01:
                min = abs(n - 8.175799 * (2 ** i))
                note = "This is a C"

            if abs(n - 8.661957 * (2 ** i)) < min:
                min = abs(n - 8.661957 * (2 ** i))
                note = "This is a C, but it's sharp"

            if abs(n - 9.177024 * (2 ** i)) < 0.01:
                min = abs(n - 9.177024 * (2 ** i))
                note = "This is a D"

            if abs(n - 9.722718 * (2 ** i)) < min:
                min = abs(n - 9.722718 * (2 ** i))
                note = "This is a D, but it's sharp"

            if abs(n - 10.30086 * (2 ** i)) < min:
                min = abs(n - 10.30086 * (2 ** i))
                note = "This is an E"

            if abs(n - 10.91338 * (2 ** i)) < min:
                min = abs(n - 10.91338 * (2 ** i))
                note = "This is an F"

            if abs(n - 11.56233 * (2 ** i)) < min:
                min = abs(n - 11.56233 * (2 ** i))
                note = "This is an F, but it's sharp"

            if abs(n - 12.24986 * (2 ** i)) < 0.01:
                min = abs(n - 12.24986 * (2 ** i))
                note = "This is a G"

            if abs(n - 12.97827 * (2 ** i)) < min:
                min = abs(n - 12.97827 * (2 ** i))
                note = "This is a G, but it's sharp"

            if abs(n - 13.75000 * (2 ** i)) < 0.01:
                min = abs(n - 13.75000 * (2 ** i))
                note = "This is an A"
	
            if abs(n - 14.56762 * (2 ** i)) < min:
                min = abs(n - 14.56762 * (2 ** i))
                note = "This is a B, but it's flat"

            if abs(n - 15.43385 * (2 ** i)) < 0.01:
                min = abs(n - 15.43385 * (2 ** i))
                note = "This is a B"
            
        names.append(note)
	
    return names
	
	
print(get_note_names([440, 490, 524, 293.66]))
# ["This is a A", "This is a B, but it's flat", "This is a C, but it's sharp", "This is a D"]

print(get_note_names([130.81, 493.88, 589, 1661.219]))
# ['This is a C', 'This is a B', "This is a D, but it's sharp", "This is a G, but it's sharp"]