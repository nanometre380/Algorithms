import heapq as hq

def solution(scoville, K):
    answer = -1
    hq.heapify(scoville)
    count = 0
    while scoville :
        if scoville[0] >= K :
            answer = count
            break
        if len(scoville) < 2 :
            break
        a1 = hq.heappop(scoville)
        a2 = hq.heappop(scoville)
        new = a1 + a2*2
        hq.heappush(scoville, new)
        count += 1
    return answer