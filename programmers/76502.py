from collections import deque

def check_right(s) :
    pair = {")" : "(", "}" : "{", "]" : "["}
    stk = []
    for c in s:
        if c == "(" or c == "[" or c == "{" :
            stk.append(c)
        elif (c == ")" or c == "]" or c == "}") and stk : 
            if pair[c] != stk[-1] :
                return False
            else : 
                stk.pop()
        else : 
            return False
    if not stk : 
        return True
    else :
        return False

def solution(s):
    queue = deque(s)
    answer = 0
    for _ in range(len(s)) :
        queue.rotate(-1)
        if check_right(queue) :
            answer += 1
    return answer