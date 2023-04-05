import math

def solution(k, d):
    result = 0
    for x in range(0, d+1, k) :
        y = math.floor(math.sqrt(d**2 - x**2))
        result += y//k+1
    return result