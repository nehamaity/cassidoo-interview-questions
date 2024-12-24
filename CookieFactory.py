'''
At the Magic Cookie Factory, cookies are baked in factorial quantities. 
A cookie is "perfectly round" if its size ends with a zero. 
Write a function to determine how many perfectly round cookies will be made when baking with n! ingredients.

Examples:

countPerfectlyRoundCookies(5)
1 // 5! = 120, which has 1 trailing zero

countPerfectlyRoundCookies(10)
2 // 10! has 2 trailing zeros

countPerfectlyRoundCookies(100)
24
'''
def factorial(ingredients):
    if ingredients == 1:
        return 1
    elif ingredients == 2:
        return 2
    else:
        return ingredients * factorial(ingredients - 1)

def count_perfectly_round_cookies(ingredients):
    cookies = factorial(ingredients)
    round_count = 0

    # While number of cookies has at least one trailing zero (is divisible by 10), continue counting round cookies
    while cookies % 10 == 0:
        # Conduct integer division as modulo has already been checked
        cookies //= 10
        round_count += 1
    return round_count

print(count_perfectly_round_cookies(5))
print(count_perfectly_round_cookies(10))
print(count_perfectly_round_cookies(100))