import sys
input = sys.stdin.readline

n = int(input())
thinks = [int(input()) for _ in range(n)]
result = 0

for i in range(n) :
    if thinks[i] >= i :
        result += (thinks[i]-i)
    else :
        break

print(result)