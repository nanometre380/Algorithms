import sys
from collections import deque
input = sys.stdin.readline

num = int(input())

cards = deque([i for i in range(1, num+1)])

for _ in range(num) :
    if len(cards) == 1:
        print(*cards)
        break
    cards.popleft()
    cards.append(cards.popleft())