# Given an array of characters chars, compress it such that consecutive duplicate 
# characters are replaced with the character followed by the count of duplicates. 
# If the count is 1, omit it.
def compress(array):
    counts = []
    first = 0
    for i in range(len(array)):
        if i == 0:
            counts.append((array[i], 1))
    
        elif array[i] != array[i - 1]:
            counts.append((array[i], 1))
            first =  [y[0] for y in counts].index(array[i])

        else: 
            if array[i] == counts[first][0]:
                updated = counts[first][1] + 1
                counts[first] = (array[i], updated)

    counts_list = []
    for c in range(len(counts)):
        if counts[c][1] > 1:
            counts_list.append(counts[c][0])
            counts_list.append(counts[c][1])
        else:
            counts_list.append(counts[c][0])

    counts_list = [str(x) for x in counts_list] 
    return counts_list

print(compress(["a", "b", "b", "b", "c"]))
# ["a", "b", "3", "c"]

print(compress(["a", "a", "b", "b", "c", "c", "c"]))
# ["a", "2", "b", "2", "c", "3"]

print(compress(["d", "d", "d", "e", "e", "f", "f", "f", "d"]))
# ["d", "3", "e", "2", "f", "3", "d"]
