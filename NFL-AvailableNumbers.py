'''
Given the current system of NFL uniform numbers, a given player's position, 
and an array of existing numbers on the team, write a function that returns 
a list of numbers that the given player can choose from for their uniform.
'''
def available_numbers(position, existing):
    
    if not isinstance(existing, list) or not all([isinstance(item, int) for item in existing]):
        return 'List not valid, please use a valid numerical list'

    match position:
        case 'QB':
            possible = list(range(1, 20))

        case 'RB':
            possible = list(range(1, 50))
            possible.extend(list(range(80, 90)))
   
        case 'WR':
            possible = list(range(1, 50))
            possible.extend(list(range(80, 90)))

        case 'TE':
            possible = list(range(1, 50))
            possible.extend(list(range(80, 90)))
     
        case 'OL':
            possible = list(range(50, 80))
          
        case 'DL':
            possible = list(range(50, 80))
            possible.extend(list(range(90, 100)))
          
        case 'LB':
            possible = list(range(1, 60))
            possible.extend(list(range(90, 100)))
          
        case 'DB':
            possible = list(range(1, 50))
         
        case 'K':
            possible = list(range(1, 50))
            possible.extend(list(range(90, 100)))
          
        case 'P':
            possible = list(range(1, 50))
            possible.extend(list(range(90, 100)))
         
        case 'LS':
            possible = list(range(1, 100))
           
        case default:
            return 'Position not valid, please use a valid NFL player position'

    return sorted(list(set(possible) - set(existing)))


print(available_numbers('QB', [1, 2, 3, 10, 19]))
# [4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18]

print(available_numbers('OL', [51, 53, 61, 65, 78]))
# [50, 52, 54, 55, 56, 57, 58, 59, 60, 62, 63, 64, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 79]



                

