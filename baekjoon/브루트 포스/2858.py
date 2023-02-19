# 기숙사 바닥
# 방 크기는 LxW 가장자리는 빨간색으로 나머지는 갈색으로 칠하기
# 빨간색과 갈색 타일의 개수를 가지고 상근이 방의 크기 구하기

import sys
input = sys.stdin.readline

def get_room(r, b):
    for w in range(5000) :
        for h in range(5000) :
            if r == w*2 + (h-2)*2 and b == w*h-r :
                return max(w, h), min(w, h)

r, b = map(int, input().split())

print(*get_room(r, b))