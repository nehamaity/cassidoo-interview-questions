def find_anagrams(s, p):
    s = s.lower()
    array = []
    p_sorted = ''.join(sorted(p))

    for i in range(len(s)):
        substring = ''.join(sorted(s[i:(i + len(p))]))

        if substring == p_sorted:
            array.append(i)

    return array


print(find_anagrams("cbaebabacd", "abc"))
# [0, 6]

print(find_anagrams("fish", "cake"))
# []

print(find_anagrams("abab", "ab"))
# [0, 1, 2]

print(find_anagrams("linguine", "in"))
# [1, 5]

print(find_anagrams("banana", "an"))
# [1, 2, 3, 4]