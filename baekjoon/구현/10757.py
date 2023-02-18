import sys
from collections import deque
input = sys.stdin.readline

def paste_zero(std, old) :
    new = ""
    for i in range(len(old), len(std)) :
        new += "0"
    return new+old

n1, n2 = map(str, input().split())
number = deque()
up = 0
if len(n1) > len(n2) :
    n2 = paste_zero(n1, n2)
else : 
    n1 = paste_zero(n2, n1)

for i in range(1, len(n1)+1, 1) :
    n = int(n1[-i]) + int(n2[-i]) + up
    up = n//10
    n = n%10
    number.appendleft(n)
if up != 0 :
    number.appendleft(up)

print("".join(map(str, number)))