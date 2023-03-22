from collections import deque

def solution(x, y, n):
    dist = [0 for _ in range(y+1)]
    queue_c = deque()
    queue_c.append(x)
    answer = 0
    if x == y :
        return 0
    while queue_c :
        prev = queue_c.popleft()
        for i in range(3) :
            if i == 0 : 
                cur = prev+n
            elif i == 1 :
                cur = prev*2
            elif i == 2 : 
                cur = prev*3
            if cur > y or dist[cur] :
                continue
            if cur == y :
                return dist[prev]+1
            dist[cur] = dist[prev]+1
            queue_c.append(cur)
    return -1