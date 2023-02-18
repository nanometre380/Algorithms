# 체스판 다시 칠하기
# 체스판은 검은색 or 흰색
# 맨 위쪽 위 칸이 흰색인 경우, 검은색인 경우
# 다시 칠해야 하는 정사각형의 최소 개수
# 보드 MxN에서 8x8만큼 자르는데 다시 칠해야 하는 최소 개수는?

import sys
input = sys.stdin.readline

lines1 = ["WBWBWBWB", "BWBWBWBW"]
lines2 = ["BWBWBWBW", "WBWBWBWB"]

def calc_paint(r_start, c_start, tiles) :
    count_1 = 0
    count_2 = 0
    for i in range(r_start, r_start+8, 1) :
        for j in range(c_start, c_start+8, 1) :
            if tiles[i][j] != lines1[(i%8)%2][j%8] :
                count_1 += 1
            elif tiles[i][j] != lines2[(i%8)%2][j%8] :
                count_2 += 1
    return min(count_1, count_2)

cnt_min = 64
n, m = map(int, input().split())
tiles = [input().rstrip() for i in range(n)]

for i in range(0, n-7) :
    for j in range(0, m-7) :
        temp_min = calc_paint(i, j, tiles)
        if temp_min < cnt_min :
            cnt_min = temp_min

print(cnt_min)