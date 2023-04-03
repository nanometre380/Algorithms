from collections import deque
def solution(name):
    answer = 0
    for c in name :
        answer += ord(c)-65 if ord(c)<79 else -(ord(c)-91)
    min_move = len(name)-1
    indices = [i for i, c in enumerate(name) if c == 'A']
    len_name = len(name)
    check = [False for _ in range(len_name)]
    
    for i in indices :
        check[i] = True
    check[0] =True
    def get_move(x, cnt) :
        nonlocal min_move
        if check.count(False) == 0 :
            min_move = min(cnt, min_move)
            return
        if cnt > min_move :
            return
        if x+1 >= len_name :
            flag = 0
            if check[0] == True :
                flag = 1
            else :
                check[0] = True
            get_move(0, cnt+1)
            if flag != 1 :
                check[0] = False
        else : 
            flag = 0
            if check[x+1] == True :
                flag = 1
            else :
                check[x+1] = True
            get_move(x+1, cnt+1)
            if flag != 1 :
                check[x+1] = False
        if x-1 < 0 :
            flag = 0
            if check[len_name-1] == True :
                flag = 1
            else :
                check[len_name-1] = True
            get_move(len_name-1, cnt+1)
            if flag != 1 :
                check[len_name-1] = False
        else : 
            flag = 0
            if check[x-1] == True :
                flag = 1
            else :
                check[x-1] = True
            get_move(x-1, cnt+1)
            if flag != 1 :
                check[x-1] = False
    get_move(0, 0)
    answer += min_move
    return answer