import sys
input = sys.stdin.readline

def primelist() :
    primes = [i for i in range(10**6+1)]
    
    for i in range(2, (10**3)+1) :
        if primes[i] != i :
            continue
        for j in range(i*i, 10**6+1, i) :
            if primes[j] != j :
                continue
            primes[j] = i
    return primes

def calc_exp(exponents, n, flag, primes) :
    while n > 1 :
        exponents[primes[n]] += flag
        n//=primes[n]
    return exponents

def deter_mint(arr) :
    flag = 0
    exponents = [0 for _ in range(10**6+1)]
    primes = primelist()
    for i in range(len(arr)) :
        if i%2 == 0 :
            continue

        num = abs(int(arr[i]))
        if arr[i-1] == '*' :
            flag = 1
            if int(num) == 0 :
                return "mint chocolate"
        
        elif arr[i-1] == '/' :
            flag = -1

        exponents = calc_exp(exponents, num, flag, primes)
    
    for i in exponents :
        if i < 0 : 
            return "toothpaste"
    return "mint chocolate"

n = int(input())
arr = input().rstrip().split()
print(deter_mint(['*'] + arr))