from collections import deque

def solution(priorities, location):
    queue =  [(p, i) for i, p in enumerate(priorities)]
    queue = deque(queue)
    answer = 0
    while True : 
        print(queue)
        
        max_q = max(queue)
        temp = queue.popleft()
        answer += 1
        if temp[0] < max_q[0] :
            answer -= 1
            queue.append(temp)
        else :
            if temp[1] == location :
                return answer
            
print(solution([1, 1, 9, 1, 1, 1], 0))