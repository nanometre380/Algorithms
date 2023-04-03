# 최단거리 문제는 BFS로 풀자!
from collections import deque

def solution(maps):
    answer = 0
    max_x = len(maps)
    max_y = len(maps[0])
    def dfs(x, y) :
        dx = [-1, 1, 0, 0] #상하좌우
        dy = [0, 0, -1, 1]
        queue = deque()
        queue.append((x, y))
        while queue : 
            cur_x, cur_y = queue.popleft()
            for i in range(4) :
                x, y = cur_x+dx[i], cur_y+dy[i]
                if x < 0 or x >= max_x or y < 0 or y >= max_y :
                    continue
                if maps[x][y] == 0 :
                    continue
                if maps[x][y] == 1 :
                    maps[x][y] += maps[cur_x][cur_y]
                    queue.append((x, y))
        return maps[max_x-1][max_y-1]
    answer = dfs(0, 0)
    return answer if answer != 1 else -1


# DFS - 효율성 테스트에서 걸림
"""
min_case = float('inf')
max_r, max_c = 0, 0
check = []

def set_xy(maps) :
    global max_r, max_c
    max_r = len(maps)
    max_c = len(maps[0])
    for _ in range(max_r) :
        check.append([False for _ in range(max_c)])

def get_route(maps, cnt, i, j) :
    global min_case
    if i == max_r-1 and j == max_c-1 :
        min_case = min(min_case, cnt)
    if maps[i][j] == 0 :
        return
    if i <= max_r-2 and check[i+1][j] != True :
        check[i+1][j] = True
        get_route(maps, cnt+1, i+1, j)
        check[i+1][j] = False
    if j <= max_c-2 and check[i][j+1] != True :
        check[i][j+1] = True
        get_route(maps, cnt+1, i, j+1)
        check[i][j+1] = False
    if i >= 1 and check[i-1][j] != True: 
        check[i-1][j] = True
        get_route(maps, cnt+1, i-1, j)
        check[i-1][j] = False
    if j >= 1 and check[i][j-1] != True :
        check[i][j-1] = True
        get_route(maps, cnt+1, i, j-1)
        check[i][j-1] = False
    
def solution(maps):
    global min_case
    set_xy(maps)
    get_route(maps, 1, 0, 0)
    if min_case == float('inf') :
        min_case = -1
    return min_case
"""