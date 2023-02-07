import sys
from collections import deque
input = sys.stdin.readline

priority = {'(' : 3, ')' : 3, '*' : 1, '/' : 1, '+' : 2, '-' : 2}

formula = input().rstrip()
ans = []
symbol = []

for c in formula : 
    if c not in priority : 
        ans.append(c)
    elif c == ')' :
        while symbol[-1] != '(' :
            ans.append(symbol.pop())
        symbol.pop()
    elif c == '(' :
        symbol.append(c)
    else :
        if symbol and priority[c] >= priority[symbol[-1]] :
            while symbol :
                ans.append(symbol.pop())
        symbol.append(c)
    print(symbol)
while symbol :
    ans.append(symbol.pop())

print("".join(ans))
