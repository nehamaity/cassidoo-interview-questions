from itertools import permutations
import random
import math

# Retrieve list with all permutations (not unique)
def permute(input):
    perm = list(permutations(input)) # List of all permutations as tuples of their characters
    perm = [''.join(permutation) for permutation in perm] # Join the tuples to create strings of each permutation
    return perm


# Retrieve random permutation 
def random_perm(input):
    selected = []

    # Continue selecting random characters until no characters are remaining
    remaining = input
    while len(selected) < len(input):
        letter = random.choice(remaining)
        i = remaining.find(letter)
        l = list(remaining)
        l.pop(i)
        remaining = ''.join(l)
        selected.append(letter)
        
    return ''.join(selected)


# Retrieve list with all unique permutations
def permute2(input):
    perm = []
    
    # Get all unique chars in input string and their counts
    unique = set(input)
    counts = []
    for u in unique:
        counts.append(input.count(u))

    # The number of permutations of a string equals the factorial of the string length
    #   Example: abc would have 3! = 6 permutations
    #
    # To get unique permutations when recurring characters exist in the string:
    # Need to divide the factorial of the string length by the count of recurring characters multiplied by each other
    #   Example: tall would have 4!/2! = 12 unique permutations
    #            toot would have 4!/(2! * 2!) = 6 unique permutations
    repeats = 1
    for c in counts:
        repeats *= math.factorial(c)

    while len(perm) < math.factorial(len(input))/repeats:
        word = random_perm(input)

        # If the permutation does not exist yet in the list, add it
        if word not in perm:
            perm.append(word)

    return perm

print(permute('abc'))
print(permute2('abc'))

print(permute('talk'))
print(permute2('talk'))

print(permute('aac'))
print(permute2('aac'))

print(permute('tall'))
print(permute2('tall'))

print(permute('toot'))
print(permute2('toot'))

