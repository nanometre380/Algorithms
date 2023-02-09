import sys
from collections import deque
input = sys.stdin.readline

def josephus(n, k) :
    circle = deque([i for i in range(1, n+1)])
    i = 1
    ans = []
    while circle :
        if i % k == 0 :
            ans.append(circle.popleft())
        else :
            circle.append(circle.popleft())
        i += 1
    return ans

n, k = map(int, input().split())
print("<" + ", ".join(map(str, josephus(n, k))) + ">")