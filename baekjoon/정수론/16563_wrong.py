import sys
input = sys.stdin.readline

def era(n) :
    isPrime = [True for _ in range(n+1)]
    isPrime[0] = False
    isPrime[1] = False
    prime_list = []
    for i in range(int(n**(1/2)+1)) :
        if not isPrime[i] :
            continue
        for j in range(i*i, n+1, i) :
            if not isPrime[j] :
                continue
            isPrime[j] = False
    for v in range(len(isPrime)) : 
        if isPrime[v] == True :
            prime_list.append(v)
    return prime_list

def divide(n, prime_list) :
    div_prime = []
    i = 0
    while n != 1 :
        if n%prime_list[i] == 0 :
            div_prime.append(prime_list[i])
            n //= prime_list[i]
        else : 
            i += 1
    print(' '.join(map(str, div_prime)))

n = int(input())
arr = list(map(int, input().split()))
prime_list = era(max(arr))
for i in arr :
    divide(i, prime_list)