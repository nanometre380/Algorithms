import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
skills = list(map(int, input().split()))
answer = deque()

for i in range(1, n+1) :
    skill = skills[-i]
    if skill == 1 :
        answer.appendleft(i)
    elif skill == 2 :
        temp = answer.popleft()
        answer.appendleft(i)
        answer.appendleft(temp)
    else :
        answer.append(i)
print(*answer)