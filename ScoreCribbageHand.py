'''
Write a function scoreHand(cards) that calculates the total score of a Cribbage hand. 
The input is an array of 5 card strings (including the starter card), where each card 
is represented as rank+suit (e.g., "AH", "10D", "KS"). Here are the scoring rules:

    15s: 2 points for each combination of cards summing to 15
    Pairs: 2 points for each pair of same-rank cards
    Runs: 1 point per card in a run of 3 or more consecutive ranks

'''
from itertools import combinations
def score_hand(cards):

    # Store card value and card order in respective dictionaries
    values = {'A': 1, 'J': 10, 'Q': 10, 'K': 10}
    order = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

    # Extract numerical int value of each non lettered card, retain letter otherwise
    ranks = [card[0] if card.isalpha() else int(card[0]) for card in cards]

    # Check for same-rank pairs by comparing length of ranks to set of ranks, 
    # the difference in these values is the number of pairs
    #
    # Multiply this value by 2 to get the score from pairs
    pairs = (len(ranks) - len(set(ranks))) * 2

    # Create lists with card values (ranks_num) and card orders (ranks_ind) respectively
    ranks_num = [rank if isinstance(rank, int) else values[rank] for rank in ranks]
    ranks_ind = [rank if isinstance(rank, int) else order[rank] for rank in ranks]

    summed = 0
    consecutive = 0

    # Iterate through all combinations of ranks_num of all lengths and check if sum = 15, if so, add 2 each time
    for n in range(1, len(ranks_num) + 1):
        for combo in combinations(ranks_num, n):
            if sum(combo) == 15:
                summed += 2

    # Iterate through all combinations of ranks_ind 3 and greater and find the longest consecutive combo
    for n in range(3, len(ranks_ind) + 1):
        for combo in combinations(ranks_ind, n):
            if list(combo) == list(range(min(combo), max(combo) + 1)):
                if len(combo) > consecutive:
                    consecutive = len(combo)

    score = summed + pairs + consecutive
    
    return score


print(score_hand(["7H", "8C", "9D", "JH", "KS"]))
# 7H + 8C = 15; 7, 8, 9 are consecutive (2 + 3 = 5)

print(score_hand(["AH", "2C", "3D", "4S", "5H"]))
# All values sum to 15 and are consecutive (2 + 5 = 7)
