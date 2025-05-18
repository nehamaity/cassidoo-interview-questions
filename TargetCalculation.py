# Given two integers origin and target, add operators in the origin number to make it equal target, if possible. 
def operation(string_num, operator, target):
    calc = int(string_num[0])
    if operator == '*':
        for n in string_num[1:]:
            calc *= int(n)
    elif operator == '+':
        for n in string_num[1:]:
            calc += int(n)
    elif operator == '/':
        for n in string_num[1:]:
            try:
                calc /= int(n)
            except:
                return None
    elif operator == '-':
        for n in string_num[1:]:
            calc -= int(n)

    string = string_num[0]
    if calc == target:
        if operator == '*':
            for n in string_num[1:]:
                string += '*' + n
        elif operator == '+':
            for n in string_num[1:]:
                string += '+' + n
        elif operator == '/':
            for n in string_num[1:]:
                string += '/' + n
        elif operator == '-':
            for n in string_num[1:]:
                string += '-' + n
    if string == string_num[0]:
        return None
    return string

def add_operators(origin, target):
    string_num = str(origin)
    results = []
    multiply = operation(string_num, '*', target)
    add = operation(string_num, '+', target)
    divide = operation(string_num, '/', target)
    sum = operation(string_num, '-', target)
    calculations = [multiply, add, divide, sum]

    for c in calculations:
        if c != None:
            results.append(c)
    return results

print(add_operators(123, 6))
# ['1*2*3', '1+2+3']
print(add_operators(3456237490, 9191))
# [] 