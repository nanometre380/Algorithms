def solution(s):
    stk = []
    for p in s : 
        if p == "(" :
            stk.append(p)
        elif p == ")" and len(stk) != 0 : 
            stk.pop()
        else :
            return False
    if len(stk) != 0 :
        return False
    else :
        return True