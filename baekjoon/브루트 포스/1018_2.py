import sys
input = sys.stdin.readline

def get_count(row, col, tiles) :
    cnt = 0
    for i in range(8) :
        for j in range(8) :
            if (i+j)%2 == 0 and tiles[row+i][col+j] != 'B' :
                cnt += 1
            elif (i+j)%2 != 0 and tiles[row+i][col+j] != 'W' :
                cnt += 1
    if cnt > 32 :
        return 64-cnt
    return cnt


n, m = map(int, input().split())
tiles = [input().rstrip() for _ in range(n)]

min_count = 64

for i in range(n-8+1) :
    for j in range(m-8+1) :
        min_count = min(min_count, get_count(i, j, tiles))

print(min_count)