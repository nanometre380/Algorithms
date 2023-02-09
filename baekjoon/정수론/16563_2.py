import sys
input = sys.stdin.readline

def era(n) :
    check = [0 for _ in range(n+1)]
    for i in range(2, n+1) :
        if check[i] != 0 :
            continue
        for j in range(i, n+1, i) :
            if check[j] != 0 :
                continue
            check[j] = i
    return check

def trace(n, check) :
    ans = []
    while n != 1 :
        ans.append(check[n])
        n//=check[n]
    print(' '.join(map(str, ans)))

n = int(input())
numbers = list(map(int, input().split()))
check = era(max(numbers))
for num in numbers : 
    trace(num, check)
