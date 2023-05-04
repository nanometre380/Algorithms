from collections import deque

def solution(sequence, k):
    answer = [1000000, 2000000]
    sub = deque()
    sum_sub = 0
    for i, n in enumerate(sequence) :
        sub.append((n, i))
        sum_sub += n
        while sum_sub > k :
            sum_sub -= sub.popleft()[0]
        if sum_sub == k :
            if answer[1]-answer[0] > sub[-1][1]-sub[0][1] : 
                answer[0] = sub[0][1]
                answer[1] = sub[-1][1]
    return answer