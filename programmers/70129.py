from collections import deque

def calc_bin(s) :
    res = deque()
    length = len(s)
    while length > 0 :
        res.appendleft(str(length % 2))
        length //= 2
    return "".join(res)

def convert(s) :
    cnt = 0
    n_zero = 0
    while s != "1" :
        cnt += 1
        n_zero += s.count("0")
        s = s.replace("0", "")
        s = calc_bin(s)
    return cnt, n_zero
        

def solution(s):
    answer = []
    answer = convert(s)
    return answer