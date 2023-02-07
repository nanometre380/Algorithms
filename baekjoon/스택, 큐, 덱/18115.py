import sys
from collections import deque
input = sys.stdin.readline

before = deque()
after = deque([i for i in range(1, int(input())+1)])

def rev_one(before, after) :
    before.appendleft(after.popleft())
    return before, after

def rev_two(before, after) :
    before.insert(1, after.popleft())
    return before, after

def rev_three(before, after) :
    before.append(after.popleft())
    return before, after

skills = list(map(int, input().split()))

for skill in skills[::-1] :
    if skill == 1 :
        before, after = rev_one(before, after)
    elif skill == 2 :
        before, after = rev_two(before, after)
    elif skill == 3 :
        before, after = rev_three(before, after)

print(*before)