from collections import deque
def solution(elements):
    len_arr = len(elements)
    queue = deque(elements)
    counts_sum = set()
    for i in range(len_arr) :
        temp = 0
        for j in range(len_arr) :
            temp += queue[j]
            counts_sum.add(temp)
        queue.rotate(1)
    return len(counts_sum)