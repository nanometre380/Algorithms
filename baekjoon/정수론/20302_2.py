#민트초코
#수식의 결과가 정수면 민트초코, 유리수이면 치약
# 모든 정수는 -100000 이상 100000 이하
# 코드 정리해서 다시 풀어보기

import sys
from collections import Counter
input = sys.stdin.readline

def make_primelist() :
    primelist = [i for i in range(10**6+1)]
    for i in range(2, 10**6+1) :
        if primelist[i] != i :
            continue
        for j in range(i*i, 10**6+1, i) :
            if primelist[j] != j :
                continue
            primelist[j] = i
    return primelist

def get_primelist(primelist, n) :
    primes = []
    while n != 1 :
        primes.append(primelist[n])
        n//=primelist[n]
    return primes

def deter_mint(formula, primelist) :
    count_exp = [0 for _ in range(10**6+1)]
    for c in range(len(formula)) :
        if c%2 != 0 :
            continue
        if c == 0 or formula[c-1] == '*':
            if formula[c] == '0' :
                return "mint chocolate"
            c_abs = abs(int(formula[c]))
            primes = get_primelist(primelist, c_abs)
            for p in primes : 
                count_exp[p] += 1
        else : 
            c_abs = abs(int(formula[c]))
            primes = get_primelist(primelist, c_abs)
            for p in primes :
                count_exp[p] -= 1
        #print(count_exp)
    for i in count_exp :
        if i < 0 :
            return "toothpaste"
    return "mint chocolate"


n = int(input())
primelist = make_primelist()
formula = list(input().split())
print(deter_mint(formula, primelist))