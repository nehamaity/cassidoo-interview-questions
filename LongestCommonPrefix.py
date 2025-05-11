# Write a function that takes a list of strings and returns the longest string 
# that is a prefix of at least two (or all) strings in the list.
def longest_common_prefix(words):
    substr = ''
    longest_substr = ''
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            for s in range(len(max(words[i], words[j]))):
                if words[j][:s] == words[i][:s]:
                    substr = words[i][:s]

            if substr in words[i - 1]:
                longest_substr = substr

    return longest_substr

print(longest_common_prefix(["flower","flow","flight"]))
# "fl"

print(longest_common_prefix(["dog","racecar","car"]))
# ""

print(longest_common_prefix(["interstellar","internet","internal","interval"]))
# "inter"

print(longest_common_prefix(["carton","car","cars","cart"]))
# "car"
