import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

circle = deque([i for i in range(1, n+1)])
ans = []

while circle :
    circle.rotate(-k+1)
    ans.append(circle.popleft())

print("<" + ", ".join(map(str, ans)) + ">")