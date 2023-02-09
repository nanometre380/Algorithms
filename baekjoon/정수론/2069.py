import sys
input = sys.stdin.readline

a, b = map(int, input().split())
ab = a*b
while b != 0 :
    a%=b
    a, b = b, a
print(a)
print(ab//a)