import math
def solution(w,h):
    gcd = math.gcd(w, h)
    answer = w*h-gcd*((w//gcd)+(h//gcd)-1)
    return answer