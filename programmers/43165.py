"""
cnt = 0
def make_target(numbers, target, result, idx) :
    global cnt
    if idx == len(numbers) :
        if target == result : 
            cnt += 1
        return
    make_target(numbers, target, result+numbers[idx], idx+1)
    make_target(numbers, target, result-numbers[idx], idx+1)

def solution(numbers, target):
    answer = 0
    make_target(numbers, target, 0, 0)
    return cnt

numbers = [4, 1, 2, 1]
target = 4
solution(numbers, target)
print(cnt)
"""
from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    print(l)
    print(list(product(*l)))
    s = list(map(sum, product(*l)))
    return s.count(target)

numbers = [4, 1, 2, 1]
target = 4
solution(numbers, target)

