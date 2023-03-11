# 컨베이어 벨트 위의 로봇
# 길이가 N인 컨베이어 벨트와, 길이가 2N인 벨트가 감싸고 돌고 있음
# 칸은 2N개 1,2,3 -- N - N+1 -- 2N 둘글게 번호가 매겨져 있음
# 벨트가 한 칸 회전하면 한칸 돌고, i번 칸의 내구도는 A_i
# 1번 칸 위치를 "올리는 위치" N번 칸이 있는 위치를 "내리는 위치"
# 올리는 위치에서 로봇을 올리고 내리는 위치에서 내림
# 로봇이 올라가면 내구도는 1만큼 감소
# 1. 벨트가 회전 - 2. 로봇 이동(이동하려는 칸에 로봇이 없거나 내구도가 1 이상이어야 함)
# 3. 내구도가 0이 아니면 올리는 위치에 로봇을 올림
# 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정을 종료

# deque index 0 - 내리는 위치 / n-1 : 올리는 위치
# 내구도 deque 로봇 위치 deque

import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))
robot = deque([False for _ in range(2*n)])
#robot[n-1] = True
cnt = 0
step = 0
up_idx = 0
down_idx = n-1

while True :
    step += 1
    a.rotate(1)
    robot.rotate(1)
    robot[down_idx] = False
    for i in range(n-2, -1, -1) :
        if robot[i] and robot[i+1] != True and a[i+1] > 0 :
            robot[i+1] = True
            robot[i] = False
            a[i+1] -= 1
            robot[down_idx] = False
    if a[0] > 0 : 
        robot[0] = True
        a[0] -= 1
    if a.count(0) >= k : 
        break

print(step)


