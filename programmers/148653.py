from collections import deque

def bfs(storey, n) :
    queue = deque()
    queue.append([storey, 0, 10])
    min_cnt = storey
    while queue :
        cur, cnt, temp = queue.popleft()
        #print(cur, cnt, temp)
        if cur == 0 :
            min_cnt = min(min_cnt, cnt)
        elif cur == n*10 : 
            continue
        else : 
            queue.append([cur-(cur%temp), cnt+(cur%temp)//(temp//10), temp*10])
            queue.append([(cur//temp+1)*temp, cnt+(((cur//temp+1)*temp-cur))//(temp//10), temp*10])
            #print("CUR :", cur, "TEMP : ", temp, "CNT M : ", (((cur//temp+1)*temp-cur)))
    return min_cnt

def solution(storey):
    answer = 0
    n = 1
    for i in range(len(str(storey))) :
        n*=10
    answer = bfs(storey, n)
    return answer