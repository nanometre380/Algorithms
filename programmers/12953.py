"""
def check_lcm(i, arr) :
    for n in arr :
        if i%n != 0 :
            return False
    return True

def solution(arr):
    answer = 0
    max_c = "*".join(map(str, arr))
    max_c = eval(max_c)
    gap = max(arr)
    for i in range(gap, max_c+1, gap) :
        if check_lcm(i, arr) == True :
            return i
    return answer
"""

import math

def solution(arr) :
    answer = arr[0]
    for i in range(1, len(arr)) :
        answer = answer*arr[i]//math.gcd(answer, arr[i])
    return answer