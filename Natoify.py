'''
Make a translation function for the NATO phonetic alphabet. 

Example:
print(natoify('hello world'))
"Hotel Echo Lima Lima Oscar (space) Whiskey Oscar Romeo Lima Delta"

print(natoify('3spooky5me'))
"Three Sierra Papa Oscar Oscar Kilo Yankee Five Mike Echo"
'''
def natoify(message):
    message = message.lower()
    nato_alphabet = {
        'a':'Alpha',
        'b':'Bravo',
        'c':'Charlie',
        'd':'Delta',
        'e':'Echo',
        'f':'Foxtrot',
        'g':'Golf',
        'h':'Hotel',
        'i':'India',
        'j':'Juliet',
        'k':'Kilo',
        'l':'Lima',
        'm':'Mike',
        'n':'November',
        'o':'Oscar',
        'p':'Papa',
        'q':'Quebec',
        'r':'Romeo',
        's':'Sierra',
        't':'Tango',
        'u':'Uniform',
        'v':'Victor',
        'w':'Whiskey',
        'x':'X-ray',
        'y':'Yankee',
        'z':'Zulu',
        ' ':'(space)',
        '1':'One',
        '2':'Two',
        '3':'Three',
        '4':'Four',
        '5':'Five',
        '6':'Six',
        '7':'Seven',
        '8':'Eight',
        '9':'Nine'
    }
    natoified = ""
    for character in message:
        natoified += ' ' + nato_alphabet[character]

    return natoified

print(natoify('hello world'))
print(natoify('3spooky5me'))