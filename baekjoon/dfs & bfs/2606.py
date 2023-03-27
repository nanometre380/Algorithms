from collections import deque

def dfs(visited, start, graph) :
    global count
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue : 
        temp = queue.popleft()
        count += 1
        for i in graph[temp] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True

n = int(input())
pairs = int(input())
visited = [False for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
count = 0
for i in range(pairs) :
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

dfs(visited, 1, graph)
print(count-1)