# Write a function that returns the first n Leyland numbers in ascending order. 
# A Leyland number is defined as x^y + y^x for integers x > 1 and y > 1. 
#
# Note: This is a limited function that only works until the 6th Leyland number: 100
def get_leyland_numbers(n):
    i = 0
    x = 2
    y = 2
    step = 0 # Variable to insert cases where x = y. Example when x and y both equal 3 (54) is less than x = 2 and y = 5 (57)
    double = True # Variable to account for cases where x and y are equal
    leyland = []
    while i <= n:
        while y < 10:

            if double:
                step = x + 1
            if double and ((x ** y) + (y ** x) >= ((step ** step) + (step ** step))):
        
                leyland.append((step ** step) + (step ** step))
                double = False

            else: 
                 leyland.append((x ** y) + (y ** x))
                 y += 1
            
        i += 1
        x += 1
        double = True

    return leyland[:n]


print(get_leyland_numbers(1))
#[8]

print(get_leyland_numbers(5))
#[8, 17, 32, 54, 57]