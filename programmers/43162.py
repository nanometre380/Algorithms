def dfs(n, visited, computers, cur) :
    visited[cur] = True
    for c in range(n) :
        if cur == c :
            continue
        if computers[cur][c] == 1 and visited[c] != True :
            dfs(n, visited, computers, c)
    

def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    for i in range(n) :
        if visited[i] != True : 
            dfs(n, visited, computers, i)
            answer += 1
    return answer