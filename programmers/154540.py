from collections import deque
def bfs(maps, x, y) :
    dx = [-1, 1, 0, 0] #상하좌우
    dy = [0, 0, -1, 1]
    result = []
    len_x = len(maps)
    len_y = len(maps[0])
    queue = deque()
    queue.append([x, y])
    temp = 0
    while queue :
        x, y = queue.popleft()
        if maps[x][y] != 'X' : 
            temp += int(maps[x][y])
            maps[x][y] = 'X'
            for i in range(4) :
                nx = x+dx[i]
                ny = y+dy[i]
                print("nx, ny : ", nx, ny)
                if nx >= len_x or ny >= len_x or nx < 0 or ny < 0 :
                    continue
                if maps[nx][ny] == 'X' :
                    continue
                if maps[nx][ny] != 'X' :
                    #temp += int(maps[nx][ny])
                    queue.append([nx, ny])
    return temp

def solution(maps):
    answer = []
    maps_list = []
    for line in maps : 
        temp = []
        for c in line : 
            temp.append(c)
        maps_list.append(temp)
    for i in range(len(maps)) :
        for j in range(len(maps[0])) :
            if maps_list[i][j] != 'X' :
                print("st", maps_list[i][j])
                answer.append(bfs(maps_list, i, j))
    if not answer :
        answer = -1 
    return answer

maps = ["X591X","X1X5X","X231X", "1XXX1"]
print(solution(maps))