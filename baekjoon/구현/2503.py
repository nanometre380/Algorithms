# 1~9까지의 숫자 세 개로 구성된 세자리수
# 하나가 동일한 위치면 스트라이크, 다른 자리에 있으면 볼

import sys
from itertools import permutations
input = sys.stdin.readline

def check_baseball(number, q) :
    s = 0
    b = 0
    for i in range(len(q)) :
        if q[i] == number[i] :
            s += 1
        elif q[i] in number :
            b += 1
    return s, b

def count_baseball(questions) :
    numbers = [str(i) for i in range(1, 10)]
    cases = list(permutations(numbers, 3))
    for q, s, b in questions :
        temp = []
        for case in cases :
            s2, b2 = check_baseball(case, q)
            if s == str(s2) and b == str(b2) :
                temp.append(case)
        cases = list(set(temp))
    return len(cases)

n = int(input())
questions = [list(input().split()) for _ in range(n)]
print(count_baseball(questions))


