import heapq as hq

def solution(n, works):
    answer = 0
    heap_list = []
    for i in works :
        hq.heappush(heap_list, (-i, i))
    
    for j in range(n) :
        _, temp = hq.heappop(heap_list)
        if temp == 0 :
            return 0
        hq.heappush(heap_list, (-(temp-1), temp-1))
    
    for _, k in heap_list : 
        answer += k**2
    return answer