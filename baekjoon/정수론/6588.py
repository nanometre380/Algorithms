# 4보다 큰 모든 짝수는 두 홀수인 소수의 합으로 나타낼 수 있다.
# 테스트 케이스를 입력하면 n = a+b 형태로 출력
# n을 만들 수 잇는 방법이 여러가지면 b-a가 가장 큰 것을 출력

import sys
input = sys.stdin.readline

def prime_list() :
    primes = [True for _ in range(10**6+1)]
    primes[0] = False
    primes[1] = False
    for i in range(2, 10**6+1) : # int(루트값)+1 까지로 해도 됨
        if primes[i] == False :
            continue
        for j in range(i*i, 10**6+1, i) :
            if primes[j] ==False :
                continue
            primes[j] = False
    primes[2] = False
    return primes

def get_numbers(q, primes) :
    for i in range(3, q//2+1, 2) : # 3에서 n//2까지의 홀수만 검사하기 위해
        if primes[i] == False :
            continue
        if primes[q-i] == False :
            continue
        print("%d = %d + %d" %(q, i, (q-i)))
        return
    print("Goldbach's conjecture is wrong.")
    return

q = 1
primes = prime_list()
while True :
    q = int(input()) 
    if q == 0 :
        break
    ans = get_numbers(q, primes)
