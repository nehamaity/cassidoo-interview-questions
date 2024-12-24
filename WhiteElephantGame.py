'''
Make a white elephant gift exchange class that simulates the game. It should generate a sequence of random 
but valid gift-opening and gift-stealing moves for n participants, tracks steal counts and frozen gifts, 
and ends the game when everyone has a gift.

Example playthrough:

const game = new WhiteElephantGame(4); // 4 players

console.log(game.nextMove()); // "Person 0 opened gift 0"
console.log(game.nextMove()); // "Person 1 opened gift 1" 
console.log(game.nextMove()); // "Person 2 stole gift 0 from person 0"
console.log(game.nextMove()); // "Person 0 stole gift 1 from person 1"
console.log(game.nextMove()); // "Person 1 opened gift 2"
console.log(game.nextMove()); // "Person 3 opened gift 3"
console.log(game.nextMove()); // "Game Over! Final distribution: {'person 0':1, 'person 1':2, 'person 2':0, 'person 3':3}"
'''
import random
class WhiteElephantGame:
    def __init__(self, participants):
        self.participants = participants 
        self.i = 0 # Iterator variable for person
        self.gifts = {} # Dictonary for tracking each person and their gift
        self.steals = 0
        self.gift_stolen = -1
        self.prev_move = -1


    def next_move(self):
        # Initialize move to None
        self.outcome = None
        
        # If no gifts have been claimed (game has not started), Person 0 by default gets gift 0
        # Increment i for next move
        if len(self.gifts) == 0:
            self.gifts['Person 0'] = 0
            self.i += 1
            self.outcome = 'Person 0 opened gift 0'
            return self.outcome

        # Create list of people who currently have gifts
        has_gifts = list(self.gifts)

        # If length of gifts dictionary equals number of participants and all participants have a gift, end game        
        if len(self.gifts) == self.participants and None not in self.gifts.values():
            return 'Game Over! Final distribution: ' + str(self.gifts)

        # If person's gift was stolen, set i to the index of the person for their turn to open or steal a gift
        for key in self.gifts:
            if self.gifts[key] == None:
                self.i = int(key.split(' ')[1])

        # Random move options: 1 for person opens new gift, 2 for person steals existing gift from another person
        actions = [1, 2]
        
        # If only 2 people have gifts and last move was a steal, next move is opening new gift (prevent stealback)
        move = 0
        if self.prev_move == 2 and len(has_gifts) < 3:
            move = 1
        # Otherwise, select random move 
        else:
            move = random.choice(actions)

        # Continue while move outcome has not been determined and current index is less than number of participants 
        # (Participant count starts at 0)
        while self.outcome is None and self.i < self.participants:

            # Initialize person for current turn
            current = 'Person ' + str(self.i )

            # If current person already has a gift, skip them and continue to next person
            if current in has_gifts and self.gifts[current] is not None:
                    self.i += 1
                    continue

            # Allow person to open gift if random move = 1 or when 3 steals have already occured (steal count starts at 0) 
            if move == 1 or self.steals >= 3: 

                # If the number of the gift matches current person and that gift is already claimed, they claim the gift 
                # one number higher than the max number gift already claimed
                if self.i in self.gifts.values() and self.gifts[current] is None:
                    max_gift = max(m for m in self.gifts.values() if m is not None) + 1
                    self.gifts[current] = max_gift

                # Otherwise they get the gift that matches their number
                else: 
                    self.gifts[current] = self.i
                
                # Outcome of current move: gift opened
                self.outcome = current + ' opened gift ' + str(self.gifts[current])

                # Increment i for next person
                self.i += 1

                # Make steals = 0 as new gift restarts number of people who stole already and reset gift_stolen
                self.steals = 0
                self.gift_stolen = -1

                # Return outcome of current move
                return self.outcome

            # Allow stealing if random move generator = 2 and steals is less than 3 (count of steals starts at 0, so 3 
            # steals take place when value is 2)   
            elif move == 2 and self.steals < 3: 

                # If no gifts have been stolen yet, current person can steal from anyone except themself of course
                except_current = list(val for val in has_gifts if val != current)
                stolen_from = random.choice(except_current)

                # Gift cannot be a gift that was stolen in prior move
                if self.gifts[stolen_from] == self.gift_stolen and len(except_current) > 1: 
                    stolen_from = random.choice(list(val for val in except_current if val != stolen_from))

                #Outcome of current move: gift stolen
                self.outcome = current + ' stole gift ' + str(self.gifts[stolen_from]) + ' from ' + stolen_from

                # Set the gift that was stolen this move to not be stolen again (prevent stealback)
                self.gift_stolen = self.gifts[stolen_from]

                # Set stealer's gift to the person they stole from's gift
                self.gifts[current] = self.gifts[stolen_from]

                # Person who had their gift stolen no longer has a gift 
                self.gifts[stolen_from] = None
               
                # Set the next person to be who had their gift stolen 
                self.i = int(stolen_from.split(' ')[1])

                # Increment number of steals and return outcome of current move
                self.steals += 1
                self.prev_move = 2
                return self.outcome

            # Otherwise redo loop to create valid move outcome with next participant
            else:
                self.i += 1
                continue 


game = WhiteElephantGame(4)
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())
print(game.next_move())

