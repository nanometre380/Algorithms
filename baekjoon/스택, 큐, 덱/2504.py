import sys
input = sys.stdin.readline

paren = []
numbers = []
pair = {')' : '(', ']' : '['}
values = {'(' : 2, ')' : 2, ']' : 3, '[' : 3}

def calc(arr) : 
    ans = 0
    temp = 1
    for i in range(len(arr)) :
        if arr[i] == '(' or arr[i] =='[' :
            paren.append(arr[i])
            temp*=values[arr[i]]
        elif arr[i] == ')' or arr[i] == ']' :
            if paren and pair[arr[i]] == paren[-1] :
                paren.pop()
                if arr[i-1] == '(' or arr[i-1] == '[' :
                    ans += temp
                temp = temp//values[arr[i]]
            else :
                return 0
    if paren : 
        return 0
    else :
        return ans

arr = input().rstrip()
print(calc(arr))
        