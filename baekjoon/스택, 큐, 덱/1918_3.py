import sys
input = sys.stdin.readline

def make_formula(arr) :
    priority = {'*' : 1, '/' : 1, '+' : 2, '-' : 2, '(' : 3, ')' : 3}
    symbol = []
    ans = []
    for c in arr :
        if c not in priority :
            ans.append(c)
        elif c == '(' :
            symbol.append(c)
        elif c == ')' :
            while symbol and symbol[-1] != '(' :
                ans.append(symbol.pop())
            symbol.pop()
        else : 
            while symbol and priority[c] >= priority[symbol[-1]] :
                ans.append(symbol.pop())
            symbol.append(c)
    while symbol :
        ans.append(symbol.pop())
    return ans

formula = input().rstrip()
print("".join(make_formula(formula)))