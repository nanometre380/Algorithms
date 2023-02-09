import sys
input = sys.stdin.readline

def getnumber(n, k) :
    isPrime = [True for _ in range(n+1)]
    isPrime[0] = False
    isPrime[1] = False
    cnt = 0
    for i in range(2, n+1) :
        if isPrime[i] == False :
            continue
            
        for j in range(i, n+1, i) :
            if isPrime[j] == False :
                continue
            isPrime[j] = False
            cnt += 1
            if cnt == k :
                return j
    return -1

n, k = map(int, input().split())
print(getnumber(n, k))