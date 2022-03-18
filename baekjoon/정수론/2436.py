import sys

input = sys.stdin.readline

def check_prime(a, b) :     # 두 수의 소수를 구하기 위한 함수
    if b == 0 :
        return a
    else :
        return check_prime(b, a%b)

def find_numbers(gcd, lcm) :    # a와 b를 구해서 리턴하는 함수
    """
    A = gcd * a, B = gcd * b (a와 b는 서로소) 라고 나타낼 수 있음
    A * B = gcd * lcm = gcd * gcd * a * b 가 되므로
    a * b = lcm / gcd
    A와 B는 a, b에 gcd만 곱하면 되기 때문에 차가 최소가 되는 a, b를 찾으면 됨
    """
    ab = lcm//gcd
    a = 0
    b = 0
    for i in range(int(ab**(1/2)), 0, -1) :
        if ab%i != 0 :
            continue
        else :
            a = i
            b = ab//i
            if check_prime(max(a, b), min(a, b)) == 1 :
                return a, b
    return a, b

gcd, lcm = map(int, input().split())

a, b = find_numbers(gcd, lcm)
print(a * gcd, b * gcd)