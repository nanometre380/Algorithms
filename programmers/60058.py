def split_string(p) :
    u = ""
    v = ""
    cnt_l = 0
    cnt_r = 0
    toggle = 'u'
    for c in p : 
        if toggle == 'v' :
            v += c
        if c == "(" and toggle == 'u' : 
            cnt_l+=1
            u += "("
        elif c == ")" and toggle == 'u':
            cnt_r += 1
            u += ")"
        if cnt_l == cnt_r :
            toggle = 'v'
    return u, v

def check_right(u) : 
    stk = []
    for c in u : 
        if c == '(' :
            stk.append(c)
        elif c == ')' and stk:
            stk.pop()
        else :
            return False
    if not stk : 
        return True
    
def make(p) :
    v = p[:]
    result = ""
    if v == "" :
        return ""
    u, v = split_string(v)
    if check_right(u) == True : 
        return u+make(v)
    else : 
        temp = u[-2:0:-1]
        result += ("(" + make(v) + ")" + temp)
        return result
        
def solution(p):
    answer = ''
    if check_right(p) == True :
        return p
    return make(p)

p = "()))((()"

print(solution(p))