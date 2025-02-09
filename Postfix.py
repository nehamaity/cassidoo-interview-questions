'''
Write a function that evaluates a postfix expression (also known as Reverse Polish Notation) 
and returns the result. The expression will contain single-digit integers and the operators +, -, *, and /. 
You can assume the input is always a valid expression! 
'''
def evaluate_postfix(expression):
    calculation = None
    last_index = 0

    for c in expression:

        # Get substring for each operation
        if c in '*/+-':

            # First operation in expression
            if last_index == 0:
                substring = expression[:expression.index(c)]

            # Subsequent operation in expression, get substring based on last operation index
            else:
                substring = expression[last_index:expression.index(c)]

            # Save last operation index for next operation
            last_index = expression.index(c)

            # Perform calculation according to substring operation
            for v in substring:
                if v.isdigit():
                    v = int(v)

                    # Initialize calculation value to first numerical value
                    if calculation == None:
                        calculation = v
                    
                    # Operation can be performed otherwise
                    else:
                        if c == '*':
                            calculation *= v
                        elif c == '/':
                            calculation //= v
                        elif c == '+':
                            calculation += v
                        elif c == '-':
                            calculation -= v

    return calculation


print(evaluate_postfix('12+'))
# 3

print(evaluate_postfix('56+7*'))
# 77

print(evaluate_postfix('23+6*3/5-'))
# 5





                

