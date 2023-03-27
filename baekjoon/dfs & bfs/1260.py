from collections import deque
import sys

input = sys.stdin.readline

def dfs(visited_dfs, start, graph) :
    visited_dfs[start] = True
    print(start, end=' ')
    for i in graph[start] :
        if visited_dfs[i] != True : 
            visited_dfs[i] = True
            dfs(visited_dfs, i, graph)

def bfs(visited_bfs, start, graph) :
    visited_bfs[start] = True
    queue = deque([start])
    while queue : 
        temp = queue.popleft()
        print(temp, end=' ')
        for i in graph[temp] :
            if visited_bfs[i] != True :
                visited_bfs[i] = True
                queue.append(i)

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]
visited_bfs = [False for _ in range(n+1)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1) :
    graph[i].sort()
dfs(visited_dfs, v, graph)
print("")
bfs(visited_bfs, v, graph)