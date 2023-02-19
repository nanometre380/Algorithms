# 모든 자연수는 1~4개의 제곱수의 합
# n을 최소 개수의 제곱수 합으로 표현하라
# n은 50,000

import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

def get_answer(n) :
    if n**(1/2) == int(n**(1/2)) :
            return 1
    for i in range(2, 4) :
        li = [j**2 for j in range(1, int(n**(1/2))+1)]
        candid = combinations_with_replacement(li, i)
        for c in candid :
            total = sum(c)
            if total == n :
                return i
    return 4

n = int(input())
print(get_answer(n))
