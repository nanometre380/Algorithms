import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0

a.sort()
b.sort(reverse=True)

for i in range(n) :
    s += a[i]*b[i]

print(s)