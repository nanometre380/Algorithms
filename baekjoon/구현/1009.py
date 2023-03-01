# 분산처리
# 컴퓨터 1대~10대 - 1번 데이터는 1번 컴퓨터 ... 11번 데이터는 1번 컴퓨터...
# 데이터 개수 a^b   %10+1
# 마지막 데이터가 처리될 컴퓨터의 번호

import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    a = a%10
    b = b%4
    if b == 0 : 
        b = 4
    com = (a**b)%10
    print(com if com != 0 else 10)