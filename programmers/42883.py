from collections import deque

def solution(number, k):
    temp = ""
    answer = []
    num_q = deque(number)
    answer.append(num_q.popleft())
    t_length = len(number)-k
    while num_q :
        temp = num_q.popleft()
        while answer and temp > answer[-1] and len(num_q) >= t_length-len(answer) :  
            answer.pop()
        if len(answer) < t_length : 
            answer.append(temp)

    return "".join(answer)