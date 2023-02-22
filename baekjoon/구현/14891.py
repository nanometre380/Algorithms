# 다시 풀기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# 톱니바퀴
# 톱니바퀴의 톱니마다 N극 S극이 있음
# 톱니바퀴를 K번 회전시키는데 맞닿은 톱니의 극이 다르면 옆의 톱니바퀴는 반대방향으로 회전함
# 맞닿은 톱니의 극이 같으면 회전하지 않음
# N극은 0, S극은 1
# 방향이 1 : 시계방향, 방향이 -1 : 반시계방향
# 점수 계산 = 1번 톱니바퀴 12시 방향이 N극이면 0, S극이면 1
# 2번은 0, 2 / 3번은 0, 4 / 4번은 0, 8

import sys
from collections import deque
input = sys.stdin.readline

dic_search = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
rotation = [0 for _ in range(4)]
wheels = []

def wheel_change(n, direction, rotation) :
    if (rotation[n] != 0) :
        return rotation
    rotation[n] = direction
    for i in dic_search[n] :
        if i < n and wheels[i][2] != wheels[n][6] :
            rotation = wheel_change(i, direction * (-1), rotation)
        elif i > n and wheels[i][6] != wheels[n][2] :
            rotation = wheel_change(i, direction * (-1), rotation)
    return rotation

def rotate_wheel(rotation, wheels) :
    for i in range(4) :
        wheels[i].rotate(rotation[i])
    return wheels

score = 0

for i in range(4) :
    wheels.append(deque(input().rstrip()))

k = int(input())

for i in range(k) :
    n, direction = map(int, input().split())
    rotation = [0 for _ in range(4)]
    rotation = wheel_change(n-1, direction, rotation)
    wheels = rotate_wheel(rotation, wheels)

for i in range(4) :
    score += int(wheels[i][0])*(2**i)

print(score)
    