'''
Given a list of integers, write a function that finds the longest subsequence where the difference between consecutive elements is either 1 or -1. 
Return the length of this subsequence.
'''
def longest_subsequence(list):
    arr = []
    prev_val = list[0]

    # Create array of differences between consecutive elements, 1 if difference was -1 or 1, 0 otherwise
    for val in list:
        if abs(val - prev_val) == 1: 
            arr.append(1)
        else:
            arr.append(0)

        prev_val = val


    # Get the maximum consecutive sum to find the longest subsequence with an absolute difference of 1 between elements
    max_subs = 0
    subs = 0

    for a in arr[1:]:
        if a == 1:
            subs += a
            if subs > max_subs:
                max_subs = subs
        else:
            subs = 0

    # Add one to account for intial element of subsequence
    max_subs += 1
  
    return max_subs


print(longest_subsequence([1,2,3,4,5]))
#5
print(longest_subsequence([4,2,3,1,5]))
#2
print(longest_subsequence([10,11,7,8,9,12]))
#3