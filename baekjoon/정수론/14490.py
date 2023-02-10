# 약분하기
# n:m이 주어지면 n:m을 최대한 약분하기
# 최대 공약수를 구해서 나눠주기

import sys
input = sys.stdin.readline

def get_gcd(a, b) :
    while b != 0 :
        a %= b
        a, b = b, a
    return a

n, m = map(int, input().split(':'))
gcd = get_gcd(max(n, m), min(n, m))
print(str(n//gcd)+":"+str(m//gcd))

