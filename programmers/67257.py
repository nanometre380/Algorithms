from itertools import permutations
from collections import deque
import re

def calc_temp(n1, n2, p) :
    if p == "+" :
        return int(n1)+int(n2)
    elif p == "-" :
        return int(n1)-int(n2)
    elif p == "*" :
        return int(n1)*int(n2)

def calc(expressions, p) :
    i = 0
    j = 0
    queue = [deque() for _ in range(4)]
    queue[0] = deque(expressions)
    for i, c in enumerate(p, start=1) :
        prev = ""
        for j in range(len(queue[i-1])) :
            if queue[i-1][j]== prev :
                prev = ""
                continue
            if queue[i-1][j] == c :
                n1 = queue[i].pop()
                n2 = queue[i-1][j+1]
                queue[i].append(calc_temp(n1, n2, c))
                prev = n2
            else : 
                queue[i].append(queue[i-1][j])
    return abs(queue[3][0])

def solution(expression):
    priorities = permutations(["+", "-", "*"], 3)
    expressions = re.split('([-|+|*])', expression)
    answer = 0
    for p in priorities :
        answer = max(answer, calc(expressions, p))
    return answer
