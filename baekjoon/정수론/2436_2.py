# 공약수
# 두 개의 자연수가 주어졌을 떄 A를 최대공약수, B를 최소공배수로 하는 자연수 구하기
# 최대공약수 gcd * lcm = A*B
# 두 수의 곱이 최대공약수와 최소공배수의 곱과 같아야 함
# A = gcd*a / B = gcd*b / a*b = lcm//gcd
#

import sys
input = sys.stdin.readline

def calc_gcd(a, b) :
    if b == 0 :
        return a
    return calc_gcd(b, a%b)
    

gcd, lcm = map(int, input().split())

ab = lcm//gcd
a = 0
b = 0
for d in range(int(ab**(1/2)), 0, -1) :
    if ab%d == 0 :
        a = d
        b = ab//a
        if calc_gcd(a, b) == 1 :
            print(a*gcd, b*gcd)
            break
