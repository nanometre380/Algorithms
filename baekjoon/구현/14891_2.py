#톱니바퀴 다시 풀기
#톱니 4개 -> k번 회전시키기 시계 or 반시계
# 톱니바퀴가 회전하려고 할 때 맞닿은 극에 따라서 옆에 있는 바퀴 회전시키기

import sys
from collections import deque
input = sys.stdin.readline

rot = [0 for i in range(6)]

def get_rotation(gears, num, dir) : 
    if num == 0 or num >= 5 :
        return
    rot[num] = dir
    state = gears[num]
    if num-1 > 0 and rot[num-1] == 0 and gears[num-1][2] != state[6] :
        get_rotation(gears, num-1, -1*dir)
    if num+1 < 5 and rot[num+1] == 0 and gears[num+1][6] != state[2] :
        get_rotation(gears, num+1, -1*dir)

def rotate_gear(gears) :
    for i in range(1, len(rot)-1) :
        gears[i].rotate(rot[i])
    return gears

def calc_score(gears) :
    score = 0
    for i in range(1, len(gears)-1) :
        score += int(gears[i][0])*2**(i-1)
    return score

# 입력
gears = ["22222222"]
gears.extend(deque(input().rstrip()) for i in range(4))
gears.append("222222222")
k = int(input())
for _ in range(k) :
    num, dir = map(int, input().split())
    get_rotation(gears, num, dir)
    gears = rotate_gear(gears)
    rot = [0 for i in range(6)]
score = calc_score(gears)
print(score)

