from collections import deque

def solution(progresses, speeds):
    queue = deque(progresses)
    speed_q = deque(speeds)
    answer = []
    check = 0
    while queue :
        check += 1
        for i in range(len(queue)) :
            queue[i] += speed_q[i]
        cnt = 0
        while queue and queue[0] >= 100 : 
            queue.popleft()
            speed_q.popleft()
            cnt += 1
        if cnt != 0 : 
            answer.append(cnt)
    return answer