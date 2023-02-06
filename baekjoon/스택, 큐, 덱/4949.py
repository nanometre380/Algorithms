import sys

input = sys.stdin.readline

def check(line) :
    pair = []
    p = {')' : '(', ']' : '['}
    for c in line : 
        if c == '(' or c == '[' :
            pair.append(c)
        elif (c == ')' or c == ']') :
            if len(pair) > 0 and (p[c] == pair[-1]) :
                pair.pop()
            else :
                return False
    if len(pair) == 0 :
        return True
    else :
        return False
             
while True : 
    line = input()
    if line.rstrip()=="." :
        break
    if check(line) :
        print("yes")
    else :
        print("no")