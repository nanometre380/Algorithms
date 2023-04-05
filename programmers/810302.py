from collections import deque

def dfs(room, sitted) :
    dx = [-1, 1, 0, 0] # 상하좌우
    dy = [0, 0, -1, 1]
    for sit in sitted :
        queue = deque()
        queue.append(sit)
        dist = [[0 for _ in range(5)] for _ in range(5)]
        visited = [[False for _ in range(5)] for _ in range(5)]
        while queue : 
            x, y = queue.popleft()
            visited[x][y] = True
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= 5 or ny < 0 or ny >= 5 :
                    continue
                if visited[nx][ny] == True :
                    continue
                if room[nx][ny] == 'O' :
                    dist[nx][ny] = dist[x][y] + 1
                    visited[nx][ny] = True
                    queue.append([nx, ny])
                if room[nx][ny] == 'P' :
                    if dist[x][y] + 1 <= 2 :
                        return 0
    return 1

def check_dist(place) :
    room = []
    sitted = []
    for i in range(5) :
        room_line = []
        for j in range(5) :
            temp = place[i][j]
            if temp == 'P' :
                sitted.append([i, j])
            room_line.append(temp)
        room.append(room_line)
    return dfs(room, sitted)
            
def solution(places):
    answer = []
    for p in places :
        answer.append(check_dist(p))
    return answer