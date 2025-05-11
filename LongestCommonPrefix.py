# Write a function that takes a list of strings and returns the longest string 
# that is a prefix of at least two (or all) strings in the list.
def longest_common_prefix(words):
    if len(words) == 1:
        return words[0]

    substr = ''
    longest_substr = ''
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            for s in range(len(max(words[i], words[j]))):
                if words[j][:s] == words[i][:s]:
                    substr = words[i][:s]

            # Solution for longest substring that is prefix of all items in list
            '''
            if substr in words[i - 1]:
                longest_substr = substr
            '''
            # Solution for longest string that is prefix of at least two strings in list
            if substr > longest_substr:
                longest_substr = substr

    return longest_substr

print(longest_common_prefix(["flower","flow","flight"]))
# "fl"

print(longest_common_prefix(["dog","racecar","car"]))
# ""

print(longest_common_prefix(["interstellar","internet","interval"]))
# "inter"

print(longest_common_prefix(["carton","car","cars","cart"]))
# "cart"