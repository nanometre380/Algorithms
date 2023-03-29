# 2020 카카오 인턴십 - 수식 최대화
"""
stack을 연산자 개수만큼 만들어서 우선 순위대로 순차적으로 계산해 나가는 방법
"""
"""
from itertools import permutations
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
    stk = [[] for _ in range(4)]
    stk[0] = expressions
    for i, c in enumerate(p, start=1) :
        prev = ""
        for j in range(len(stk[i-1])) :
            if stk[i-1][j]== prev :
                prev = ""
                continue
            if stk[i-1][j] == c :
                n1 = stk[i].pop()
                n2 = stk[i-1][j+1]
                stk[i].append(calc_temp(n1, n2, c))
                prev = n2
            else : 
                stk[i].append(stk[i-1][j])
    return abs(stk[3][0])

def solution(expression):
    priorities = permutations(["+", "-", "*"], 3)
    expressions = re.split('([-|+|*])', expression)
    answer = 0
    for p in priorities :
        answer = max(answer, calc(expressions, p))
    return answer
"""
"""
문자열을 이용한 방법
"""
from itertools import permutations

def solution(expression) :
    op_cases = permutations(["+", "-", "*"], 3)
    answer = 0
    for case in op_cases :
        op1, op2, op3 = case
        temp = []
        joined_temp = []
        for sp in expression.split(op1) :
            temp = [f'({s})' for s in sp.split(op2)]
            joined_temp.append(f'({op2.join(temp)})')
        joined = op1.join(joined_temp)
        answer = max(answer, abs(eval(joined)))
    return answer
