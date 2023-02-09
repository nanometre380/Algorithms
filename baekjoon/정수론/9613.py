import sys
input = sys.stdin.readline

def gcd(a, b) :
    while b != 0 :
        a%=b
        a, b = b, a
    return a

n = int(input())
for _ in range(n) :
    total = 0
    case = list(map(int, input().split()))
    for i in range(1,len(case)) :
        for j in range(i+1, len(case)) :
            total += gcd(case[i], case[j])
    print(total)
