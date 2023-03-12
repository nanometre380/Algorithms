from collections import deque

def conversion(n) :
    ans = deque()
    numbers = ['1', '2', '4']
    while n >= 1 :
        tmp = n%3
        n //= 3
        if tmp == 0 :
            tmp = 3
            n-=1
        ans.appendleft(numbers[tmp-1])
    return ans

def solution(n):
    answer = ''
    answer = "".join(conversion(n))
    return answer