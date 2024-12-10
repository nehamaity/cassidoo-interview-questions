'''
Write a function wrapGifts that finds the maximum number of gifts that can be wrapped using a single 
strip of wrapping paper of a given width. Each gift has a specific length, and you can only wrap gifts 
if their total length fits within the paper width without cutting the paper.

wrapGifts([2, 3, 4, 5], 7)
2 // either gifts 2 and 5, or 3 and 4.

wrapGifts([1, 1, 1, 1, 1, 1, 1], 3)
3

wrapGifts([1, 2, 3, 4, 5], 6)
3 // 1 and 2 and 3

---

wrapGifts([2, 3, 6, 7, 7, 8, 9], 14)
3 // 2 and 3 and 9

wrapGifts([2, 2, 2, 2, 4, 4], 8)
4 // 2 and 2 and 2 and 2

'''

import itertools
def wrapGifts(gifts, paper):
    combos = []
    number = 0
    
    # Iterate through gifts to get all possible combinations
    for i in range(1, len(gifts)+1):
        combos.extend(itertools.combinations(gifts, i))

    # Check if the sum for each combination equals length of paper
    # combos is in order from by smallest to largest combo lengths, 
    # so the loop automatically results in the max number of gifts
    for combo in combos:
        if sum(combo) == paper:
            number = len(combo)

    return number


print(wrapGifts([2, 3, 4, 5], 7))
print(wrapGifts([1, 1, 1, 1, 1, 1, 1], 3))
print(wrapGifts([1, 2, 3, 4, 5], 6))
#
print(wrapGifts([2, 3, 6, 7, 7, 8, 9], 14))
print(wrapGifts([2, 2, 2, 2, 4, 4], 8))