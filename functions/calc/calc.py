# calc.py

title = "Super Calc" 
print(f"{title}".title().center(40, '='), '\n')

ops = ('+','-','*','/','//','%','**')

choices = {'c':'Calculate', 'h': "Help", 'q': "Quit"}

def alignMenu():
    print("_"*30)
    str1 = 'Select operation:'
    print('|'+str1+' '*(28-len(str1))+'|')
    print('|'+"_"*28+'|')
    l = [("| "+k+" : "+v) for (k, v) in choices.items()]
    for i in l:
        print(i.ljust(29,' ')+'|')
    print("="*30)

def menu():
    print(f"{title}".title().center(30, '='), '\n')
    alignMenu()
    choice = input("| Enter choice (" + ''.join(((i+'|') for i in choices.keys()))+"):")
    
    return str(choice.lower()) if choice.lower() != '' else 'h'

def extacts(entry, o):
    index = entry.find(o)
    if index != -1:
        a,b = entry.split(o)
        a = a.strip()
        b = b.strip()
    return (a,b,o)

def calcHelp(e=''):
    print(f"\n{e}") if e != '' else print()
    print ("""
        Usage operation:
            h                        Display this usage message
            2 + 2                    Add
            3 - 1                    Subtract
            2 * 2                    Multiply
            4 / 2                    Divide
            5 // 2                   Int Divide
            7 % 3                    Nodulo Divide
            q                        Quit
        """)

def result(a, b, operator):
    """This function return result"""

    r = False
    error = ''
    if operator == "+":
        r = lambda a, b: a + b
    elif operator == '-':
        r = lambda a, b: a - b
    elif operator == "*":
        r = lambda a, b: a * b
    elif operator == "**":
        r = lambda a, b: a ** b
    elif (operator == "/" or operator == "//" or operator == "%" ) and b==0:
        error = "Oops, division or modulo by zero"
    elif operator == "//" and b !=0:
        r = lambda a, b: a // b
    elif operator == "%" and b !=0:
        r = lambda a, b: a % b
    elif operator == "/" and b !=0:
        r = lambda a, b: a / b
    else:
        error = "Use either + - * / or % next time"
    return r(a, b), error

while True:
    choice = menu()

    if choice == 'q':
        print('{!s}'.format('Thank You for using calculator.py!'))
        break 
    
    if choice == 'h':
        calcHelp()
        continue

    if choice == 'c':
        entry = input("Enter x operator y: ")
        for o in ops:
            if entry.count(o) == 1:
                x,y,operator = extacts(entry,o)
            elif entry.count(o) == 2:
                x,y,operator = extacts(entry,2*o)

        if operator not in ops:
            calcHelp()
            continue
        
        a = float(x)
        b = float(y)
        
        res, err = result(a, b, operator)
        if res != False:
            print(f"{a} {operator} {b} = {res}")
        else:
            print(f"{err}")
