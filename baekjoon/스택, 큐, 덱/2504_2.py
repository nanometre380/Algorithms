import sys
input = sys.stdin.readline

def calc(arr) :
    paren = {')' : '(', ']' : '['}
    val = {'(' : 2, ')' : 2, '[' : 3, ']' : 3}
    stk = []
    temp = 1
    ans = 0
    for idx, i in enumerate(arr) :
        if i == ')' or i == ']' :
            if paren[i] == stk[-1] :
                stk.pop()
                if len(arr) > 0 and (arr[idx-1] == '(' or arr[idx-1] == '['):
                    ans +=temp
                temp = temp//val[i]
            else :
                return 0
        else :
            stk.append(i)
            temp *= val[i]
            
    if not stk :
        return ans
    else :
        return 0

arr = input().rstrip()
print(calc(arr))

        