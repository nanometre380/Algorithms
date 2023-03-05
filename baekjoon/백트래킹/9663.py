# N-queen
# NxN인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 것
# N이 주어졌을 때, 퀸을 놓는 방법의 수
# 퀸 - 퀸이 놓이면 가로세로대각선에 위치한 곳엔 다른 퀸을 둘 수 없음

import sys
input = sys.stdin.readline

check_col = [False for _ in range(16)] #행이 index라고 생각
check_left = [False for _ in range(30)]
check_right = [False for _ in range(30)]
queens = []
ans = 0

def get_queen(i) :
    global ans
    if i == n :
        ans += 1
        return
    for j in range(0, n) :
        if check_col[j] == True or check_left[i+j] == True or check_right[i-j+n] == True :
            continue
        check_col[j] = True
        check_left[i+j] = True
        check_right[i-j+n] = True
        get_queen(i+1)
        check_col[j] = False
        check_left[i+j] = False
        check_right[i-j+n] = False

n = int(input())
get_queen(0)
print(ans)

    
