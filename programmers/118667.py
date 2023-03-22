from collections import deque

def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    sum_1, sum_2 = sum(queue1), sum(queue2)
    for i in range(len(queue1)*4) :
        if sum_1 == sum_2 : 
            return i
        elif sum_1 > sum_2 :
            num = queue1.popleft()
            queue2.append(num)
            sum_1 -= num
            sum_2 += num
        else : 
            num = queue2.popleft()
            queue1.append(num)
            sum_2 -= num
            sum_1 += num
    return -1