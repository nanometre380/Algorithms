def move(cur, direction) :
    new = []
    if direction == "U" :
        new = (cur[0], cur[1]+1)
    elif direction == "D" :
        new = (cur[0], cur[1]-1)
    elif direction == "R" :
        new = (cur[0]+1, cur[1])
    elif direction == "L" :
        new = (cur[0]-1, cur[1])
    if (new[0] < -5 or new[0] > 5) or (new[1] < -5 or new[1] > 5) :
        return cur
    else :
        return new
    
def solution(dirs):
    answer = 0
    routes = set()
    cur = [0,0]
    temp1 = ()
    temp2 = ()
    for c in dirs :
        nxt = move(cur, c)
        if cur == nxt :
            continue
        else :
            temp1 = (*cur, *nxt)
            temp2 = (*nxt, *cur)
            if temp1 not in routes or temp2 not in routes : 
                answer += 1
                routes.add(temp1)
                routes.add(temp2)
            cur = nxt
    return answer