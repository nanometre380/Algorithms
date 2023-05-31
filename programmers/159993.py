from collections import deque

def bfs(maps, start, target) :
    queue = deque()
    queue.append([start, 0])
    dr = [1, -1, 0, 0] #상하좌우
    dc = [0, 0, -1, 1]
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    while queue : 
        cur, n = queue.popleft()
        r, c = cur[0], cur[1]
        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == target[0] and nc == target[1] :
                return n+1
            if nr >= len(maps) or nr < 0 or nc >= len(maps[0]) or nc < 0 or visited[nr][nc] != False:
                continue
            elif maps[nr][nc] == "X" :
                continue
            queue.append([[nr, nc], n+1])
            visited[nr][nc] = True
    return 0

def solution(maps):
    answer = 0
    targets = {}
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps[i][j] == "L" :
                targets["L"] = [i, j]
            elif maps[i][j] == "E" :
                targets["E"] = [i, j]
            elif maps[i][j] == "S" :
                targets["S"] = [i, j]
    first = bfs(maps, targets["S"], targets["L"])
    if first == 0 :
        return -1
    second = bfs(maps, targets["L"], targets["E"])
    if second == 0 :
        return -1
    return first+second
