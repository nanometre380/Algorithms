import sys
input = sys.stdin.readline

last_digit = [[i] for i in range(10)]
size = []

for i in range(10) :
    temp = i
    while i != (temp*i)%10 :
        temp *= i
        last_digit[i].append(temp%10)
    size.append(len(last_digit[i]))

n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    a = a%10
    b = b%size[a]-1
    print(10 if a == 0 else last_digit[a][b])