'''
Given a list of integers, write a function that finds the longest subsequence where the difference between consecutive elements is either 1 or -1. 
Return the length of this subsequence.
'''
def longest_subsequence(list):
    if list == None:
        return 0

    prev_val = list[0]
    subsequence = 0
    max_subsequence = 0

    # Sum subsequent elements if absolute difference is 1, keep track of max subsequence
    for val in list:
        if abs(val - prev_val) == 1: 
            subsequence += 1
            if subsequence > max_subsequence:
                max_subsequence = subsequence
        else:
            subsequence = 0

        prev_val = val

    # Add one to account for initial element of subsequence
    max_subsequence += 1
    
    return max_subsequence 


print(longest_subsequence([1,2,3,4,5]))
#5
print(longest_subsequence([4,2,3,1,5]))
#2
print(longest_subsequence([10,11,7,8,9,12]))
#3